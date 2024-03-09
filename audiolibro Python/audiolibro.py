from gtts import gTTS

file = open('ana.txt', 'r', encoding='utf-8')
textBook = file.read()
file.close()

audio = gTTS(text=textBook, lang='es')

audio.save('audio-Ana.mp3')
