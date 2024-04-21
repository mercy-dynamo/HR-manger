import speech_recognition as sr
import pyaudio
from gtts import gTTS
import pygame
from io import BytesIO

def text_to_speech(text, language='en'):
    """Converts text to speech and plays it using Pygame."""
    tts = gTTS(text=text, lang=language)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def speech_to_text(prompt):
    """Captures speech input from the user, handling silence and recognition errors."""
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print(prompt)
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()  # Convert to lowercase for case-insensitive matching
        except sr.UnknownValueError:
            print("Sorry, could not understand audio. Please speak again.")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

text1a = "Hello, how are you?"
text_to_speech(text1a)
print("HR:", text1a)

text1b = speech_to_text("What would you like to tell me?")

text2a = "I am HR Manager, I am going to ask you some questions"
text_to_speech(text2a)
print("HR:", text2a)
text3a="Tell me about yourself"
text_to_speech(text3a)
print("HR:", text3a)

text3b=speech_to_text("Answer?")

text4a="What was your percentage in last semester?"
text_to_speech(text4a)
print("HR:", text4a)

text4b=speech_to_text("Answer?")

text5a="What's the projects that you have done?"
text_to_speech(text5a)
print("HR:", text5a)

text5b=speech_to_text("Answer?")

text6a="Why should we hire you?"
text_to_speech(text6a)
print("HR:", text6a)

text6b=speech_to_text("Answer?")

text7a="Do you have any Experience - Internship done for the same role?"
text_to_speech(text7a)
print("HR:", text7a)

text7b=speech_to_text("Answers?")

# ... continue your code with text1b and text2b