import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print out the available voices
for voice in voices:
    print(f"Voice ID: {voice.id} - Name: {voice.name} - Language: {voice.languages}")

# Clean up the engine
engine.stop()
