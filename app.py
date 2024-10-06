#----------Para ejecutar desde consola: streamlit run /ruta/al/directorio/app.py

import streamlit as st
import yt_dlp

# Función para descargar el video
def descargar_video_youtube(url):
    try:
        opciones = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            return True
    except Exception as e:
        return str(e)

# Configuración de la aplicación
st.title("Descargador de Videos de YouTube")
st.write("Introduce la URL del video de YouTube que deseas descargar:")

# Campo de entrada para la URL
url = st.text_input("URL del video:")

# Botón para descargar
if st.button("Descargar"):
    if url:
        resultado = descargar_video_youtube(url)
        if resultado is True:
            st.success("Descarga completada.")
        else:
            st.error(f"Error: {resultado}")
    else:
        st.warning("Por favor, introduce una URL válida.")
