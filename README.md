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
`ash
docker pull splunk/splunk:latest
docker run -d -p 8000:8000 -e "SPLUNK_GENERAL_TERMS=--accept-sgt-current-at-splunk-com" -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=splunk123" --name splunk-enterprise splunk/splunk:latest
docker logs -f splunk-enterprise
