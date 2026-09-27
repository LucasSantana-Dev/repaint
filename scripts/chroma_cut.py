"""Cut the magenta background (#FF00FF) out of a generated sprite and crop to content.

usage: python3 chroma_cut.py <input.png> [...]   -> writes <input>-cutout.png

A pixel turns transparent when it is "magenta enough": high red and blue, low green. The
tolerance is tuned for the slightly dirty fringe an image model tends to leave around the
sprite's edge.
"""
import sys

from PIL import Image


def cut(path):
    im = Image.open(path).convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = px[x, y]
            if r > 170 and b > 170 and g < 110 and abs(r - b) < 70:
                px[x, y] = (0, 0, 0, 0)
            # fringe: magenta blended into the dark outline (R and B well above G, not light purple)
            elif r - g > 55 and b - g > 55 and abs(r - b) < 60 and g < 90:
                px[x, y] = (0, 0, 0, 0)
    box = im.getbbox()
    if box:
        im = im.crop(box)
    dest = path.replace(".png", "-cutout.png")
    im.save(dest)
    return dest, im.size


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 chroma_cut.py <input.png> [...]")
    for p in sys.argv[1:]:
        print(*cut(p))
