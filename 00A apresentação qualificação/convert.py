import os

filenames = [f for f in os.listdir('./') if '.md' in f]

md = ''
for filename in filenames:
  print(filename)
  md += open(filename, "r", encoding="utf8").readlines() ## !encoding

