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
