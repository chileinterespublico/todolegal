import fitz

text=[page.getText() for page in fitz.open('Informe-en-derecho-Jaime-Jara.pdf')]

fw=open('informe.txt','w',encoding='utf-8')
for page in text:
    fw.write(page.replace(chr(13),''))
fw.close()