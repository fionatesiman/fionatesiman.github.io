import os
from PIL import Image

# 1. Live2D icon: crop tight and make white transparent
p4 = Image.open('page_previews/page-04.png')
w4, h4 = p4.size
# Live2D logo box
live2d = p4.crop((int(w4 * 0.395), int(h4 * 0.548), int(w4 * 0.453), int(h4 * 0.655)))
live2d = live2d.convert("RGBA")
datas = live2d.getdata()
newData = []
for item in datas:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
live2d.putdata(newData)
live2d.save('processed_assets/skill_live2d.png')
print("Saved skill_live2d.png", live2d.size)

# 2. Page 19 stick figure (climbing/hanging)
p19 = Image.open('page_previews/page-19.png')
w19, h19 = p19.size
stick19 = p19.crop((int(w19 * 0.03), int(h19 * 0.52), int(w19 * 0.20), int(h19 * 0.93)))
stick19 = stick19.convert("RGBA")
datas19 = stick19.getdata()
newData19 = []
for item in datas19:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData19.append((255, 255, 255, 0))
    else:
        newData19.append(item)
stick19.putdata(newData19)
stick19.save('processed_assets/doodle_stick_hang.png')
print("Saved doodle_stick_hang.png", stick19.size)

# 3. Page 8 stick figure climbing slope
p8 = Image.open('page_previews/page-08.png')
w8, h8 = p8.size
stick8 = p8.crop((int(w8 * 0.388), int(h8 * 0.025), int(w8 * 0.45), int(h8 * 0.22)))
stick8 = stick8.convert("RGBA")
datas8 = stick8.getdata()
newData8 = []
for item in datas8:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData8.append((255, 255, 255, 0))
    else:
        newData8.append(item)
stick8.putdata(newData8)
stick8.save('processed_assets/doodle_stick_climb.png')
print("Saved doodle_stick_climb.png", stick8.size)
