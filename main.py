import sounddevice as sd
import soundfile as sf
from pynput import keyboard
import numpy as np

# Vars
mic_in = 1 #file read needed ( TODO )
mic_out = 2 #file read needed
latency = 0.2
last_callback = 0

RECORD_COMBINATION = {keyboard.Key.shift_r, keyboard.Key.down} #read file needed ( TODO )
DELETE_COMBINATION = {keyboard.Key.shift_r, keyboard.Key.up}


rec_key = "+" #file read needed
playback_key = "-"#file read needed ( TODO )
playback_key2 = "_" #file read needed
recording = {"data": np.array([], np.float32), 
            "playback": np.array([], np.float32),
            "sr": 0,
            "vol": 1,
            "record_state": False}

#extra binds for uploaded sounds (TODO)
#need to loop depending on amount of keybinds in file
bindings = [
    {
    "key":playback_key, 
    "data":np.array([], np.float32), 
    "sr":0, 
    "vol": 1, 
    "active":False,
    'isUsed': False
    },
    {
    "key":playback_key2, 
    "data":np.array([], np.float32), 
    "sr":0, 
    "vol": 1, 
    "active":False,
    'isUsed': False
    },
]

# Load configs

# Keyboard handler
def on_press(key):
    try:
        if key.char == rec_key:
            recording["record_state"] = True #starts recording
        for sound in bindings: #for each indivual sound in bindings
            if key.char == sound["key"]: #if the key pressed is the same as the key in the sound
                print(sound["key"] + " played")
                sound["active"] = True #starts playing the sound
                
    except KeyboardInterrupt:
        return False
    except AttributeError as ex:
        print(ex)

def on_release(key):
    try:
        if key.char == rec_key: #if key released is recording key
            recording["record_state"] = False #stop recording
            recording["playback"] = np.copy(recording["data"]) #copy the sound from data to playback
            recording["data"] = np.array([], np.float32) #clear the sound from data
            
            for sound in bindings:
                if sound["isUsed"] == False:
                    sound["isUsed"] = True
                    sound["data"] = recording["playback"] #set the sound from recording to bindings
                    sound["sr"] = recording["sr"]
                    break
    except KeyboardInterrupt:
        return False
    except AttributeError as ex:
        print(ex)

def start_input(): #starts listening on the keyboard
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

# Audio stream handler
def get_vol_multiplier(vol): #not used
    return pow(2, (np.sqrt(np.sqrt(np.sqrt(vol))) * 192 - 192)/6)

def callback(indata, outdata, frames, time, status):
    if status: #prints status of stream
        print(status)
    outdata[:] = indata #not sure what this is ( TODO )

    if recording["record_state"]: #if recording is true then record to data
        recording["data"] = np.append(recording["data"], np.frombuffer(indata, np.float32))
        recording["sr"] = frames * 68.90625#(1584 * 60 + frames * 60) / 2

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

    for sound in bindings:
        sf.write("C:\\Users\\cyber\\Desktop\\Main\\soundboard_py\\record.wav",sound["playback"], 1584 * 60)
    

# main
def main():
    #load sounds into bindings as arrays
    #binds[0]["data"], binds[0]["fs"] = sf.read("C:\\Users\\cyber\\Desktop\\Main\\soundboard_py\\pda_objective.wav")
    start_input()
    start_main_stream()

main()