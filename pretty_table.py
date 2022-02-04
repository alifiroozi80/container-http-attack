from prettytable import PrettyTable
import urllib.request
import json


class PrettyShow:
    def __init__(self):
        self.IP = []
        self.PORT = []
        self.COUNTRY = []
        self.CITY = []

    def pretty_table(self, items: list) -> None:
        """
        Show items in a very neat order
        :param items:
        :return:
        """
        self.IP.clear()
        self.PORT.clear()
        self.COUNTRY.clear()
        self.CITY.clear()

        t = PrettyTable()
        t.field_names = ["IP", "PORT", "COUNTRY", "CITY", "PROXY"]
        for p in items:
            self.IP.append(p.split(":")[0])
            self.PORT.append(p.split(":")[1])
        for ip in self.IP:
            try:
                with urllib.request.urlopen(f"https://geolocation-db.com/json/{ip}") as url:
                    data = json.loads(url.read().decode())
                    self.COUNTRY.append(data.get("country_name"))
                    self.CITY.append(data.get("city"))
            except Exception as e:
                print(f"ERROR: {e}")
        for i in range(len(self.IP)):
            t.add_row([self.IP[i], self.PORT[i], self.COUNTRY[i], self.CITY[i], items[i]])
        print(t)
