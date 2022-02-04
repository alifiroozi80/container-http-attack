# from ping3 import verbose_ping
#
# verbose_ping('example.com')
# print("------------------")

import os

user = input("1-ping / 2-http")

if int(user) == 1:
    os.system("ping www.google.com")
else:
    os.system("httping www.google.com")
