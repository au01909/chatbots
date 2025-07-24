import streamlit as st
from streamlit_chat import message
import time
import json
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Load animation safely
animation1 = load_lottie_animation("assets/quic_rail.json")

stations = ["Banglore", "Delhi", "Mumbai", "Chennai", "Hyderabad", "Kolkata"]

prices = {
    # Your existing prices dictionary
    ("Banglore", "Delhi"): 20,
    ("Banglore", "Mumbai"): 30,
    ("Banglore", "Chennai"): 40,
    ("Banglore", "Hyderabad"): 25,
    ("Banglore", "Kolkata"): 35,
    
    ("Delhi", "Banglore"): 20,
    ("Delhi", "Mumbai"): 30,
    ("Delhi", "Chennai"): 40,
    ("Delhi", "Hyderabad"): 25,
    ("Delhi", "Kolkata"): 35,

    ("Mumbai", "Banglore"): 30,
    ("Mumbai", "Delhi"): 30,
    ("Mumbai", "Chennai"): 40,
    ("Mumbai", "Hyderabad"): 25,
    ("Mumbai", "Kolkata"): 35,

    ("Chennai", "Banglore"): 40,
    ("Chennai", "Delhi"): 40,
    ("Chennai", "Mumbai"): 40,
    ("Chennai", "Hyderabad"): 25,
    ("Chennai", "Kolkata"): 35,

    ("Hyderabad", "Banglore"): 25,
    ("Hyderabad", "Delhi"): 25,
    ("Hyderabad", "Mumbai"): 25,
    ("Hyderabad", "Chennai"): 25,
    ("Hyderabad", "Kolkata"): 35,

    ("Kolkata", "Banglore"): 35,
    ("Kolkata", "Delhi"): 35,
    ("Kolkata", "Mumbai"): 35,
    ("Kolkata", "Chennai"): 35,
    ("Kolkata", "Hyderabad"): 35,
}

def calculate_price(from_station, to_station, passengers):
    return prices.get((from_station, to_station), 50) * passengers

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'num_passengers' not in st.session_state:
    st.session_state.num_passengers = None
if 'from_station' not in st.session_state:
    st.session_state.from_station = None
if 'to_station' not in st.session_state:
    st.session_state.to_station = None
if 'show_thank_you' not in st.session_state:
    st.session_state.show_thank_you = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

def app():
    col01, col02 = st.columns([1, 0.4])
    with col01:
        st.title("QuickRail - Train Ticket Booking Chatbot")
        st.write(":orange[Tired of long queues for train tickets?] Don't worry, that's a thing of the past!  \nBook tickets instantly from anywhere. Just chat, choose your destination, pay, and enjoy a hassle-free booking experience.")
        st.markdown("---")
    with col02:
        if animation1:
            st_lottie(animation1, height=210, key="animation1")
    
    col11, col22 = st.columns([1, 0.5])
    
    with col11:
        # Step 0: Initial state
        if st.session_state.step == 0:
            if st.button("Book your Tickets Now"):
                st.session_state.messages.append({
                    "content": "Hello! How many passengers are traveling?", 
                    "is_user": False
                })
                st.session_state.step = 1
                st.rerun()

        # Display previous messages - FIXED VERSION
        for msg in st.session_state.messages:
            # Ensure the message has the required keys
            if isinstance(msg, dict) and "content" in msg and "is_user" in msg:
                role = "assistant" if not msg["is_user"] else "user"
                avatar_image = "train.png" if role == "assistant" else "user.jpg"
                
                # Use fallback avatars if images don't exist
                try:
                    with st.chat_message(role):
                        st.write(msg["content"] + (" 🚆" if role == "assistant" else " ✅"))
                except:
                    # Fallback without avatar
                    if role == "assistant":
                        st.write(f"🤖 {msg['content']} 🚆")
                    else:
                        st.write(f"👤 {msg['content']} ✅")

        # Step 1: Ask for passengers
        if st.session_state.step == 1:
            col1, col2 = st.columns([2, 1])  
            with col2:
                user_input = st.selectbox("Number of passengers:", list(range(1, 6)))
                if st.button("Submit", key="passengers_submit"):
                    st.session_state.num_passengers = user_input
                    st.session_state.messages.append({
                        "content": f"{user_input}", 
                        "is_user": True
                    })
                    st.session_state.messages.append({
                        "content": "Please select your departure station.", 
                        "is_user": False
                    })
                    st.session_state.step = 2
                    st.rerun()

        # Step 2: Ask for departure station
        elif st.session_state.step == 2:
            col1, col2 = st.columns([2, 1])
            with col2:
                user_input = st.selectbox("Departure station:", stations)
                if st.button("Submit", key="departure_submit"):
                    st.session_state.from_station = user_input
                    st.session_state.messages.append({
                        "content": user_input, 
                        "is_user": True
                    })
                    st.session_state.messages.append({
                        "content": "Please select your destination station.", 
                        "is_user": False
                    })
                    st.session_state.step = 3
                    st.rerun()

        # Step 3: Ask for destination station
        elif st.session_state.step == 3:
            col1, col2 = st.columns([2, 1])
            with col2:
                user_input = st.selectbox("Destination station:", stations)
                if st.session_state.from_station == user_input:
                    st.error("Departure and destination stations cannot be the same!")
                else:
                    if st.button("Submit", key="destination_submit"):
                        st.session_state.to_station = user_input
                        st.session_state.messages.append({
                            "content": user_input, 
                            "is_user": True
                        })
                        ticket_price = calculate_price(
                            st.session_state.from_station, 
                            st.session_state.to_station, 
                            st.session_state.num_passengers
                        )
                        st.session_state.messages.append({
                            "content": f"Your total price for {st.session_state.num_passengers} passenger(s) from {st.session_state.from_station} to {st.session_state.to_station} is ₹{ticket_price}.", 
                            "is_user": False
                        })
                        st.session_state.step = 4
                        st.rerun()

        # Step 4: Payment
        if st.session_state.step == 4:
            col1, col2 = st.columns([2, 1])
            with col2:
                if st.button("Make Payment"):
                    try:
                        st.image('payment.jpg')
                    except:
                        st.write("💳 Payment QR Code would appear here")
                    
                    # Instead of time.sleep (which blocks), use a success message
                    st.success("Payment processed successfully!")
                    st.session_state.show_thank_you = True
                    st.rerun()

        if st.session_state.show_thank_you:
            col1, col2 = st.columns([2, 1])  
            with col2:
                if st.button("Thank You - Book Another Ticket"):
                    # Reset session state
                    st.session_state.messages = []
                    st.session_state.step = 0
                    st.session_state.num_passengers = None
                    st.session_state.from_station = None
                    st.session_state.to_station = None
                    st.session_state.start_time = None
                    st.session_state.show_thank_you = False
                    st.rerun()

    with col22:
        with st.form('Question2'):
            st.write("  - :orange[About this Chatbot]")
            st.write("This chatbot follows a rule-based approach to guide users through ticket booking. It provides predefined responses based on user inputs. Errors like selecting the same departure and destination are flagged. The chatbot is structured, interactive, and calculates ticket prices dynamically.")
            if st.form_submit_button("Hope it helped"):
                st.write("Feel free to customise and use it. Push any improvements to the repo!")

if __name__ == "__main__":
    app()
