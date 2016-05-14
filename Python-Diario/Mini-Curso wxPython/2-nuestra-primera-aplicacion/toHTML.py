import os

os.system('pandoc post.md -s --highlight-style pygments -o post.html')
os.startfile('post.html')