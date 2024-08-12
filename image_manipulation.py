from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        # Memuat gambar
        image = Image.open(input_path)
        print("✅ Gambar berhasil dimuat")

        # Tentukan ukuran cropping
        crop_width = min(image.width, 200)
        crop_height = min(image.height, 200)

        # Lakukan cropping
        cropped_image = image.crop((10, 10, crop_width, crop_height))
        print(f"✅ Cropping berhasil dengan ukuran: {crop_width}x{crop_height}")

        # Operasi Resizing
        resized_image = cropped_image.resize((100, 100), Image.Resampling.LANCZOS)
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(1.5)
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered_image, bright_image, alpha=0.5)
        print("✅ Penggabungan gambar berhasil")

        # Menyimpan semua hasil manipulasi gambar
        cropped_image.save('cropped_' + output_path)
        resized_image.save('resized_' + output_path)
        filtered_image.save('filtered_' + output_path)
        bright_image.save('bright_' + output_path)
        combined_image.save('combined_' + output_path)
        

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_image('gunungg.jpeg', 'result.jpg')
