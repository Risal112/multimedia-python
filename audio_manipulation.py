from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file("mss.mp3")
print("✅ Audio berhasil dimuat")

# Pemotongan audio
start_time = 30 * 1000  # 30 detik
end_time = 60 * 1000    # 60 detik
clipped_audio = audio[start_time:end_time]
clipped_audio.export("clipped_result.mp3", format="mp3")
print("✅ Pemotongan berhasil")

# Penggabungan audio
audio2 = AudioSegment.from_file("mss.mp3")
combined_audio = clipped_audio + audio2
combined_audio.export("combined_result.mp3", format="mp3")
print("✅ Penggabungan berhasil")

# Konversi format
audio.export("result.wav", format="wav")
print("✅ Konversi format berhasil")

# Pengaturan volume
louder_audio = audio + 10  # Menambah volume 10dB
louder_audio.export("louder_result.mp3", format="mp3")
print("✅ Pengaturan volume berhasil")

# Memutar audio hasil manipulasi
from pydub.playback import play
play(louder_audio)
print("🔊 Memutar audio hasil manipulasi...")
