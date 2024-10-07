import pyttsx3

# เริ่มต้นการใช้งาน pyttsx3
engine = pyttsx3.init()

# เลือกเสียงภาษาไทย
voices = engine.getProperty('voices')
for voice in voices:
    if 'thai' in voice.name.lower() or 'th' in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

# พูดทดสอบเป็นภาษาไทย
engine.say("สวัสดีครับ ยินดีที่ได้รู้จัก")
engine.runAndWait()
