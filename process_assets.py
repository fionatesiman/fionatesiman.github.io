import os
from PIL import Image

mask_pairs = [
    (0, 1),
    (9, 10),
    (12, 13),
    (14, 15),
    (17, 18),
    (24, 25),
    (29, 30),
    (32, 33),
    (40, 41),
    (42, 43),
    (49, 50),
    (51, 52),
    (57, 58),
    (61, 62),
    (66, 67),
]

os.makedirs('processed_assets', exist_ok=True)

# Combine masked images into RGBA
for img_idx, mask_idx in mask_pairs:
    img_path = f'extracted_raw/img-{img_idx:03d}.png'
    mask_path = f'extracted_raw/img-{mask_idx:03d}.png'
    rgb_img = Image.open(img_path).convert('RGB')
    mask_img = Image.open(mask_path).convert('L')
    if rgb_img.size != mask_img.size:
        mask_img = mask_img.resize(rgb_img.size, Image.Resampling.LANCZOS)
    rgb_img.putalpha(mask_img)
    out_path = f'processed_assets/img-{img_idx:03d}_rgba.png'
    rgb_img.save(out_path)
    print(f"Saved RGBA: {out_path} {rgb_img.size}")

# Also copy unmasked standalone images
mask_set = set()
for img_idx, mask_idx in mask_pairs:
    mask_set.add(img_idx)
    mask_set.add(mask_idx)

for i in range(68):
    if i not in mask_set:
        src = f'extracted_raw/img-{i:03d}.png'
        dst = f'processed_assets/img-{i:03d}.png'
        if os.path.exists(src):
            img = Image.open(src)
            img.save(dst)
            print(f"Copied standalone: {dst} {img.size} {img.mode}")
