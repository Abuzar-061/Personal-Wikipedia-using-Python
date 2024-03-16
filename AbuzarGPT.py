import pyttsx3
import wikipedia
voice = pyttsx3.init()
search = input("Message AbuzarGPT : ")
result = wikipedia.summary(search, sentences = 1)
print(result)
voice.say(result)
voice.runAndWait()