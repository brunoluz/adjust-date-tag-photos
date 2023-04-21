from PIL import Image
from PIL.ExifTags import TAGS

file_path = 'foto.jpeg'

results = {}
i = Image.open(file_path)
info = i._getexif()
for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    results[decoded] = value

print(info.items()['DateTime'])

print(results)