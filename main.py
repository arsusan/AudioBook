import pyttsx3
import PyPDF2

number = int(input("Enter the page number to star reading from: "))

# Initialize the speaker
# speed = int(input("Enter speed rate of the audio (normal rate is 225): "))
# speaker = pyttsx3.init()
# rate = speaker.getProperty('rate')   
# print(speed)
# speaker.setProperty('rate', speed)
# 
speaker = pyttsx3.init()
# voice
audio_voice = input("Enter the voice type (male or female): ")
voices = speaker.getProperty('voices')
print(voices)
count = 0
while (count < 1):   
    if (audio_voice == 'male'):
        #changing index, changes voices, 0 for male
        speaker.setProperty('voice', voices[1].id)
        count = count + 1
    elif(audio_voice == 'female'):
        speaker.setProperty('voice', voices[0].id)
        count = count + 1
    else:
        print("Please choose a valid voice.")
    
# 

print("Audio is starting...............")
book = open('Coding All-in-One For Dummies ( PDFDrive ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(number-1, pages):
    program = input("Enter (C) to continue and (S) to Stop the program: ")
    if (program == 'C'):
        print(f"Page Number {num + 1} is playing....................")
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
    elif(program == 'S'):
        break

speaker.stop() 
print("\tProgram closed. \n\t HAVE A NICE DAY")




# # volume
# volume = engine.getProperty('volume')
# print(volume)
# engine.setProperty('volume',1.0)

# # saving audio file
# engine.save_to_file(text, 'audio.mp3')
# engine.runAndWait()