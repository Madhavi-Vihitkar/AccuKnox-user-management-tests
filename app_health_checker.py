#!/usr/bin/env python3
import requests
import time
import logging

# Configure logging
logging.basicConfig(filename="app_health.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

URL = "https://opensource-demo.orangehrmlive.com/"  # replace with your app URL
CHECK_INTERVAL = 60  # seconds

def check_application():
    try:
        response = requests.get(URL, timeout=10)
        status_code = response.status_code
        if status_code == 200:
            print(f"✅ Application is UP (Status Code: {status_code})")
            logging.info(f"Application UP (Status Code: {status_code})")
        else:
            print(f"⚠️ Application may be DOWN (Status Code: {status_code})")
            logging.warning(f"Application DOWN (Status Code: {status_code})")
    except requests.exceptions.RequestException as e:
        print(f"❌ Application is DOWN - Error: {e}")
        logging.error(f"Application DOWN - Error: {e}")

if __name__ == "__main__":
    print(f"Monitoring application health for: {URL}")
    while True:
        check_application()
        time.sleep(CHECK_INTERVAL)
