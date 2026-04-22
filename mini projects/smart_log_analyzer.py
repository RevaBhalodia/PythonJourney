from collections import defaultdict

def detect_anomalies(logs, threshold=3):
    ip_count = defaultdict(int)

    for log in logs:
        ip = log.split()[0]
        ip_count[ip] += 1

    return [ip for ip, count in ip_count.items() if count > threshold]

logs = [
    "192.168.1.1 GET /home",
    "192.168.1.1 GET /about",
    "192.168.1.2 GET /home",
    "192.168.1.1 GET /contact",
    "192.168.1.1 GET /login"
]

print(detect_anomalies(logs))