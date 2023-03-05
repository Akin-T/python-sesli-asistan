import playsound
import speech_recognition as sr
from gtts import gTTS
import random

def konus(yazi):
    tts =gTTS(text=yazi,lang="tr")

    dosya_ismi="ses"+str(random.randint(0,100000000000000000000))+".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)
    
    
def sesi_kaydet():
    r=sr.Recognizer()

    with sr.Microphone () as kaynak:
        ses=r.listen(kaynak)
        soylenen_cumle=""

    try: 
         soylenen_cumle=r.recognize_google(ses,language="Tr-tr")
         print(soylenen_cumle)
    except Exception:
        konus("söyledigin cümleyi anlamadim !")

        return soylenen_cumle
    while True:
        yazi  = sesi_kaydet()
        if "nasilsin" in yazi:
            konus("iyiyim sen nasilsin")

print("akin")

while True:
    sesi_kaydet()

