from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pretty_table import PrettyShow
from check_proxy import ProxyChecker, correct_proxies
import threading
import concurrent.futures
import time
import os

# -------------------------------- CONSTANT --------------------------------
PROXIES = []
THREADS = []

# -------------------------------- SETTINGS --------------------------------
options = Options()
options.add_argument("--headless")
# driver = webdriver.Chrome("/home/development/chromedriver", options=options)
driver = webdriver.Chrome("/Users/ali/Development/chromedriver", options=options)

# -------------------------------- GET PROXIES --------------------------------
url_req = "https://spys.one/en/https-ssl-proxy"
driver.get(url_req)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "lxml")
driver.close()

trs = soup.find_all('tr', {'class': ['spy1x', 'spy1xx']})
for i in trs[1:]:
    PROXIES.append(i.select_one('td').text.strip())

table = PrettyShow()
table.pretty_table(PROXIES)

# -------------------------------- CHECK PROXIES --------------------------------
t1 = time.perf_counter()

for proxy in PROXIES:
    t = threading.Thread(target=ProxyChecker, args=(proxy,))
    t.start()
    THREADS.append(t)
for thread in THREADS:
    thread.join()

table.pretty_table(correct_proxies)

t2 = time.perf_counter()
print(f'Finished in {t2 - t1} seconds')


# -------------------------------- CREATE CONTAINERS --------------------------------
def containers(p: str):
    os.system(f'docker container run --name t{correct_proxies.index(p)} -it yyy')
    # os.system(f'docker container run --name t{correct_proxies.index(p)} --env HTTPS_PROXY="https://{p}" xxx')


t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(containers, correct_proxies)
t2 = time.perf_counter()
print(f'Finished in {t2 - t1} seconds')
