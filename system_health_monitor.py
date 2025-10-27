#!/usr/bin/env python3
import psutil
import datetime
import logging

# Set up logging
logging.basicConfig(filename="system_health.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 85

def log_alert(message):
    print(f"[ALERT] {message}")
    logging.warning(message)

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")

    if cpu > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory}%")
    if disk > DISK_THRESHOLD:
        log_alert(f"Low Disk Space: {disk}% used")

    logging.info(f"Health Check -> CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}")

if __name__ == "__main__":
    print(f"System Health Check - {datetime.datetime.now()}")
    check_system_health()
