# Enterprise SIEM & Log Analysis Lab (Splunk Enterprise & Docker)

## Overview
A lightweight, containerized Security Information and Event Management (SIEM) architecture deployed to simulate enterprise-grade security monitoring, log ingestion, and threat detection analysis while bypassing local resource bottlenecks.

## Architecture & Tech Stack
* **Containerization:** Docker Desktop (WSL 2 backend for host kernel isolation)
* **SIEM Platform:** Splunk Enterprise (Latest)
* **Threat Simulation:** Python 3 (Custom Telemetry Generator)
* **Host Environment:** Windows / Linux WSL 2 integration

## Deployment Procedure

### Step 1: Pull the Container Image
```bash
docker pull splunk/splunk:latest 
docker run -d -p 8000:8000 -e "SPLUNK_GENERAL_TERMS=--accept-sgt-current-at-splunk-com" -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=splunk123" --name splunk-enterprise splunk/splunk:latest
docker logs -f splunk-enterprise
import datetime
import random

users = ["admin", "jsmith", "bwayne", "tstark", "service_account"]
source_ips = ["192.168.1.50", "10.0.0.15", "172.16.4.22", "203.0.113.5"]
actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "PASSWORD_RESET", "UNAUTHORIZED_ACCESS_ATTEMPT"]

def generate_log_entry():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = random.choice(users)
    ip = random.choice(source_ips)
    action = random.choice(actions)
    return f"[{timestamp}] SEVERITY={'HIGH' if 'FAILED' in action or 'UNAUTHORIZED' in action else 'INFO'} user={user} src_ip={ip} action={action}\n"

if __name__ == "__main__":
    with open("security_events.log", "w") as f:
        for _ in range(50):
            f.write(generate_log_entry())
    print("Generated 50 simulated security log entries in security_events.log")
sourcetype="security_events" action="LOGIN_FAILED" | stats count by user, src_ip | where count > 2 | sort - count
python soar_enrichment.py
