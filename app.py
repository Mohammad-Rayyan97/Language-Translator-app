import streamlit as st
from translator import translate


# page configuration
st.set_page_config(
    page_title = "AI_Translator_app",
    page_icon = "📲",
    layout = "centered"
)

# page title
st.title("👾Language-Translator with GROQ")

# setting columns
col1, col2 = st.columns(2)

with col1:
    input_languages_list=['English','Hindi','Urdu','Tamil','Telugu','Bengali','French','Spanish','German','Arabic','Hebrew']
    input_language = st.selectbox(label = "input language", options=input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="output language",options=output_languages_list)

input_text = st.text_area("type your text here.....")

# creating the translate button
if st.button("Translate!"):
    translated_text = translate(input_language,output_language,input_text )
    st.success(translated_text)