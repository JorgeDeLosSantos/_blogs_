import os

#os.system('pandoc post.md -s --highlight-style pygments -o post.html')
clo = "pandoc post.md -o post.html --template template.html --css template.css --self-contained"
os.system(clo)
#os.system('pandoc -t beamer pres.md -o ex.pdf')
#os.system('pandoc post.md -s --highlight-style pygments -o ex.pdf')
os.startfile('post.html')
