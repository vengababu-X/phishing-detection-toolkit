import logging

logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logging.info(f"Scanned URL: {url} | Result: {result}")
