import urllib.request
import socket
import urllib.error
import threading
import time

correct_proxies = []


class ProxyChecker:
    def __init__(self, proxy: str):
        self.main(p=proxy)

    def is_bad_proxy(self, pip: str) -> bool:
        """
        The checker function
        :param pip:
        :return:
        """
        try:
            proxy_handler = urllib.request.ProxyHandler({"http": pip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [("User-agent", "Mozilla/5.0")]
            urllib.request.install_opener(opener)
            req = urllib.request.Request("http://www.example.com")
            sock = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
            # return e.code
        except Exception as detail:
            print(f"ERROR: {detail}")
            return True
        return False

    def main(self, p: str) -> None:
        """
        main function plus appender to correct proxies list
        :param proxy_list:
        :return:
        """
        socket.setdefaulttimeout(120)

        if self.is_bad_proxy(p):
            print(f"BAD Proxy ====> {p}")
        else:
            # print(f"{current_proxy} is working")
            correct_proxies.append(p)
            print(f"HEALTHY Proxy ====> {p}")
