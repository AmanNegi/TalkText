import speech_recognition as sr
from datetime import datetime

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

while (True):
    ready = input("Do you want to speak? y/n\n> ")
    if (ready == 'n'):
        exit()
    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Start Speaking...")
        audio_text = r.listen(source)
        print("Great! We're done...")

    try:
        data = r.recognize_google(audio_text)
        res = input("Do you want to store this text? y/n\n>")
        if (res == 'y'):
            print("Saving Data to file")
            with open('output.txt', 'a') as file:
                file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": ")
                file.write("\n")
                file.write(data)
                file.write("\n\n")
    except:
        print("Didn't get what you said. Try again.")
