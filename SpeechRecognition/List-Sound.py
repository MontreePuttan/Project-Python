import pyttsx3

# เริ่มต้นการใช้งาน pyttsx3
engine = pyttsx3.init()

# แสดงรายชื่อเสียงทั้งหมดในระบบ
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id}) - Language: {voice.languages}")

# คุณสามารถเลือกเสียงที่รองรับภาษาไทย (ตรวจสอบจากผลลัพธ์)
