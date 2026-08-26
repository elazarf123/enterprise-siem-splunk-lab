import json
import datetime

def simulate_ai_triage():
    print("--------------------------------------------------")
    print("      SPLUNK AI ASSISTANT & SOC TRIAGE SIMULATOR  ")
    print("--------------------------------------------------")
    
    natural_language_query = "Find all failed login attempts targeting the admin account from external IPs and map them to potential brute-force vectors."
    
    print(f"[?] Natural Language Prompt: \"{natural_language_query}\"")
    print("[*] Translating prompt via Security LLM / Splunk AI Assistant...")
    
    generated_spl = "sourcetype=\"security_events\" action=\"LOGIN_FAILED\" user=\"admin\" | stats count by src_ip | where count > 2 | sort - count"
    
    print(f"[+] Generated SPL Query:\n    {generated_spl}\n")
    
    triage_summary = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "analyst_interface": "AI-Augmented Natural Language Assistant",
        "intent_classification": "Credential Access / Brute-Force",
        "mitre_att_ck_mapping": "T1110 - Brute Force",
        "ai_generated_summary": "High-confidence brute-force pattern detected targeting administrative service accounts. Source IP telemetry indicates external origin with recurring failed authentication states crossing the threshold velocity.",
        "recommended_action": "Execute automated SOAR playbook for IP containment and firewall block."
    }
    
    output_file = "ai_triage_incident_summary.json"
    with open(output_file, "w") as f:
        json.dump(triage_summary, f, indent=4)
        
    print(f"[+] Success: AI triage report generated and saved to '{output_file}'")
    print("--------------------------------------------------")

if __name__ == "__main__":
    simulate_ai_triage()
