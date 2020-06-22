import console
import sys
import glob
import os
from youtube_dl import YoutubeDL


outdir = os.path.expanduser("~/Documents/Downloads")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass

if len(sys.argv) != 2:
    raise IndexError("usage: %s url" % sys.argv[0])
url = sys.argv[1]
print(f"URL: {url}")



opts = {
    "outtmpl": os.path.join(outdir, "%(title)s.%(ext)s"),
    "nocheckcertificate": True,
    "restrictfilenames": True
}

with YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=True)
    filepath = ydl.prepare_filename(info)

print(f"Downloaded: {info['title']}.{info['ext']}")

try:
    console.quicklook(filepath)
    console.open_in(filepath)
finally:
    os.remove(filepath)
    print(f"Deleted: {info['title']}.{info['ext']}")