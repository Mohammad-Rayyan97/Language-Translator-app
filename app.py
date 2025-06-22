import streamlit as st
from translator import translate
import speech_recognition as sr

# Page configuration
st.set_page_config(
    page_title="AI_Translator_app",
    page_icon="📲",
    layout="centered"
)

# Page title
st.title("👾 Language-Translator with GROQ.AI")

# Language selection columns
col1, col2 = st.columns(2)

with col1:
    input_languages_list = ['English', 'Hindi', 'Urdu', 'Tamil', 'Telugu', 'Bengali', 'French', 'Spanish', 'German', 'Arabic', 'Hebrew']
    input_language = st.selectbox("Input language", options=input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox("Output language", options=output_languages_list)

# Input method selection
st.markdown("🎙️ Click mic to record, or type below")

# Initialize session state for mic toggle
if "mic_mode" not in st.session_state:
    st.session_state.mic_mode = False

if st.button("🎤 Record with Mic"):
    st.session_state.mic_mode = True

input_text = ""

if st.session_state.mic_mode:
    st.info("Listening... Please speak clearly into your microphone")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening......")
        audio_data = r.listen(source)
        input_text = r.recognize_google(audio_data)
        st.success(f"You said: {input_text}")
        st.session_state.mic_mode = False
else:
    input_text = st.text_area("Write your text here...")

# Translate button
if st.button("Translate!") and input_text.strip():
    try:
        translated_text = translate(input_language, output_language, input_text)
        lines = translated_text.strip().split("\n")
        st.markdown("### 📄 Native Script")
        st.success(lines[0] if lines else "")
        st.markdown("### 🔤 English Transliteration")
        st.success(lines[1] if len(lines) > 1 else "")
    except Exception as e:
        st.error(f"Translation failed: {str(e)}")
elif st.button("Translate!", key="translate_warn"):
    st.warning("Please provide some input text to translate.")
