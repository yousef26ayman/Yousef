from gtts import gTTS 
  

import os 
  
mytext = 'hallo my name is yousef ayman'
  

language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  

os.system("start output.mp3") 