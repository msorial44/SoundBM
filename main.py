from time import time
import sounddevice as sd
import soundfile as sf
from pynput import keyboard
import numpy as np

# Vars
mic_in = 1
mic_out = 6
latency = 0.2 # min 0.2
last_callback = 0

rec_key = "+"
playback_key = "-"
recording = {"data": np.array([], np.float32), 
            "playback": np.array([], np.float32),
            "sr": 0,
            "vol": 1,
            "record_state": False}

#extra binds for uploaded sounds (TODO)
bindings = [{"key":playback_key, "data":recording["playback"], "sr":0, "vol": 1, "active":False}]

# Load configs

# Keyboard handler
def on_press(key):
    try:
        if key.char == rec_key:
            recording["record_state"] = True
        for sound in bindings:
            if key.char == sound["key"]:
                print(sound["key"] + " played")
                sound["active"] = True
                
    except KeyboardInterrupt:
        return False
    except AttributeError as ex:
        print(ex)

def on_release(key):
    try:
        if key.char == rec_key:
            recording["record_state"] = False 
            recording["playback"] = np.copy(recording["data"])
            recording["data"] = np.array([], np.float32)

            bindings[0]["data"] = recording["playback"]
            bindings[0]["sr"] = recording["sr"]
    except KeyboardInterrupt:
        return False
    except AttributeError as ex:
        print(ex)

def start_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

# Audio stream handler
def get_vol_multiplier(vol):
    return pow(2, (np.sqrt(np.sqrt(np.sqrt(vol))) * 192 - 192)/6)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

    
    if recording["record_state"]:
        global last_callback
        recording["data"] = np.append(recording["data"], np.frombuffer(indata, np.float32))
        recording["sr"] = (recording["sr"] + (frames / (time.currentTime - last_callback) * 2)) / 2
        #frames * 68.90625#(1584 * 60 + frames * 60) / 2
        last_callback = time.currentTime
    

    for sound in bindings:
        if sound["active"]:
            sound["active"] = False
            sd.default.device = mic_out
            # this should, by no means known to god, work, but it does
            print("sound sr {} | frames*60: {} ".format(sound["sr"], frames * 60))
            sd.play(sound["data"], sound["sr"])

def start_main_stream():
    print(sd.query_devices())
    try:
        with sd.Stream(device=(mic_in, mic_out), latency=latency, callback=callback):
            print("Press ctrl + c to exit")
            input() # keeps stream open (hacky)
    except KeyboardInterrupt:
        print("\nExited due to user input")
    except:
        print("\nExited due to error")

    sf.write("C:\\Users\\cyber\\Desktop\\Main\\soundboard_py\\record.wav", recording["playback"], 1584 * 60)

# main
def main():
    #load sounds into bindings as arrays
    #binds[0]["data"], binds[0]["fs"] = sf.read("C:\\Users\\cyber\\Desktop\\Main\\soundboard_py\\pda_objective.wav")
    start_input()
    start_main_stream()

main()