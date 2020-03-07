import console
import sys
import glob
import os
from youtube_dl import YoutubeDL

if len(sys.argv) != 2:
	raise IndexError('usage: %s url' % (sys.argv[0]))
url = sys.argv[1]
print('url: %s' % (url))

choice = ('Video', 'best[ext=mp4]', 'mp4')

_, format, ext = choice
print('format: %s' % (format))

opts = {
	'format': format
	'output': '%(title)s.%(ext)s'
}
with YoutubeDL(opts) as ydl:
	ydl.download([url])

file = max(glob.glob('*.'+ext), key=os.path.getctime)
if not file:
	raise IndexError('downloaded file not found')
print('downloaded: %s' % (file))

try:
	console.open_in(file)	
finally:
	os.remove(file)
	print('deleted: %s' % (file))
