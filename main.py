import os
import time
import subprocess

next_page_file = "next_button_url.txt"

# Loop until the next_page file is not marked as "DONE"
while True:
    # Run the scrapper.py script using subprocess
    subprocess.run(["/usr/bin/python3", "scrape.py"])

    # Wait for a few seconds before checking the next_page file again
    time.sleep(5)

    # Check the content of the next_page file
    with open(next_page_file, "r") as file:
        next_page_status = file.read().strip()

    # If the next_page file contains "DONE", break the loop
    if next_page_status == "DONE":
        break
