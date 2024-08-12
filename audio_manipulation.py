from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        if len(audio) > 10000:
            clipped_audio = audio[:10000]
            clipped_audio.export('clipped_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        combined_audio = audio + clipped_audio
        combined_audio.export('combined_' + output_path, format='mp3')
        print("✅ Penggabungan berhasil")

        audio.export('result.wav', format='wav')
        print("✅ Konversi format berhasil")

        if audio.dBFS < -10:
            louder_audio = audio + 10
            louder_audio.export('louder_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            raise ValueError("Volume audio sudah terlalu tinggi")

        print("🔊 Memutar audio hasil manipulasi...")
        play(louder_audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('example.mp3', 'result.mp3')
