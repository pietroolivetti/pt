import streamlit as st
import subprocess
import edge_tts



st.write("""## TTS PT
        
        """)

txt = st.text_input('Escreva: ')


# if st.button('OR say it outloud'):
#     txt = listen_mic()
#     st.write(txt)

subprocess.run(['edge-tts' ,'--voice', 'pt-BR-AntonioNeural', '--text', txt, '--write-media', 'txt.mp3', '--write-subtitles', 'sub.vtt'])

st.audio('txt.mp3')
