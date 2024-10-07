from googletrans import Translator
translator = Translator()
user_input = input("==กรอกข้อความที่ต้องการ==\n")
translations = translator.translate(user_input, dest='en')
print(translations.origin, ' = ', translations.text)