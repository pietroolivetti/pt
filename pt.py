import streamlit as st
import subprocess
import edge_tts
from gtts import gTTS



st.write("""## TTS anything
        
        """)

txt = st.text_input('Escreva: ')


# if st.button('OR say it outloud'):
#     txt = listen_mic()
#     st.write(txt)

# subprocess.run(['edge-tts' ,'--voice', 'pt-BR-AntonioNeural', '--text', txt, '--write-media', 'txt.mp3', '--write-subtitles', 'sub.vtt'])

#st.write(generated_answer)



# Texto que você deseja converter em fala
#texto = "Olá, isso é um exemplo de texto para fala usando o Google TTS com Python."

# Cria um objeto gTTS
tts = gTTS(text=txt, lang='pt', tld='com.br')

# Salva o arquivo de áudio
tts.save("txt.mp3")


st.audio('txt.mp3')
