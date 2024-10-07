import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def translate_and_convert_to_mp3(text, dest_language='th'):
    # Translate the text
    translated = translator.translate(text, dest=dest_language)
    print(f"Original: {text}")
    print(f"Translated: {translated.text}")

    # Convert the translated text to speech
    tts = gTTS(text=translated.text, lang=dest_language)
    
    # Save as MP3 file
    mp3_filename = "translated_audio.mp3"
    tts.save(mp3_filename)
    print(f"Saved translated audio as {mp3_filename}")

    # Play the saved MP3 file
    playsound(mp3_filename)

# Main function to recognize Thai speech and translate
def main():
    print("== เริ่มการทำงาน ==")
    with sr.Microphone() as source:
        print("== กำลังฟัง ==")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for the first phrase

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio, language='th-TH')
            print(f"You said: {text}")

            # Translate the recognized text to Thai and convert to MP3
            translate_and_convert_to_mp3(text, dest_language='th')
        
        except sr.UnknownValueError:
            print("เราไม่เข้าใจคุณ")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the program
if __name__ == "__main__":
    main()
