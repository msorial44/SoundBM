import sounddevice as sd
import soundfile as sf
from pynput import keyboard
import numpy as np

# Vars
mic_in = 1
mic_out = 6
binds = [{"key":"v", "data":[], "fs":0, "active":False}]

# Load configs


# Keyboard handler
def on_press(key):
    try:
        for bind in binds:
            if key.char == bind["key"]:
                print(bind["key"] + " played")
                bind["active"] = True
                
    except KeyboardInterrupt:
        return False
    except AttributeError as ex:
        print(ex)

def start_input():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    #listener.join()

# Audio stream handler
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    
    for bind in binds:
        if bind["active"]:
            bind["active"] = False
            sd.default.device = 6
            volFactor = 0.25
            mult = pow(2, (np.sqrt(np.sqrt(np.sqrt(volFactor))) * 192 - 192)/6)
            sd.play(bind["data"] * mult, bind["fs"])

def start_main_stream():
    print(sd.query_devices())
    try:
        with sd.Stream(device=(1, 6), latency=0.25, callback=callback):
            print("Press ctrl + c to exit")
            input() # keeps stream open (hacky)
    except KeyboardInterrupt:
        print("\nExited due to user input")
    except:
        print("\nExited due to error")

# main
def main():
    binds[0]["data"], binds[0]["fs"] = sf.read("C:\\Users\\cyber\\Desktop\\Main\\soundboard\\pda_objective.wav")
    start_input()
    start_main_stream()

main()