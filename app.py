import time
import numpy as np
import sounddevice as sd
import librosa
import keyboard  # Detect keypress events
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pydub import AudioSegment

# Load Azan audio sample (Converted to WAV)
AZAN_AUDIO_FILE = "C:/Users/shayon/Downloads/azan10.wav"

# Load and extract MFCC features from the Azan sample
y_azan, sr_azan = librosa.load(AZAN_AUDIO_FILE, sr=22050)
mfcc_azan = librosa.feature.mfcc(y=y_azan, sr=sr_azan, n_mfcc=13)
azan_features = np.mean(mfcc_azan, axis=1)

# Function to mute/unmute system sound
def mute_sound(mute=True):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1 if mute else 0, None)

# Function to capture system audio and analyze it
def check_audio():
    duration = 3  # Analyze every 3 seconds
    sample_rate = 22050
    channels = 1

    print("Listening for Azan... (Press 'Q' to Quit)")
    
    while True:
        if keyboard.is_pressed("q"):  # Check if 'Q' is pressed
            print("\nExiting Program...")
            break

        print("Listening...")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
        sd.wait()
        
        # Extract features
        mfcc_audio = librosa.feature.mfcc(y=recording[:, 0], sr=sample_rate, n_mfcc=13)
        audio_features = np.mean(mfcc_audio, axis=1)

        # Compare with Azan features
        distance = np.linalg.norm(audio_features - azan_features)
        print(f"Audio match score: {distance}")

        if distance < 20:  # Threshold for similarity
            print("Azan detected! Muting audio...")
            mute_sound(True)
            time.sleep(120)  # Wait for 2 minutes (Azan duration)
            print("Unmuting audio...")
            mute_sound(False)

        time.sleep(3)  # Check every 3 seconds

# Start the detection process
if __name__ == "__main__":
    check_audio()
