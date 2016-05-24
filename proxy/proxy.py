from pwn import *
import json
import requests

r = serialtube(port='/dev/ttyACM0',timeout=10, baudrate=9600)
res = r.recv()
while ("SENSOR" in res):
    print res
    res = r.recv()
    if 'Setup Finished' in res:
        break
r.recvline()
in_num = 0
out_num = 0
previn = 0
prevout = 0
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
while True:
    res = r.recvline()
    if "IN" in res:
        in_num = int(res.strip().split(":")[1])
    elif "OUT" in res:
        out_num = int(res.strip().split(":")[1])
    if in_num != previn or out_num != prevout:
        log.info("Sending to webserver!")
        json_dict = {"out":out_num, "in":in_num}
        requests.post('http://127.0.0.1:5000/summary', data=json.dumps(json_dict), headers=headers).text
        previn = in_num
        prevout = out_num
    res = r.recvline()
