import os

os.system('pandoc post.md -s --highlight-style pygments -o post.html')
#os.system('pandoc post.md -s --highlight-style pygments --mathjax -o post.html')
#os.system('pandoc -t beamer pres.md -o ex.pdf')
#os.system('pandoc post.md -s --highlight-style pygments -o ex.pdf')
os.startfile('post.html')
