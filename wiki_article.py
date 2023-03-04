# Imports
import speech_recognition as sr
import numpy as np
import pyaudio

def inference(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    
    return response

#create recognizer
r = sr.Recognizer()

#create mic
mic = sr.Microphone()

#inference using the function we built
words = inference(r, mic)

#produce word cloud
print(words["transcription"])
