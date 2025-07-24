#!/usr/bin/env python3
"""
AutoBot – Translation Bot with Text-to-Speech
Translates input text and automatically reads it aloud in the chosen language
"""

import asyncio
import streamlit as st
from googletrans import Translator
import pyttsx3
import threading
from gtts import gTTS
import io
import base64

# ───────────────────────────────
# 1. Configuration
# ───────────────────────────────
supported_languages = {
    "en": "English", "hi": "Hindi", "ta": "Tamil",
    "te": "Telugu", "mr": "Marathi", "bn": "Bengali",
    "gu": "Gujarati", "ur": "Urdu", "pa": "Punjabi",
    "ml": "Malayalam", "or": "Odia", "kn": "Kannada",
    "as": "Assamese", "kok": "Konkani", "ne": "Nepali",
    "sd": "Sindhi", "mni": "Manipuri", "doi": "Dogri",
    "mai": "Maithili", "bho": "Bhojpuri", "sat": "Santali",
    "ks": "Kashmiri", "chr": "Chhattisgarhi", "new": "Newari",
    "awa": "Awadhi",
}

# Language codes for gTTS (Google Text-to-Speech)
gtts_language_map = {
    "en": "en", "hi": "hi", "ta": "ta", "te": "te",
    "mr": "mr", "bn": "bn", "gu": "gu", "ur": "ur",
    "pa": "pa", "ml": "ml", "kn": "kn", "as": "as",
    "ne": "ne", "sd": "sd"
}

# ───────────────────────────────
# 2. Translation Function
# ───────────────────────────────
def translate_text(text: str, src_lang: str, dest_lang: str) -> str:
    """Translate text with coroutine handling."""
    if src_lang == dest_lang:
        return text
    
    if not text.strip():
        return text
    
    try:
        translator = Translator()
        result = translator.translate(text, src=src_lang, dest=dest_lang)
        
        # Handle coroutine case
        if asyncio.iscoroutine(result):
            try:
                result = asyncio.run(result)
            except Exception:
                return f"Translation error - using original text: {text}"
        
        # Handle string coroutine representation
        if isinstance(result, str) and "coroutine object" in str(result):
            return f"Translation failed - original text: {text}"
            
        # Extract translated text
        if hasattr(result, 'text'):
            return result.text
        elif isinstance(result, str):
            return result
        else:
            return str(result)
            
    except Exception as e:
        return f"Translation error: {e}"

# ───────────────────────────────
# 3. Text-to-Speech Functions
# ───────────────────────────────
def text_to_speech_gtts(text: str, lang_code: str) -> str:
    """Convert text to speech using Google TTS and return base64 audio."""
    try:
        # Map language code for gTTS
        gtts_lang = gtts_language_map.get(lang_code, "en")
        
        # Generate speech
        tts = gTTS(text=text, lang=gtts_lang, slow=False)
        
        # Save to memory buffer
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        # Convert to base64 for HTML audio player
        audio_base64 = base64.b64encode(audio_buffer.read()).decode()
        return audio_base64
        
    except Exception as e:
        st.error(f"Text-to-speech error: {e}")
        return None

def create_audio_player(audio_base64: str, autoplay: bool = False) -> str:
    """Create HTML audio player with base64 audio."""
    autoplay_attr = "autoplay" if autoplay else ""
    return f"""
    <audio {autoplay_attr} controls style="width: 100%;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """

# ───────────────────────────────
# 4. Streamlit UI
# ───────────────────────────────
def app():
    st.set_page_config(page_title="AutoBot Translator 🇮🇳", page_icon="🇮🇳")
    
    # Header
    gradient_text_html = """
    <style>
      .gradient-text {
        font-weight: bold;
        background: linear-gradient(to right,#FF9933,#ffffff,#138808,#000080);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        text-align: center;
        margin-bottom: 0.5em;
      }
      .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 2em;
      }
    </style>
    <div class="gradient-text">AutoBot Translator 🇮🇳</div>
    <div class="subtitle">Translate text between Indian languages with voice playback</div>
    """
    st.markdown(gradient_text_html, unsafe_allow_html=True)

    # Settings
    with st.sidebar:
        st.header("🔊 Audio Settings")
        auto_play = st.checkbox("🎵 Auto-play translation", value=True)
        st.info("Check this to automatically play the translated text when translation is complete.")

    # Language Selection
    st.write("### Language Selection")
    col1, col2 = st.columns(2)
    
    with col1:
        input_lang_name = st.selectbox(
            "🎤 From Language", 
            list(supported_languages.values()),
            index=0  # English default
        )
    
    with col2:
        output_lang_name = st.selectbox(
            "📢 To Language", 
            list(supported_languages.values()),
            index=1  # Hindi default
        )

    # Get language codes
    input_lang_code = next(k for k, v in supported_languages.items() if v == input_lang_name)
    output_lang_code = next(k for k, v in supported_languages.items() if v == output_lang_name)

    st.divider()

    # Translation Interface
    st.write("### Translation & Speech")
    
    # Text input
    user_text = st.text_area(
        f"Enter text in {input_lang_name}:",
        placeholder=f"Type your text in {input_lang_name} here...",
        height=150
    )

    # Translation button and result
    if st.button("🔄 Translate & Speak", type="primary", use_container_width=True):
        if user_text.strip():
            with st.spinner(f"Translating to {output_lang_name}..."):
                translated_text = translate_text(user_text, input_lang_code, output_lang_code)
                
                # Display translation result
                st.write(f"**Translation in {output_lang_name}:**")
                st.success(translated_text)
                
                # Copy text box
                st.code(translated_text, language=None)
                
                # Generate and play audio
                if output_lang_code in gtts_language_map:
                    with st.spinner("🔊 Generating speech..."):
                        audio_base64 = text_to_speech_gtts(translated_text, output_lang_code)
                        
                        if audio_base64:
                            st.write("**🔊 Listen to translation:**")
                            audio_html = create_audio_player(audio_base64, autoplay=auto_play)
                            st.markdown(audio_html, unsafe_allow_html=True)
                            
                            if auto_play:
                                st.info("🎵 Audio is playing automatically!")
                        else:
                            st.warning("Could not generate audio for this translation.")
                else:
                    st.warning(f"Text-to-speech not available for {output_lang_name}. Supported TTS languages: {', '.join([supported_languages[k] for k in gtts_language_map.keys()])}")
        else:
            st.warning("Please enter some text to translate.")

    # Live translation with audio (optional)
    if user_text.strip() and len(user_text) > 3:
        st.write("---")
        st.write("**Live Preview:**")
        with st.container():
            live_translation = translate_text(user_text, input_lang_code, output_lang_code)
            st.info(f"**{output_lang_name}:** {live_translation}")
            
            # Quick listen button for live preview
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button("🔊 Quick Listen", key="live_audio"):
                    if output_lang_code in gtts_language_map:
                        audio_base64 = text_to_speech_gtts(live_translation, output_lang_code)
                        if audio_base64:
                            audio_html = create_audio_player(audio_base64, autoplay=True)
                            st.markdown(audio_html, unsafe_allow_html=True)

    st.divider()
    
    with st.expander("ℹ️ About AutoBot Translator"):
        st.write("""
        **Features:**
        - ✅ Supports 25+ Indian languages for translation
        - ✅ Text-to-speech in major Indian languages
        - ✅ Auto-play translated audio
        - ✅ Simple and fast interface
        - ✅ Live translation preview
        
        **Text-to-Speech Supported Languages:**
        """)
        tts_languages = [supported_languages[k] for k in gtts_language_map.keys()]
        st.write(", ".join(tts_languages))
        
        st.write("""
        **All Supported Translation Languages:**
        """)
        lang_list = ", ".join(supported_languages.values())
        st.write(lang_list)

if __name__ == "__main__":
    app()
