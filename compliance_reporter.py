import json
import datetime
import os

def generate_compliance_report():
    print("--------------------------------------------------")
    print("      EXECUTIVE COMPLIANCE & METRICS ENGINE       ")
    print("--------------------------------------------------")
    
    # Load recent ticket data if available
    events_file = "security_events.log"
    total_events = 0
    if os.path.exists(events_file):
        with open(events_file, "r") as f:
            total_events = sum(1 for line in f if line.strip())

    ticket_file = "enriched_incident_ticket.json"
    incident_count = 0
    high_severity_count = 0
    mitigated_count = 0
    
    if os.path.exists(ticket_file):
        with open(ticket_file, "r") as f:
            ticket_data = json.load(f)
            incident_count = 1
            if ticket_data.get("alert", {}).get("severity") == "HIGH":
                high_severity_count = 1
            if "CONTAINMENT_RECOMMENDED" in ticket_data.get("automation_verdict", ""):
                mitigated_count = 1

    report = {
        "report_metadata": {
            "framework_alignment": "NIST CSF v2.0 / CIS Controls v8",
            "generated_timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "reporting_period": "Lab sample run"
        },
        "operational_metrics": {
            "total_security_events_processed": total_events,
            "automated_incidents_triaged": incident_count,
            "high_severity_threats_identified": high_severity_count,
            "containment_recommendations": mitigated_count
        },
        "framework_mapping": {
            "NIST_CSF_v2": ["DE.CM (Continuous Monitoring)", "RS.AN (Incident Analysis)"],
            "CIS_Controls_v8": ["Control 8 (Audit Log Management)", "Control 17 (Incident Response Management)"]
        }
    }
    
    output_filename = "executive_compliance_report.json"
    with open(output_filename, "w") as f:
        json.dump(report, f, indent=4)
        
    print(f"[+] Success: Executive compliance report compiled and written to '{output_filename}'")
    print("[+] Framework Mapped: NIST CSF (Detect & Respond Core Functions)")
    print("--------------------------------------------------")

if __name__ == "__main__":
    generate_compliance_report()
