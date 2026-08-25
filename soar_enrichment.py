import json
import datetime

incoming_alert = {
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "user": "admin",
    "source_ip": "185.220.101.5",
    "action": "UNAUTHORIZED_ACCESS_ATTEMPT",
    "severity": "HIGH"
}

def query_abuseipdb(ip_address):
    print(f"[*] SOAR Pipeline: Intercepted alert for IP {ip_address}")
    print("[*] SOAR Pipeline: Querying Threat Intelligence API (AbuseIPDB)...")
    return {
        "ipAddress": ip_address,
        "isPublic": True,
        "abuseConfidenceScore": 98,
        "country": "RE",
        "usageType": "Data Center/Web Hosting/Tor",
        "totalReports": 1420
    }

def run_soar_playbook():
    print("--------------------------------------------------")
    print("       ENTERPRISE SOAR AUTOMATION PLAYBOOK        ")
    print("--------------------------------------------------")
    print(f"[+] Alert Triggered at: {incoming_alert['timestamp']}")
    print(f"[+] Target User: {incoming_alert['user']}")
    print(f"[+] Suspicious IP: {incoming_alert['source_ip']}")
    
    intel_data = query_abuseipdb(incoming_alert['source_ip'])
    score = intel_data.get("abuseConfidenceScore", 0)
    print(f"[*] Threat Intel Verdict: Abuse Confidence Score = {score}%")
    
    if score > 75:
        action_taken = "CONTAINMENT_RECOMMENDED: Auto-blocking IP at firewall and escalating ticket severity."
    else:
        action_taken = "MONITOR: Score below threshold, logging event for review."
        
    print(f"[+] SOAR Action: {action_taken}")
    
    enriched_incident = {
        "alert": incoming_alert,
        "threat_intel": intel_data,
        "automation_verdict": action_taken,
        "processed_timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open("enriched_incident_ticket.json", "w") as f:
        json.dump(enriched_incident, f, indent=4)
        
    print("[+] Success: Enriched incident ticket written to 'enriched_incident_ticket.json'")
    print("--------------------------------------------------")

if __name__ == "__main__":
    run_soar_playbook()
