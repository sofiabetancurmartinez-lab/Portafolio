import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio IA",
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
    st.title("🧠 IA Portfolio")
    st.write(
        "Portafolio de aplicaciones desarrolladas con Inteligencia Artificial. "
        "Explora diferentes herramientas y proyectos interactivos."
    )

    st.divider()
    st.write("🔊 Audio")
    st.write("📄 Texto")
    st.write("👁️ Visión")
    st.write("📊 Datos")
    st.write("🤖 Modelos")

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;'>✨ Portafolio de Inteligencia Artificial ✨</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle' style='text-align:center;'>"
    "Exploración de herramientas de IA aplicadas a audio, texto, visión artificial y análisis de datos."
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
    ("🔊 Text to voice", "txt_to_audio2.png", "Convierte texto en audio usando IA.", "https://trabajo-1-3jxvmzuzkkprjfnoa6crqf.streamlit.app"),
    ("✨ Mi primera app", "OIG5.jpg", "Primer proyecto interactivo con Streamlit.", "https://mi-app-yd6oyue7heujgc554s2gak.streamlit.app"),
    ("🌎 Traductor", "OIG8.jpg", "Traducción automática de texto.", "https://traductorrrr-xp9vrdbef6nrkk998syusv.streamlit.app"),
    ("📄 OCR", "Chat_pdf.png", "Reconocimiento de texto en imágenes.", "https://ghreqvhvwbxasyrnpzta57.streamlit.app"),
    ("🎙️ OCR Audio", "OIG3.jpg", "Procesamiento de audio con IA.", "https://ocr-audio-7qyhk56pmskk8tbjb4tctx.streamlit.app"),
    ("☁️ Word Cloud", "data_analisis.png", "Visualización de palabras clave.", "https://word-cloud-zrjbekvkx2syqbehzt3zm7.streamlit.app"),
    ("💬 Análisis de sentimiento", "OIG4.jpg", "Identifica emociones en texto.", "https://sentimientos-4hzujfgjvl9d3zhcjv3uxh.streamlit.app"),
    ("📊 TF-IDF", "data_analisis.png", "Relevancia de palabras en textos.", "https://tf-idf-ivdf3wmunir46z5nzqqfts.streamlit.app"),
    ("📊 TF-IDF ESP", "data_analisis.png", "Análisis textual en español.", "https://y3ajdf7temeqlf68yhapkw.streamlit.app"),
    ("👁️ YOLO", "txt_to_audio.png", "Detección de objetos en imágenes.", "https://dwscrxjmp4iyae8hkzduaz.streamlit.app"),
    ("🧠 Detección de objetos", "OIG6.jpg", "Reconocimiento visual avanzado.", "https://claseee-9-eqlvhylpcknawfhvbqudyd.streamlit.app"),
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
