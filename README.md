# Splunk SIEM Lab

A home lab that runs Splunk Enterprise in Docker, ingests simulated authentication logs, detects brute-force logins with an SPL search, and passes the alert to Python scripts that enrich it and summarize it against NIST CSF and CIS Controls.

## Results

**Sample output (illustrative).** These numbers come from the fixed sample file [`sample_security_events.log`](sample_security_events.log) (12 events), not from a real network.

Brute-force search results on the sample log:

| user | src_ip | failed logins |
| :--- | :--- | :--- |
| `admin` | `203.0.113.5` | 4 |
| `service_account` | `172.16.4.22` | 3 |

Compliance summary from [`executive_compliance_report.json`](executive_compliance_report.json):

| Metric | Value |
| :--- | :--- |
| Events processed | 12 |
| Alerts enriched | 1 |
| High-severity alerts | 1 |
| Containment recommendations | 1 |

## How it works

- [`log_simulator.py`](log_simulator.py) writes 50 random authentication events to `security_events.log` (users, source IPs, success/failure).
- The log is uploaded to Splunk under `sourcetype=security_events`; this SPL search flags any user + IP pair with more than 2 failed logins:
  ```spl
  sourcetype="security_events" action="LOGIN_FAILED" | stats count by user, src_ip | where count > 2 | sort - count
  ```
- [`soar_enrichment.py`](soar_enrichment.py) takes the `admin` / `203.0.113.5` alert, adds a **mocked** threat-intel response shaped like AbuseIPDB (no API call), and recommends blocking the IP when the score is above 75. It writes [`enriched_incident_ticket.json`](enriched_incident_ticket.json). No firewall change is made.
- [`compliance_reporter.py`](compliance_reporter.py) counts events and alerts and maps them to NIST CSF 2.0 (DE.CM, RS.AN) and CIS Controls v8 (8, 17) in [`executive_compliance_report.json`](executive_compliance_report.json).
- [`ai_triage_simulator.py`](ai_triage_simulator.py) shows how a plain-English request maps to the same SPL search and MITRE ATT&CK T1110. The query and summary are hardcoded examples; no AI model is called. Notes are in [`AI_SOC_HUNTING_GUIDE.md`](AI_SOC_HUNTING_GUIDE.md).

## Tech stack

Splunk Enterprise · SPL · Docker · Python 3 (standard library only)

## Run it

```bash
git clone https://github.com/elazarf123/enterprise-siem-splunk-lab.git
cd enterprise-siem-splunk-lab

# 1. Start Splunk. Choose your own admin password (8+ characters); never commit it.
export SPLUNK_PASSWORD='change-me-to-a-strong-password'
docker run -d -p 8000:8000 \
  -e "SPLUNK_GENERAL_TERMS=--accept-sgt-current-at-splunk-com" \
  -e "SPLUNK_START_ARGS=--accept-license" \
  -e "SPLUNK_PASSWORD=$SPLUNK_PASSWORD" \
  --name splunk-enterprise splunk/splunk:latest

# 2. Generate logs (or use sample_security_events.log)
python log_simulator.py

# 3. In Splunk (http://localhost:8000, user admin): Settings > Add Data > Upload,
#    choose security_events.log, set sourcetype to security_events, then run the SPL search above.

# 4. Enrich the alert and build the summary
python soar_enrichment.py
python compliance_reporter.py
```

## What I learned

- A detection is only convincing when the sample data, the search results, and the report all agree.
- Splunk extracts `key=value` pairs automatically, so a consistent log format matters more than a custom parser.
- Credentials belong in environment variables, not in commands or READMEs.

## Roadmap

- Call the real AbuseIPDB API with a key read from an environment variable
- Save the SPL search as a scheduled Splunk alert
- Pull the event count straight from Splunk instead of the log file

> Lab use only. All events, IPs, and threat-intel values are simulated.
