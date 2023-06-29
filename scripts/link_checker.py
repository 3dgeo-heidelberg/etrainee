import sys
import os
from urlextract import URLExtract
import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen, http
import re
from string import *


failed_links_total = 0
directory = "../course"
for root, dirs, files in os.walk(directory):
    for file in files:
        if (file.endswith(".md")):
            open_file = open(os.path.join(root, file),encoding="utf8")
            try:
                urls_clean = []
                urls_to_check = []
                urls_to_check2 = []
                extensions = [")", ".", ",", "</i>"] # list of artefacts from re.findall (line 24)
                substring = "]("
                filecontent = open_file.read()
                urls = re.findall(r'(https?://\S+)', filecontent) # might be replaced by more sophisticated regex to avoid artefacts but didn't find one working better than this simple one

                # find links where linktext and url are identical
                for idx, url in enumerate(urls):
                    if substring in str(url):
                        url_split = url.split("]")
                        url_clean = url_split[0] # only take first element because the two elements (=links) are identical
                        urls_clean.append(url_clean)

                    else:
                        urls_to_check.append(url)

                # clean remaining links from artefacts resulting from re.findall
                for idx, url in enumerate(urls_to_check):
                    for extension in extensions:
                        if url.endswith(extension):
                            url_split = url.split(")")
                            url_clean = url_split[0]
                            urls_clean.append(url_clean)

                        else:
                            urls_to_check2.append(url)



            except Exception as err:
                print(err)

            failed = 0
            i = 0
            broken_links = []
            for url in urls_clean:
                try:

                    req_link = urllib.request.Request(url, headers={
                        'User-Agent': "Magic Browser"})

                    response = requests.get(url)
                    if response.status_code == 200:
                        continue

                except Exception as err:
                    failed += 1
                    failed_links_total += 1
                    broken_links.append(str(url))
                    if failed >= 0:
                        print(("%i link(s) failed for page %s." % (failed, file)))
                        print("---------------------------")
                        for link in broken_links:
                            print(link)
                            print("---------------------------")

assert failed_links_total == 0, "broken links found"
