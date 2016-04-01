import os

os.system('pandoc post.md -s --highlight-style pygments -o post.html')
#os.system('pandoc -t beamer pres.md -o post.pdf')
#os.system('pandoc post.md -s --highlight-style pygments -o post.pdf')
os.startfile('post.html')
