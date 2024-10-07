import speech_recognition as speech
import pyttsx3

# ตั้งค่าตัวแปลงข้อความเป็นเสียง
engine = pyttsx3.init()

# ตั้งค่าความเร็วการพูด (rate of speech) เป็น 160 WPM
engine.setProperty('rate', 160)

# ปรับเสียงพูด (หญิง):
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # เลือกเสียงผู้หญิง

# เริ่มต้นการทำงานของตัวแปลงข้อความเป็นเสียง
data = speech.Recognizer()
print("==เริ่มการทำงาน==")

with speech.Microphone() as source:
    # ปรับการฟังให้เงียบก่อนเพื่อหลีกเลี่ยงเสียงรบกวน
    data.adjust_for_ambient_noise(source)
    
    while True:
        print("==กำลังฟัง==")
        audio = data.listen(source)
        
        try:
            # แปลงเสียงที่ได้ยินเป็นข้อความ โดยระบุให้ใช้ภาษาไทย
            text = data.recognize_google(audio, language='th')
            print("คุณพูดว่า: " + text)
            
            # นำข้อความที่ได้มาย้อนกลับออกไปเป็นเสียงพูด
            engine.say(text)
            engine.runAndWait()
        
        except speech.UnknownValueError:
            # หากไม่สามารถแปลงเสียงเป็นข้อความได้ (ไม่เข้าใจเสียง)
            print("เราไม่เข้าใจคุณ")
            engine.say("เราไม่เข้าใจคุณ")
            engine.runAndWait()
        
        except speech.RequestError as e:
            # หากมีข้อผิดพลาดในการร้องขอ (เช่น ไม่สามารถเชื่อมต่อกับ Google API)
            print(f"ไม่สามารถร้องขอได้: {e}")
            engine.say("ไม่สามารถเชื่อมต่อกับระบบได้")
            engine.runAndWait()

        except Exception as e:
            # จับข้อผิดพลาดทั่วไปอื่นๆ
            print(f"เกิดข้อผิดพลาด: {e}")
            engine.say("เกิดข้อผิดพลาด")
            engine.runAndWait()
