from PIL import Image

im = Image.open('processed_assets/doodle_stick_hang.png')
datas = im.getdata()
newData = []
for item in datas:
    # If reddish:
    if item[0] > 150 and item[1] < 100 and item[2] < 100:
        newData.append(item)
    else:
        newData.append((255, 255, 255, 0))
im.putdata(newData)
bbox = im.getbbox()
if bbox:
    im = im.crop(bbox)
im.save('processed_assets/doodle_stick_hang_clean.png')
print("Saved doodle_stick_hang_clean.png", im.size)
