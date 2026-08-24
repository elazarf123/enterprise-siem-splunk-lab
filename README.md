# Enterprise SIEM & Log Analysis Lab (Splunk Enterprise & Docker)

## Overview
A lightweight, containerized Security Information and Event Management (SIEM) architecture deployed to bypass local resource bottlenecks and simulate enterprise-grade security monitoring, log ingestion, and threat detection analysis.

## Architecture & Tech Stack
* **Containerization:** Docker Desktop (WSL 2 backend for high-performance host kernel isolation)
* **SIEM Platform:** Splunk Enterprise (Latest)
* **Host Environment:** Windows / Linux WSL 2 integration

## Deployment Procedure
1. **Pull the Container Image:**
   ```bash
   docker pull splunk/splunk:latest
