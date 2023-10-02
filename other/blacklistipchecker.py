# This CLI script checks if entered ips are or
# aren`t blacklisted on different lists
# You need to get API key on blacklistchecker
# to make it work (it`s free 30 IPs per month)

import json
import re
import sys
from typing import Any

import requests

api_key = "key_CAMF5HI5t4ZzkmgGkioI1tius"


def test_ip(ip: str) -> Any:
    result = requests.get(
        "https://api.blacklistchecker.com/check/" + ip, auth=(api_key, "")
    )
    result_dec = json.loads(result.content)
    print(result_dec)
    if result_dec.get("statusCode"):
        res = "limit exceeded"
        detects = "!"
        return (res, detects)
    elif result_dec.get("detections") != 0:
        res = ip
        blsts = result_dec.get("blacklists")
        detects = []
        for n in blsts:
            if n.get("detected") is True:
                detects.append(n.get("name"))
        return (res, detects)


def isip(ip: str) -> bool:
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    if not bool(match):
        return False
    octets = ip.split(".")
    return all(not (int(b) < 0 or int(b) > 255) for b in octets)


res_txt = "IP blacklists check returned next results:\n"
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        if isip(x) is not True:
            print(f"IP {x} is incorrect\n")
        else:
            if test_ip(x) is not None:
                res, detec = test_ip(x)
                if res == "limit exceeded":
                    res_txt = res_txt + " LIMIT Exceeded!"
                    break
                else:
                    res_txt += f"{res} is detected in {detec} blacklists \n \n"
else:
    print("Type in ip to check")
    x = input()
    if isip(x) is not True:
        print(f"IP {x} is incorrect\n")
    else:
        if test_ip(x) is not None:
            res, detec = test_ip(x)
            if res == "limit exceeded":
                res_txt = res_txt + "Limit Exceeded!\n"
            else:
                res_txt += f"{res} is detected in {detec} blacklists \n \n"
if len(res_txt) <= 43:
    print("IPs not blacklisted!")
    print(res_txt)
else:
    print("Blacklist check result is: \n" + res_txt)
