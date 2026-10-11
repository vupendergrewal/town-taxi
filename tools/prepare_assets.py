from PIL import Image
import os

src = r"C:\Users\grewa\.cursor\projects\c-Users-grewa-Downloads-town-taxi\assets\c__Users_grewa_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images_image-9cfa2594-1f18-4f93-ab23-444cc7b545e1.png"
out_dir = r"C:\Users\grewa\Downloads\town-taxi\assets"
im = Image.open(src).convert("RGBA")
px = im.load()
w, h = im.size

def is_field(r, g, b):
    peak = max(r, g, b)
    return peak > 170 and b < 150 and r > 150 and g > 90

# Only the yellow connected to the canvas edge is background.
# The taxi checker uses the same yellow, but it sits inside the car.
seen = bytearray(w * h)
stack = []
for x in range(w):
    stack.append((x, 0))
    stack.append((x, h - 1))
for y in range(h):
    stack.append((0, y))
    stack.append((w - 1, y))
while stack:
    x, y = stack.pop()
    i = y * w + x
    if seen[i]:
        continue
    seen[i] = 1
    r, g, b, a = px[x, y]
    if not is_field(r, g, b):
        continue
    px[x, y] = (0, 0, 0, 0)
    if x > 0:
        stack.append((x - 1, y))
    if x + 1 < w:
        stack.append((x + 1, y))
    if y > 0:
        stack.append((x, y - 1))
    if y + 1 < h:
        stack.append((x, y + 1))

for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        if a == 0:
            continue
        peak = max(r, g, b)
        if peak < 80:
            px[x, y] = (12, 12, 12, 255)
        elif is_field(r, g, b):
            px[x, y] = (0, 0, 0, 0)
        else:
            # fringe between ink and the removed field
            alpha = int(max(0, min(255, 255 - peak)))
            px[x, y] = (12, 12, 12, alpha if alpha > 20 else 0)

alpha = im.split()[-1]
full = im.crop(alpha.getbbox())
full.save(os.path.join(out_dir, "logo-full.png"))

pixels = full.load()
fw, fh = full.size
rows = [any(pixels[x, y][3] > 30 for x in range(fw)) for y in range(fh)]
gaps = []
in_gap = False
start = 0
for y, has in enumerate(rows):
    if not has and not in_gap:
        in_gap = True
        start = y
    elif has and in_gap:
        in_gap = False
        gaps.append((start, y, y - start))
candidates = [g for g in gaps if g[0] > fh * 0.35 and g[2] > 8]
split = candidates[0][0] if candidates else int(fh * 0.72)
mark = full.crop((0, 0, fw, split))
mark = mark.crop(mark.split()[-1].getbbox())
mark.save(os.path.join(out_dir, "logo-mark.png"))

tile = Image.new("RGBA", (512, 512), (253, 208, 1, 255))
m = mark.copy()
m.thumbnail((380, 300))
tile.paste(m, ((512 - m.size[0]) // 2, (512 - m.size[1]) // 2), m)
tile.save(os.path.join(out_dir, "logo-tile.png"))
preview = Image.new("RGBA", (full.size[0] + 80, full.size[1] + 80), (232, 226, 214, 255))
preview.paste(full, (40, 40), full)
preview.convert("RGB").save(os.path.join(out_dir, "logo-preview.jpg"), quality=90)
print("full", full.size, "mark", mark.size, "split", split)
