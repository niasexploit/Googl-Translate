from googletrans import Translator, LANGUAGES

translator = Translator()
text = input("Masukkan Text : ")
bahasa = input("Terjemahkan ke Bahasa :")  
hasil = translator.translate(text, dest = bahasa)

print("Dari ", LANGUAGES[hasil.src], " : ", text)
print("Ke ", LANGUAGES[hasil.dest], " : ", hasil.text)
print("Pronounsiasi : ", hasil.pronunciation)

