import console
import sys
import glob
import os
from youtube_dl import YoutubeDL


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def postdownload(d):
    if d["status"] == "finished":
        print("Done downloading  ...")
        console.quicklook(d["filename"])
        os.remove(d["filename"])
        appex.finish()
        return


outdir = os.path.expanduser("~/Documents/Downloads")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass

if len(sys.argv) != 2:
    raise IndexError("usage: %s url" % sys.argv[0])
url = sys.argv[1]
print(f"url: {url}")

# choice = ("Video", "best[ext=mp4]", "mp4")

# _, format, ext = choice
# print("format: %s" % (format))

opts = {
    "outtmpl": os.path.join(outdir, "%(title)s.%(ext)s"),
    "format": "bestaudio/best",
    "nocheckcertificate": True,
    "logger": MyLogger()
    # "output": "%(title)s.%(ext)s"
}

with YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=True)
    filepath = ydl.prepare_filename(info)

print(f"Downloaded: {filepath}")

try:
    console.open_in(filepath)
finally:
    os.remove(filepath)
    print(f"Deleted: {filepath}")
