import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio",
    page_icon="✨",
    layout="wide"
)

# ---------- ESTILOS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
    color: white;
}

h1, h2, h3 {
    color: #ffffff;
}

.card {
    background: rgba(255, 255, 255, 0.10);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.15);
}

.card:hover {
    transform: scale(1.02);
    transition: 0.3s;
}

.subtitle {
    font-size: 18px;
    color: #ddd6fe;
}

.stButton button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("Portafolio Interfaces Multimodales")
    st.write(
        "Portafolio de aplicaciones desarrolladas. "
        "Explora diferentes herramientas y proyectos interactivos."
    )

    st.divider()
    st.write("🔊 Audio")
    st.write("📄 Texto")
    st.write("👁️ Visión")
    st.write("📊 Datos")
    st.write("🤖 Modelos")
    st.write("🎨 Dibujo")
    st.write("🌐 IoT")

# ---------- HEADER ----------
st.markdown(
    "<h1 style='text-align:center;'>✨ Portafolio de Sofia Betancur ✨</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle' style='text-align:center;'>"
    "Exploración de herramientas de IA aplicadas a audio, texto, visión artificial, análisis de datos, dibujo interactivo e IoT."
    "</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------- FUNCIÓN TARJETA ----------
def tarjeta(titulo, imagen, descripcion, url):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(titulo)

    try:
        image = Image.open(imagen)
        st.image(image, use_container_width=True)
    except:
        st.warning(f"⚠️ No se encontró la imagen: {imagen}")

    st.write(descripcion)

    st.link_button("Abrir proyecto", url)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PROYECTOS ----------
proyectos = [
    ("🔊 Text to voice", "text_to_voice.png", "Convierte texto en audio usando IA.", "https://trabajo-1-3jxvmzuzkkprjfnoa6crqf.streamlit.app"),
    ("✨ Mi primera app", "mi_app.png", "Primer proyecto interactivo con Streamlit.", "https://mi-app-yd6oyue7heujgc554s2gak.streamlit.app"),
    ("🌎 Traductor", "traductor.png", "Traducción automática de texto.", "https://traductorrrr-xp9vrdbef6nrkk998syusv.streamlit.app"),
    ("📄 OCR", "ocr.png", "Reconocimiento de texto en imágenes.", "https://ghreqvhvwbxasyrnpzta57.streamlit.app"),
    ("🎙️ OCR Audio", "ocr_audio.png", "Procesamiento de audio con IA.", "https://ocr-audio-7qyhk56pmskk8tbjb4tctx.streamlit.app"),
    ("☁️ Word Cloud", "wordcloud.png", "Visualización de palabras clave.", "https://word-cloud-zrjbekvkx2syqbehzt3zm7.streamlit.app"),
    ("💬 Análisis de sentimiento", "sentimiento.png", "Identifica emociones en texto.", "https://sentimientos-4hzujfgjvl9d3zhcjv3uxh.streamlit.app"),
    ("📊 TF-IDF", "tfidf.png", "Relevancia de palabras en textos.", "https://tf-idf-ivdf3wmunir46z5nzqqfts.streamlit.app"),
    ("📊 TF-IDF ESP", "tfidf_esp.png", "Análisis textual en español.", "https://y3ajdf7temeqlf68yhapkw.streamlit.app"),
    ("👁️ YOLO", "yolo.png", "Detección de objetos en imágenes.", "https://dwscrxjmp4iyae8hkzduaz.streamlit.app"),
    ("🧠 Detección de objetos", "deteccion.png", "Reconocimiento visual avanzado.", "https://claseee-9-eqlvhylpcknawfhvbqudyd.streamlit.app"),

    ("📚 Chatea PDF", "chatea_pdf.png", "Permite conversar con un documento PDF usando IA.", "https://chateapdf-zctnkikv5p3uevkbzvdtl4.streamlit.app"),
    ("✍️ Generador de Texto con LSTM", "lstm.png", "Genera texto usando un modelo LSTM de procesamiento de lenguaje.", "https://lstmnlp-pksv6cvjssqd4mjncmthjy.streamlit.app"),
    ("🖼️ Análisis de imagen", "analisis_imagen.png", "Interpreta imágenes y describe su contenido usando visión artificial.", "https://interpretacion-de-imagenes-jtzkqsqdaadvpfxizbo2l9.streamlit.app"),
    ("🔢 Reconocimiento de números", "numeros.png", "Reconoce números escritos a mano mediante IA.", "https://numeros-ghbqg8ktreabntmbyqwmpn.streamlit.app"),
    ("🎨 Tablero para dibujar", "tablero_dibujar.png", "Permite dibujar en un tablero interactivo y procesar el resultado.", "https://handrecognition-mspzlkusvnxukdhevcaxcy.streamlit.app"),
    ("🧩 Tablero inteligente", "tablero_inteligente.png", "Interpreta dibujos realizados en un tablero usando inteligencia artificial.", "https://tablero-inteligente-frjxx47q2w8mdcxg3vkb5y.streamlit.app"),
    ("🎙️ Control Voz", "control_voz.png", "Aplicación de control mediante comandos de voz.", "https://control-voice-jtclbz7tkab7tat7sad7ue.streamlit.app"),
    ("🌐 MQTT Control", "mqtt_control.png", "Permite controlar dispositivos o acciones mediante comunicación MQTT.", "https://mqtt-control-lnepauv4hu8elbvnancrmu.streamlit.app"),
    ("📡 Lector de sensor MQTT", "sensor_mqtt.png", "Lee y muestra datos provenientes de sensores conectados por MQTT.", "https://sensor-mqtt-8tmvwvhazxsftvph3uazzz.streamlit.app"),
]

cols = st.columns(3)

for i, proyecto in enumerate(proyectos):
    titulo, imagen, descripcion, url = proyecto

    with cols[i % 3]:
        tarjeta(titulo, imagen, descripcion, url)

# ---------- FOOTER ----------
st.markdown("""
<br><br>
<div style="text-align:center; color:#ddd6fe;">
    <p>✨ Portafolio académico de IA - Sofía Betancur ✨</p>
</div>
""", unsafe_allow_html=True)
