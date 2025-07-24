#!/usr/bin/env python3
"""
Voice Assistant - Simple Text/Voice Input with Audio & Visual Output
"""

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai
import toml
import io
import base64
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════

try:
    config = toml.load('config.toml')
    genai.configure(api_key=config['api_keys']['gemini'])
except Exception as e:
    st.error(f"⚠️ Configuration error: {e}")
    st.stop()

# ═══════════════════════════════════════════════════════════════════
# Core Functions
# ═══════════════════════════════════════════════════════════════════

def listen_for_speech():
    """Capture speech input."""
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎤 Listening... Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "❓ Could not understand audio"
    except sr.RequestError as e:
        return f"🚫 Speech service error: {e}"
    except Exception as e:
        return f"⚠️ Error: {e}"

def generate_response(user_input):
    """Generate AI response."""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"You are a helpful voice assistant. Respond naturally and concisely to: {user_input}"
        return model.generate_content(prompt).text
    except Exception as e:
        return f"I'm having trouble right now: {e}"

def text_to_speech(text):
    """Convert text to speech."""
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        audio_base64 = base64.b64encode(audio_buffer.read()).decode()
        
        return f"""
        <audio controls autoplay style="width: 100%; margin: 10px 0;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """
    except Exception:
        return None

def process_input(user_input, input_type):
    """Process user input and generate response."""
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "input_type": input_type,
        "timestamp": datetime.now()
    })
    
    # Generate AI response
    with st.spinner("🤖 Thinking..."):
        ai_response = generate_response(user_input)
    
    # Generate audio
    with st.spinner("🔊 Creating audio..."):
        audio_html = text_to_speech(ai_response)
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response,
        "audio": audio_html,
        "timestamp": datetime.now()
    })

# ═══════════════════════════════════════════════════════════════════
# UI Styling
# ═══════════════════════════════════════════════════════════════════

def load_css():
    return """
    <style>
        .header {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
        }
        .chat-message {
            padding: 15px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .user-msg {
            background: linear-gradient(135deg, #4CAF50, #45a049);
            color: white;
            margin-left: 20%;
        }
        .bot-msg {
            background: linear-gradient(135deg, #2196F3, #1976D2);
            color: white;
            margin-right: 20%;
        }
        .input-container {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }
    </style>
    """

# ═══════════════════════════════════════════════════════════════════
# Main Application Function
# ═══════════════════════════════════════════════════════════════════

def app():
    """Main application function - primary entry point."""
    st.set_page_config(
        page_title="Voice Assistant",
        page_icon="🎙️",
        layout="wide"
    )
    
    # Load styling
    st.markdown(load_css(), unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="header">
        <h1>🎙️ Voice Assistant</h1>
        <p>Type or speak your message - I'll respond with text and audio!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Input Section
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💬 Text Input")
        text_input = st.text_area("Type your message:", height=100, key="text_input")
        send_text = st.button("📤 Send Text", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("🎤 Voice Input")
        st.write("Click to speak:")
        send_voice = st.button("🎙️ Start Speaking", type="secondary", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Process Text Input
    if send_text and text_input.strip():
        process_input(text_input.strip(), "text")
        st.rerun()
    
    # Process Voice Input
    if send_voice:
        with st.spinner("🎤 Listening..."):
            voice_input = listen_for_speech()
            if voice_input and not voice_input.startswith(('❓', '🚫', '⚠️')):
                st.success(f"📝 I heard: {voice_input}")
                process_input(voice_input, "voice")
                st.rerun()
            else:
                st.error(voice_input)
    
    # Display Chat History
    st.subheader("💬 Conversation")
    
    if st.session_state.messages:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                icon = "🎤" if msg.get("input_type") == "voice" else "💬"
                st.markdown(f"""
                <div class="chat-message user-msg">
                    <strong>{icon} You:</strong><br>{msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-msg">
                    <strong>🤖 Assistant:</strong><br>{msg["content"]}
                </div>
                """, unsafe_allow_html=True)
                
                # Add audio for bot responses
                if "audio" in msg and msg["audio"]:
                    st.markdown(msg["audio"], unsafe_allow_html=True)
    else:
        st.info("👋 Start a conversation using text or voice input above!")
    
    # Clear Chat Button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    app()
