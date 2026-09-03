import os
import shutil
from PIL import Image

assets_dir = '/usr/local/google/home/normanbt/Documents/kezia2/fiona/assets'
os.makedirs(assets_dir, exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'skills'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'characters'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'zine'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'concept_art'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'illustrations'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'promotional'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'photography'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'animation'), exist_ok=True)
os.makedirs(os.path.join(assets_dir, 'doodles'), exist_ok=True)

# 1. Signature crop
sig = Image.open('processed_assets/img-000_rgba.png')
# signature is around bottom right:
bbox = sig.getbbox()
if bbox:
    sig_crop = sig.crop(bbox)
    sig_crop.save(os.path.join(assets_dir, 'signature.png'))
    print("Saved signature.png", sig_crop.size)

# 2. Hero background
shutil.copy('processed_assets/img-002.png', os.path.join(assets_dir, 'hero_bg.png'))

# 3. Profile photo
shutil.copy('processed_assets/img-005.png', os.path.join(assets_dir, 'profile_photo.png'))

# 4. Characters
shutil.copy('processed_assets/img-003.png', os.path.join(assets_dir, 'characters', 'duality_battle.png'))
shutil.copy('processed_assets/img-006.png', os.path.join(assets_dir, 'characters', 'cyberpunk_squad.png'))
shutil.copy('processed_assets/img-016.png', os.path.join(assets_dir, 'characters', 'nobleman_rose.png'))

# Green-haired character (crop tight)
green = Image.open('processed_assets/img-017_rgba.png')
gbox = green.getbbox()
if gbox:
    green.crop(gbox).save(os.path.join(assets_dir, 'characters', 'green_commander.png'))

# Butterfly fairy (crop tight)
fairy = Image.open('processed_assets/img-040_rgba.png')
fbox = fairy.getbbox()
if fbox:
    fairy.crop(fbox).save(os.path.join(assets_dir, 'characters', 'butterfly_fairy.png'))

# Reyna peeking (crop tight)
reyna_peek = Image.open('processed_assets/img-032_rgba.png')
rpbox = reyna_peek.getbbox()
if rpbox:
    reyna_peek.crop(rpbox).save(os.path.join(assets_dir, 'characters', 'reyna_peeking.png'))

# Reyna standing
reyna_stand = Image.open('processed_assets/img-024_rgba.png')
rsbox = reyna_stand.getbbox()
if rsbox:
    reyna_stand.crop(rsbox).save(os.path.join(assets_dir, 'characters', 'reyna_standing.png'))

# Byron hooded standing
byron_stand = Image.open('processed_assets/img-029_rgba.png')
bsbox = byron_stand.getbbox()
if bsbox:
    byron_stand.crop(bsbox).save(os.path.join(assets_dir, 'characters', 'byron_standing.png'))

# Photographer girl
photog = Image.open('processed_assets/img-061_rgba.png')
pbox = photog.getbbox()
if pbox:
    photog.crop(pbox).save(os.path.join(assets_dir, 'characters', 'photographer_girl.png'))

# Marionette puppet
puppet = Image.open('processed_assets/img-066_rgba.png')
pubox = puppet.getbbox()
if pubox:
    puppet.crop(pubox).save(os.path.join(assets_dir, 'characters', 'marionette_puppet.png'))

# 5. Skills
shutil.copy('processed_assets/img-007.png', os.path.join(assets_dir, 'skills', 'illustrator.png'))
shutil.copy('processed_assets/img-008.png', os.path.join(assets_dir, 'skills', 'photoshop.png'))
shutil.copy('processed_assets/img-009_rgba.png', os.path.join(assets_dir, 'skills', 'indesign.png'))
shutil.copy('processed_assets/img-011.png', os.path.join(assets_dir, 'skills', 'zappar.png'))
shutil.copy('processed_assets/img-012_rgba.png', os.path.join(assets_dir, 'skills', 'figma.png'))
shutil.copy('processed_assets/img-014_rgba.png', os.path.join(assets_dir, 'skills', 'canva.png'))
shutil.copy('processed_assets/skill_live2d.png', os.path.join(assets_dir, 'skills', 'live2d.png'))

# 6. Zine
shutil.copy('processed_assets/img-019.png', os.path.join(assets_dir, 'zine', 'zine_cover.png'))
shutil.copy('processed_assets/img-020.png', os.path.join(assets_dir, 'zine', 'meet_characters.png'))
shutil.copy('processed_assets/img-021.png', os.path.join(assets_dir, 'zine', 'comic_panel1.png'))
shutil.copy('processed_assets/img-022.png', os.path.join(assets_dir, 'zine', 'comic_panel2.png'))
shutil.copy('processed_assets/img-023.png', os.path.join(assets_dir, 'zine', 'what_is_pixel_art.png'))
shutil.copy('processed_assets/img-026.png', os.path.join(assets_dir, 'zine', 'comic_panel3.png'))
shutil.copy('processed_assets/img-027.png', os.path.join(assets_dir, 'zine', 'origins_of_icons.png'))
shutil.copy('processed_assets/img-028.png', os.path.join(assets_dir, 'zine', 'try_it_yourself.png'))
shutil.copy('processed_assets/img-031.png', os.path.join(assets_dir, 'zine', 'pixel_art_guide.png'))

# 7. Concept Art
shutil.copy('processed_assets/img-034.png', os.path.join(assets_dir, 'concept_art', 'game_concept_sketch.png'))
shutil.copy('processed_assets/img-035.png', os.path.join(assets_dir, 'concept_art', 'reyna_concept.png'))
shutil.copy('processed_assets/img-036.png', os.path.join(assets_dir, 'concept_art', 'byron_concept.png'))
shutil.copy('processed_assets/img-037.png', os.path.join(assets_dir, 'concept_art', 'zine_layout_iterations.png'))
shutil.copy('processed_assets/img-038.png', os.path.join(assets_dir, 'concept_art', 'pixels_logo_green.png'))
shutil.copy('processed_assets/img-039.png', os.path.join(assets_dir, 'concept_art', 'pixels_logo_skyline.png'))

# 8. Illustrations
starry = Image.open('processed_assets/img-042_rgba.png')
sbox = starry.getbbox()
if sbox:
    starry.crop(sbox).save(os.path.join(assets_dir, 'illustrations', 'starry_hair_cosmic.png'))
shutil.copy('processed_assets/img-044.png', os.path.join(assets_dir, 'illustrations', 'crimson_flower_noble.png'))
shutil.copy('processed_assets/img-045.png', os.path.join(assets_dir, 'illustrations', 'red_thread_shrine_maiden.png'))
shutil.copy('processed_assets/img-046.png', os.path.join(assets_dir, 'illustrations', 'lightning_arcane_trio.png'))
shutil.copy('processed_assets/img-047.png', os.path.join(assets_dir, 'illustrations', 'fire_water_duality.png'))

# 9. Promotional
# Kitsune pointing girl
kitsune = Image.open('processed_assets/img-048.png').convert("RGBA")
kdatas = kitsune.getdata()
knew = []
for p in kdatas:
    if p[0] > 240 and p[1] > 240 and p[2] > 240:
        knew.append((255, 255, 255, 0))
    else:
        knew.append(p)
kitsune.putdata(knew)
kbox = kitsune.getbbox()
if kbox:
    kitsune.crop(kbox).save(os.path.join(assets_dir, 'promotional', 'kitsune_pointing.png'))

shutil.copy('processed_assets/img-051_rgba.png', os.path.join(assets_dir, 'promotional', 'interbat_dental_booth.png'))
shutil.copy('processed_assets/img-053.png', os.path.join(assets_dir, 'promotional', 'delisaos_shelf_talker.png'))
shutil.copy('processed_assets/img-054.png', os.path.join(assets_dir, 'promotional', 'region_badges_app.png'))
shutil.copy('processed_assets/img-055.png', os.path.join(assets_dir, 'promotional', 'pocky_splash_banner.png'))
shutil.copy('processed_assets/img-056.png', os.path.join(assets_dir, 'promotional', 'youtube_video_overlay.png'))
shutil.copy('processed_assets/img-057_rgba.png', os.path.join(assets_dir, 'promotional', 'silverqueen_chocolate.png'))

# 10. Photography
shutil.copy('processed_assets/img-059.png', os.path.join(assets_dir, 'photography', 'batik_floral_portrait.png'))
shutil.copy('processed_assets/img-060.png', os.path.join(assets_dir, 'photography', 'red_suit_dramatic_studio.png'))

# 11. Animation
shutil.copy('processed_assets/img-065.png', os.path.join(assets_dir, 'animation', 'panda_brushing_tooth.png'))
shutil.copy('processed_assets/img-063.png', os.path.join(assets_dir, 'animation', 'panda_sleeping.png'))
shutil.copy('processed_assets/img-064.png', os.path.join(assets_dir, 'animation', 'panda_sitting.png'))

# 12. Doodles
shutil.copy('processed_assets/doodle_stick_climb.png', os.path.join(assets_dir, 'doodles', 'stick_climb.png'))
shutil.copy('processed_assets/doodle_stick_hang_clean.png', os.path.join(assets_dir, 'doodles', 'stick_hang.png'))

print("All assets successfully organized in assets/ directory!")
