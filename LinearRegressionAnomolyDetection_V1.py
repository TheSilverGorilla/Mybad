import subprocess
import os
import pathlib
import matplotlib.pyplot as plt
from scipy import stats
import numpy


word_dict = {'cal':1, 'bc':1, 'expr':1, 'export':1, 'date':1, 'mkdir':2, 'rmdir':2, 'dir':2, 'ls':2, 'pwd':2, 'cd':2,
             'tr':3, 'uniq':3, 'split':3, 'wc':3, 'head':3, 'cut':3, 'diff':3, 'join':3, 'more':3, 'less':3, 'sort':3, 'comm':3,
             'cat':3, 'tail':3, 'find':4, 'Is':4, 'rm':4, 'locate':4, 'cp':4, 'du':4, 'file':4, 'mv':4, 'grep':4, 'egrep':4,
             'fgrep':4, 'man':4, '|': 1, 'xargs':-3, 'tar':5, 'gzip':5, 'gunzip':5, 'zcat':5, 'uuedcode':5, 'zip':5, 'unizip':5,
             'rmp':5, 'bzip2':5, 'bunzip2':5, 'rar':5, 'ex':6, 'vi':6, 'nano':6, 'view':6, 'emacs':6, 'sublime':6, 'sed':6,
             'pico':6, 'df':7, 'mkfs':7, 'resize2fs':8, 'fsck':7, 'pvcreate':7, 'mount':7, 'fdisk':7, 'lvcreate':7, 'umount':7,
             'free':8, 'killall':8, 'sensors':8, 'top':8, 'kill':8, 'service':8, 'ps':4, 'aux':4, 'dmesg':8, 'jobs':6, 'uname':9,
             'whoami':7, 'ifconfig':9, 'telnet':9, 'netstat':9, 'tcpdump':12, 'ssh':12, 'ping':8, 'arp':8, 'nmap':20, 'ncat':14,
             'awk':7, 'gwk':7, 'tsh':7, 'python3':6, 'bash':6, 'ksh':6, 'php':7, 'csh':8, 'tcsh':8, 'perl':6, 'ruby':6, 'python':6,
             'sudo':12, 'chmod':12, 'touch':5, 'chown':20, 'chgrp':20, 'nohup':15, 'chage':20, 'chrontab':13}

fin_vals = 0
x1 = [1]
y1 = [1]
x2 = [1]
y2 = [1]
break_function = False
yval = 1


def lin_reg(xcord,ycord):
    slope, intercept, r, p, std_err = stats.linregress(xcord, ycord)

    def line(x):
        return slope * x + intercept

    return line(5) + line(7)

def line_regression_in(xcord, ycord, instance):
    global fin_vals
    global break_function
    global yval
    password = 'user'
    pwd_input = input('Type in your password: ')
    def exec(cmd):
        cmd = (cmd.split(' '))
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout = process.communicate()[0]
        print(stdout.decode())

    def get_number(l):
        temp = 0
        for i in l:
            try:
                temp = temp + word_dict.get(i)
            except:
                pass
        return temp

    t = True
    request_string = os.getcwd()
    while t == True:
        h = input(request_string+'/~')
        if instance > 1 and yval == 7:
            print(value_1, lin_reg(xcord, ycord), lin_reg(xcord, ycord) - value_1)
            if abs(lin_reg(xcord, ycord) - value_1) > 5:
                print("Peculiar Command Entry Detected")
                t = False
            instance = 1
        else:
            if h == 'stop':
                t = False
            else:
                try:
                    cd_cmd = h.split(' ')
                    if cd_cmd[0] == 'cd':
                        if cd_cmd[1] == '~':
                            request_string = pathlib.Path(__file__).parent.resolve()
                            os.chdir(request_string)
                        try:
                            request_string = os.path.abspath(cd_cmd[1])
                            os.chdir(request_string)
                        except:
                            pass
                    ycord.append(ycord[yval - 1] + get_number(h.split(' ')))
                    yval = yval + 1
                    xcord.append(yval)
                    exec(h)

                except Exception as e:
                    print('Invalid Command: Reason - ', e)
    slope, intercept, r, p, std_err = stats.linregress(xcord, ycord)
    def line(x):
        return slope * x + intercept

    yval = 1
    return line(5) + line(7)




value_1 = line_regression_in(x1, y1, 1)
print(value_1)
h = input("Enter to start again")
value_2 = line_regression_in(x2, y2, 2)
print(value_2)
