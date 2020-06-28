from pydub import AudioSegment
import wave

sound = AudioSegment.from_file("D:/PyCode/analysis/608.mp3", format='MP3')
f = wave.open("777.wav", 'wb')
f.setnchannels(1)  # 频道数
f.setsampwidth(2)  # 量化位数
f.setframerate(16000)  # 采样频率
f.setnframes(len(sound.raw_data))  # 采样点数，波形数据长度
f.writeframes(sound.raw_data)  # 写入波形数据
f.close()