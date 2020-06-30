from aip import AipSpeech

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

app_id = '20666429'
api_key = 'x6zoV2apTweQNGUjGE4dIrmC'
sercret_key = 'NZkU9ZTKpTuAkxmv8MTMCKz8hcOtEE4F'

client = AipSpeech(app_id, api_key, sercret_key)
# 识别本地文件
result = client.asr(get_file_content('7772.pcm'), 'pcm', 16000, {'dev_pid': 1537, })
print(result['err_no'])
print(result['result'])

# from pydub import AudioSegment
# import wave
#
#
# sound = AudioSegment.from_file("D:/PyCode/analysis/608.mp3", format='MP3')
# f = wave.open("777.wav", 'wb')
# f.setnchannels(1)  # 频道数，
# f.setsampwidth(2)  # 量化位数，1为8位，2为16位
# f.setframerate(8000)  # 采样频率，
# f.setnframes(len(sound.raw_data)//2)  # 采样点数，波形数据长度
# f.writeframes(sound.raw_data)  # 写入波形数据
# f.close()