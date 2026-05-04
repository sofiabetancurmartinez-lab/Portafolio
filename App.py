import streamlit as st

st.set_page_config(
    page_title="Portafolio",
    page_icon="✨",
    layout="wide"
)

# ---------- ESTILOS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050816 0%, #111827 45%, #312e81 100%);
    color: white;
}

h1, h2, h3 {
    color: #ffffff;
}

.subtitle {
    font-size: 19px;
    color: #c4b5fd;
    text-align: center;
}

.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 26px;
    border-radius: 22px;
    margin-bottom: 24px;
    min-height: 245px;
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0px 8px 28px rgba(0,0,0,0.28);
    backdrop-filter: blur(12px);
    text-align: center;
}

.card:hover {
    transform: translateY(-6px);
    transition: 0.3s;
    border: 1px solid rgba(236,72,153,0.55);
    box-shadow: 0px 12px 35px rgba(236,72,153,0.22);
}

.project-title {
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 14px;
    color: #ffffff;
}

.project-desc {
    font-size: 15px;
    color: #ddd6fe;
    min-height: 72px;
    margin-bottom: 18px;
}

.category {
    display: inline-block;
    padding: 6px 13px;
    border-radius: 999px;
    background: rgba(236,72,153,0.18);
    color: #fbcfe8;
    font-size: 13px;
    margin-bottom: 16px;
    border: 1px solid rgba(236,72,153,0.25);
}

.stButton button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    border-radius: 14px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    width: 100%;
}

.stButton button:hover {
    transform: scale(1.04);
    transition: 0.2s;
}

.header-card {
    background: rgba(255, 255, 255, 0.07);
    padding: 38px;
    border-radius: 28px;
    margin-bottom: 34px;
    border: 1px solid rgba(255,255,255,0.13);
    box-shadow: 0px 10px 35px rgba(0,0,0,0.25);
}

.footer {
    text-align: center;
    color: #c4b5fd;
    margin-top: 45px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("Portfolio")
    st.write(
        "Portafolio académico de aplicaciones desarrolladas en clase, "
        "procesamiento de lenguaje, visión artificial, audio, dibujo interactivo e IoT."
    )

    st.divider()

    st.subheader("Categorías")
    st.write("📄 Texto y documentos")
    st.write("👁️ Visión artificial")
    st.write("🎙️ Audio y voz")
    st.write("🎨 Dibujo interactivo")
    st.write("🌐 IoT y sensores")
    st.write("🤖 Modelos IA")

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <h1 style="text-align:center;">✨ Portafolio de Sofia Betancur ✨</h1>
    <p class="subtitle">
        Exploración de aplicaciones interactivas creadas con Streamlit, IA generativa,
        visión artificial, procesamiento de lenguaje natural, audio e IoT.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- FUNCIÓN TARJETA ----------
def tarjeta(titulo, categoria, descripcion, url):
    st.markdown(
        f"""
        <div class="card">
            <div class="category">{categoria}</div>
            <div class="project-title">{titulo}</div>
            <div class="project-desc">{descripcion}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button("Abrir proyecto", url)

# ---------- PROYECTOS ----------
proyectos = [
    ("Text to Voice", "🎙️ Audio", "Convierte texto escrito en audio usando herramientas de inteligencia artificial.", "https://trabajo-1-3jxvmzuzkkprjfnoa6crqf.streamlit.app"),
    ("Mi primera app", "✨ Streamlit", "Primera aplicación interactiva desarrollada como acercamiento inicial a Streamlit.", "https://mi-app-yd6oyue7heujgc554s2gak.streamlit.app"),
    ("Traductor", "📄 Lenguaje", "Aplicación para traducir texto entre idiomas de forma automática.", "https://traductorrrr-xp9vrdbef6nrkk998syusv.streamlit.app"),
    ("OCR", "👁️ Visión", "Reconoce texto dentro de imágenes mediante técnicas de visión artificial.", "https://ghreqvhvwbxasyrnpzta57.streamlit.app"),
    ("OCR Audio", "🎙️ Audio", "Procesa información desde audio y la transforma en texto o contenido útil.", "https://ocr-audio-7qyhk56pmskk8tbjb4tctx.streamlit.app"),
    ("Word Cloud", "📊 Datos", "Genera nubes de palabras para visualizar términos frecuentes o importantes.", "https://word-cloud-zrjbekvkx2syqbehzt3zm7.streamlit.app"),
    ("Análisis de Sentimiento", "📄 NLP", "Identifica emociones, polaridad o intención dentro de textos.", "https://sentimientos-4hzujfgjvl9d3zhcjv3uxh.streamlit.app"),
    ("TF-IDF", "📊 NLP", "Analiza la relevancia de palabras dentro de un conjunto de textos.", "https://tf-idf-ivdf3wmunir46z5nzqqfts.streamlit.app"),
    ("TF-IDF Español", "📊 NLP", "Versión en español para análisis de relevancia textual mediante TF-IDF.", "https://y3ajdf7temeqlf68yhapkw.streamlit.app"),
    ("YOLO", "👁️ Visión", "Detecta objetos en imágenes usando modelos de visión artificial.", "https://dwscrxjmp4iyae8hkzduaz.streamlit.app"),
    ("Detección de Objetos", "👁️ Visión", "Reconoce objetos presentes en imágenes de forma automática.", "https://claseee-9-eqlvhylpcknawfhvbqudyd.streamlit.app"),

    ("Chatea PDF", "📄 RAG", "Permite conversar con un documento PDF y hacer preguntas sobre su contenido.", "https://chateapdf-zctnkikv5p3uevkbzvdtl4.streamlit.app"),
    ("Generador de Texto con LSTM", "🤖 Modelo IA", "Genera texto usando una red neuronal LSTM aplicada al lenguaje natural.", "https://lstmnlp-pksv6cvjssqd4mjncmthjy.streamlit.app"),
    ("Análisis de Imagen", "👁️ Visión", "Interpreta imágenes y describe su contenido usando inteligencia artificial.", "https://interpretacion-de-imagenes-jtzkqsqdaadvpfxizbo2l9.streamlit.app"),
    ("Reconocimiento de Números", "🤖 Modelo IA", "Reconoce números escritos a mano a partir de una imagen o dibujo.", "https://numeros-ghbqg8ktreabntmbyqwmpn.streamlit.app"),
    ("Tablero para Dibujar", "🎨 Dibujo", "Permite crear dibujos en un tablero interactivo dentro de la aplicación.", "https://handrecognition-mspzlkusvnxukdhevcaxcy.streamlit.app"),
    ("Tablero Inteligente", "🎨 IA Creativa", "Interpreta dibujos realizados en un tablero y describe lo que ocurre en la escena.", "https://tablero-inteligente-frjxx47q2w8mdcxg3vkb5y.streamlit.app"),
    ("Control Voz", "🎙️ Voz", "Permite controlar acciones mediante comandos de voz.", "https://control-voice-jtclbz7tkab7tat7sad7ue.streamlit.app"),
    ("MQTT Control", "🌐 IoT", "Controla acciones o dispositivos mediante comunicación MQTT.", "https://mqtt-control-lnepauv4hu8elbvnancrmu.streamlit.app"),
    ("Lector de Sensor MQTT", "📡 IoT", "Lee y visualiza datos provenientes de sensores conectados mediante MQTT.", "https://sensor-mqtt-8tmvwvhazxsftvph3uazzz.streamlit.app"),
]

# ---------- GRID ----------
cols = st.columns(3)

for i, proyecto in enumerate(proyectos):
    titulo, categoria, descripcion, url = proyecto

    with cols[i % 3]:
        tarjeta(titulo, categoria, descripcion, url)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <p>✨ Portafolio académico de IA - Sofía Betancur ✨</p>
</div>
""", unsafe_allow_html=True)
