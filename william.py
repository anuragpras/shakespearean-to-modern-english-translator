import streamlit as st
from googletrans import Translator

translator = Translator()

# Function to translate Shakespearean English to Modern English
def shakespearean_to_modern(text):
    try:
        translated = translator.translate(text, src='en', dest='en-shakespeare').text
    except Exception as e:
        st.error("Translation error: {}".format(str(e)))
        return None
    return translated

# Function to translate Modern English to Shakespearean English
def modern_to_shakespearean(text):
    try:
        translated = translator.translate(text, src='en', dest='en').text
    except Exception as e:
        st.error("Translation error: {}".format(str(e)))
        return None
    return translated

# Streamlit app UI
def main():
    st.set_page_config(page_title="Shakespearean to Modern English Translator", layout="centered", initial_sidebar_state="collapsed")

    st.title("Shakespearean to Modern English Translator")
    st.subheader("Translate text between Shakespearean English and Modern English")

    # Input text area
    text = st.text_area("Enter text to translate:")

    if text:
        # Translate Shakespearean English to Modern English
        translated_modern = shakespearean_to_modern(text)
        if translated_modern:
            st.markdown("### Modern English Translation:")
            st.write(translated_modern)

        st.markdown("---")

        # Translate Modern English to Shakespearean English
        translated_shakespearean = modern_to_shakespearean(text)
        if translated_shakespearean:
            st.markdown("### Shakespearean English Translation:")
            st.write(translated_shakespearean)

if __name__ == "__main__":
    main()
