from googletrans import Translator, LANGUAGES

translator = Translator()

kalimat = 'My Name Is hidayat.'

detection = translator.detect(kalimat)

print("Kalimat ini berasal dari bahasa", LANGUAGES[detection.lang])
print("Dengan kemiripan sebesar", (detection.confidence * 100), "%")
