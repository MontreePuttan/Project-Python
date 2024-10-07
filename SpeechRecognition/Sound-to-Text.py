import speech_recognition as speech
data = speech.Recognizer()
print("==เริ่มการทํางาน==")
with speech.Microphone() as source:
    while True:
        print("==กำลังฟัง==")
        audio = data.listen(source)
        try:
            print("คุณพูดว่า : " + data.recognize_google(audio, None,'th'))
        except:
            print("เราไม่เข้าใจคุณ")