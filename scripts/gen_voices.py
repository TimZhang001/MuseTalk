from pydub import AudioSegment

# 创建一个静音的音频，设置为10秒钟
duration_ms = 5000  # 10秒钟
silence = AudioSegment.silent(duration=duration_ms)

# 保存为 WAV 文件
silence.export("silence.wav", format="wav")
