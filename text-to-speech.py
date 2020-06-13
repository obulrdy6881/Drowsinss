from gtts import gTTS
import os

myspeech = "Hey!, You are feeling asleep. Have a break for 5 minutes"

Lang = 'en'

output = gTTS(text=myspeech, lang=Lang, slow=False)

output.save("alert.mp3")

os.system("start alert.mp3")
