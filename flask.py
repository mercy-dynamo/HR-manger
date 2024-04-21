from flask import Flask, request, jsonify
from tryhack.py import text_to_speech, speech_to_text
import pygame
app = Flask(_name_)

@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.json
    user_input = data['message']
    
    # Process user input
    # Example: Implement your speech_to_text function here
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
    response = speech_to_text(user_input)

    
    # Example: Implement your text_to_speech function here
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
    text_to_speech(response)
    
    return jsonify({'response': response})

if _name_ == 'main':
    app.run(debug=True)