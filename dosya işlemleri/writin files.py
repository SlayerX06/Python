
#text = "Merhaba bu bir dosya yazma testidir.\nYeni bir satır ekliyoruz."

#text = "Eğer bir aynı isimde dosya varsa, bu dosyanın içeriği silinir ve yeni içerik yazılır."

text = "Bu son yazı. Hoşçakal"

with open("example.txt", "a") as file:
    file.write(text)  #dosyaya metni yazar
    # open kodunda komutu a olarak değiştirirsek bu yazıyı dosyaya ekler