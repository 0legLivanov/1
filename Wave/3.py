import wave
import struct

a = int(input())
source = wave.open("in.wav", mode="rb")
dest = wave.open("3.wav", mode="wb")
dest.setparams(source.getparams())

frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))

newdata = []
for i in range(0, len(data)):
    newdata.append(data[i] + a)

newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()
