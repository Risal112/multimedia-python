from PIL import Image, ImageFilter

# Load the image
image = Image.open('gunungg.jpeg')

# Crop the image (example coordinates)
cropped_image = image.crop((10, 10, 200, 200))

# Resize the cropped image
resized_image = cropped_image.resize((100, 100))

# Apply a blur filter
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Save the filtered image
filtered_image.save('filtered_gunungg.jpeg')

from pydub import AudioSegment;

# Load the audio file
audio = AudioSegment.from_file('mss.mp3')

# Clip the first 10 seconds
clipped_audio = audio[:10000]

# Increase the volume by 10dB
louder_audio = clipped_audio + 10

# Save the modified audio
louder_audio.export('modified_mss.mp3', format='mp3')
