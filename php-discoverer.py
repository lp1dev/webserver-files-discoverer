#!/bin/python
from sys import argv
import asyncio
import requests
import concurrent

report_file = "report.txt"
filesLists = argv[2:]

def             usage():
  print("%s : domain files_list1 files_list2 [...]" %argv[0])
  return -1

def             add_to_report(filename):
  with open(report_file, "a+") as f:
    f.write("%s\n" %filename)

def             get_list(url):
  r = requests.get(url)
  return r.text.split()

def             test_file(domain, filename):
  url = domain
  if domain[len(domain) - 1] is "/":
    url += filename
  else:
    url += "/%s" %filename
  r = requests.get(url)
  if (r.status_code - (r.status_code % 100) == 200): # Checking if the status code is 2XX
    print("\t[+] found existing file %s" %url)
    add_to_report(filename)
    return url
  return False

async def       discover(domain, files, threads=2):
  print("Starting PHP Discoverer\nScan report for %s" %domain)
  print("Scanning %i filenames (using %i threads)" % (len(files), threads))
  results = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(executor, test_file, domain, filename) for filename in files]
    for response in await asyncio.gather(*futures):
      if response is not False:
        results.append(response)

def             main():
  if len(filesLists) < 1:
    return usage()
  domain = argv[1]
  files = []
  for fileList in filesLists:
    files += get_list(fileList)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(discover(domain, files))
  return 0

if __name__ == '__main__':
  main()
