import time
from concurrent.futures import ThreadPoolExecutor
def fetch_data(url:str):
    print("fetching data from:",url)
    time.sleep(4)
    print("Data fetching from",url)
    return "Data from "+ url
url_lists = ["https://example.com/api/data1",
             "https://example.com/api/data2",
             "https://example.com/api/data3",
             "https://example.com/api/data4",
             "https://example.com/api/data5"]
results = []
with ThreadPoolExecutor(max_workers=len(url_lists))as executor:
    futures = executor.map(fetch_data,url_lists)
    results.extend(futures)
print(results)

for i in url_lists:
    fetch_data(i)