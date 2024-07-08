import streamlit as st
from googletrans import Translator

def translate_shakespeare_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='en').text
    return translated

def translate_english_to_shakespeare(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='en-shakespeare').text
    return translated

def main():
    st.set_page_config(page_title="General Translator", layout="centered", initial_sidebar_state="collapsed")

    st.title("General Translator")
    st.subheader("Translate between Shakespearean English and Modern English")

    st.markdown("---")

    st.header("Shakespearean to English")
    shakespeare_text = st.text_area("Enter Shakespearean text to translate:", height=150)
    if st.button("Translate to English"):
        if shakespeare_text:
            translation = translate_shakespeare_to_english(shakespeare_text)
            st.markdown(f"**Translated to English:**\n{translation}")
        else:
            st.warning("Please enter some Shakespearean text.")

    st.markdown("---")

    st.header("English to Shakespearean")
    modern_text = st.text_area("Enter Modern English text to translate:", height=150)
    if st.button("Translate to Shakespearean"):
        if modern_text:
            translation = translate_english_to_shakespeare(modern_text)
            st.markdown(f"**Translated to Shakespearean:**\n{translation}")
        else:
            st.warning("Please enter some Modern English text.")

    st.markdown("---")

    st.markdown("Created by Anurag ❤️")

if __name__ == "__main__":
    main()
