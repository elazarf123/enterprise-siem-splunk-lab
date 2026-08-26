# From Plain English to Threat Hunting

## Introduction
Security Operations Center (SOC) analysts face constant friction translating raw operational intent into complex Search Processing Language (SPL).

## Scenario: Brute-Force Detection
- **Prompt:** Find failed admin logins.
- **SPL:** sourcetype="security_events" action="LOGIN_FAILED" user="admin" | stats count by src_ip | where count > 2
