#This is a Text to Speech and Speech to Text Engine

#Developer: Hassan Ali

#Roll no at FCIT: BCSF19A540

#Mail: hassanali202456@gmail.com

#Web: hassanonline.netlify.app





from gtts import gTTS

import speech_recognition as sr

from playsound import playsound

language = "en"



print("""Choose 1 for Text to Speech

                OR

Choose 2 for Speech to Text""")



engine_choice = int(input("Enter your Choice: "))







#Text to Speech Engine

def text_to_speech():

    print("""Choose 1 for entering text

                OR

choose 2 to read from a TXT file""")



    input_choice = int(input("Enter your Choice: "))



    if(input_choice == 1):

        user_text = input("Your Text: ")

        output = gTTS(text = user_text, lang = language, slow = False)

        output.save("output.mp3")

        playsound("output.mp3")



    if(input_choice == 2):

        file_name = input("File name is: ")

        file_handle = open(file_name, "r") #r is for read permissions

        file_text = file_handle.read().replace("\n", " ")

        file_handle.close()

        output = gTTS(text = file_text, lang = language, slow = False)

        output.save("audio_output.mp3")

        playsound("audio_output.mp3")





def speech_to_text():

    speech = sr.Recognizer()

    with sr.Microphone() as source:

        speech.adjust_for_ambient_noise(source)

        print("Say Something")

        audio = speech.listen(source)

    try:

        output_file = open("text_output.txt", "w+")

        output_text = speech.recognize_google(audio)

        output_file.write(output_text)

        print("You said: " + speech.recognize_google(audio))

    except:

        print("Can't Understand")





#main function

if(engine_choice == 1):

    text_to_speech()

if(engine_choice == 2):

    speech_to_text()



