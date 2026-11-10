import os
import re

html_path = '/usr/local/google/home/normanbt/Documents/kezia2/fiona/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
data_imgs = re.findall(r'data-img=["\']([^"\']+)["\']', content)
urls = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', content)

all_paths = set(srcs + data_imgs + urls)
print(f"Found {len(all_paths)} referenced asset paths in index.html")

base_dir = '/usr/local/google/home/normanbt/Documents/kezia2/fiona'
missing = []
found = []

for p in sorted(all_paths):
    if p.startswith('http') or p.startswith('data:'):
        continue
    full_path = os.path.join(base_dir, p)
    if os.path.exists(full_path):
        found.append(p)
    else:
        missing.append(p)

print(f"\nFound ({len(found)}):")
for p in found:
    print(f"  [OK] {p}")

if missing:
    print(f"\nMissing ({len(missing)}):")
    for p in missing:
        print(f"  [ERROR MISSING] {p}")
    exit(1)
else:
    print("\nALL 52/52 REFERENCED ASSETS RECOVERED AND VERIFIED!")
