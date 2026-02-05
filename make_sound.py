import wave
import struct
import math
import os

# Ensure sounds folder exists
os.makedirs("sounds", exist_ok=True)

# Sound parameters
sample_rate = 44100     
duration = 0.12         
frequency = 800        
volume = 0.6           

filename = "sounds/sounds.wav"

with wave.open(filename, "w") as wav:
    wav.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

    for i in range(int(sample_rate * duration)):
        sample = volume * math.sin(2 * math.pi * frequency * i / sample_rate)
        wav.writeframes(struct.pack("<h", int(sample * 32767)))

print("✅ Shooting sound created at:", filename)