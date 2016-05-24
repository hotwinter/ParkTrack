from pwn import *
import requests

r = serialtube(timeout=10)
r.recvuntil('')
