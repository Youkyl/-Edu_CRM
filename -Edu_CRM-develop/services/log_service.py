from datetime import datetime


logs = []

def log_action(user, action, target):
    entry = {
        "id": len(logs) + 1,
        "user": user,
        "action": action,
        "target": target,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    logs.append(entry)

def get_logs():
    return list(reversed(logs))

def clear_logs():
    logs.clear()