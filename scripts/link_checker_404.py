
import os
import requests
import re
import urllib.request

failed_links_total = 0
directory = "../course"

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            open_file = open(os.path.join(root, file), encoding="utf8")
            filecontent = open_file.read()
            links = re.findall(r'\[.*?\]\((.*?)\)', filecontent)
            failed = 0
            broken_links = []

            for link in links:
                if link.startswith('http') or link.startswith('https'):  # Exclude local links
                    try:
                        response = session.head(link, timeout=10)
                        if response.status_code == 404:
                            failed += 1
                            failed_links_total += 1
                            broken_links.append(str(link))
                    except requests.exceptions.RequestException:
                        print(f"Error checking link in file '{file}': {link}")

            if failed > 0:
                print(f"{failed} link(s) failed for page {file}.")
                print("---------------------------")
                for url in broken_links:
                    print(url)
                    print("---------------------------")

#assert failed_links_total == 0, "broken links found"