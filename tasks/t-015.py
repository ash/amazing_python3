import math, wave, struct
rate = 44100
freq = 440
duration = 2
with wave.open('audio.wav','wb') as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(rate)
    o = 2 * math.pi * freq / rate
    for t in range(rate * duration):
        f = 32767 * math.sin(o * t)
        data = struct.pack('<h', int(f))
        wav.writeframesraw(data)
