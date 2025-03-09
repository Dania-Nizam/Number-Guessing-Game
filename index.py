import streamlit as st
import random

# Function to initialize game state
def initialize_game():
    return random.randint(1, 50)

# Streamlit App UI
st.set_page_config(page_title="🎯 Number Guessing Game", page_icon="🎮")

st.title("🎯 Guess the Number Game!")

# Initialize game state
if 'number' not in st.session_state:
    st.session_state.number = initialize_game()
    st.session_state.guesses = 0
    st.session_state.feedback = ""
    st.session_state.game_over = False
    st.session_state.best_score = None  # Track best score

# Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .big-font {
        font-size:24px !important;
        font-weight: bold;
        color: #4CAF50;
    }
    .feedback {
        font-size:18px !important;
        font-weight: bold;
    }
    .score {
        font-size:20px !important;
        font-weight: bold;
        color: #FF5733;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Best Score
if st.session_state.best_score is not None:
    st.markdown(f"<p class='score'>🏆 Best Score: {st.session_state.best_score} attempts</p>", unsafe_allow_html=True)

# User Input
guess = st.number_input("🔢 Enter a number between 1 and 50:", min_value=1, max_value=50, step=1)

# Submit Guess
if st.button("🎯 Submit Guess", use_container_width=True):
    if not st.session_state.game_over:
        st.session_state.guesses += 1
        
        if guess == st.session_state.number:
            st.session_state.feedback = f"🎉 **Correct! You guessed the number {st.session_state.number} in {st.session_state.guesses} attempts!**"
            st.session_state.game_over = True
            st.balloons()  # Celebration animation
            
            # Update Best Score
            if st.session_state.best_score is None or st.session_state.guesses < st.session_state.best_score:
                st.session_state.best_score = st.session_state.guesses  # Store new best score
                
        elif guess < st.session_state.number:
            st.session_state.feedback = "🔼 **Too low! Try a higher number.**"
        else:
            st.session_state.feedback = "🔽 **Too high! Try a lower number.**"

# Show Feedback
if st.session_state.feedback:
    st.markdown(f"<p class='feedback'>{st.session_state.feedback}</p>", unsafe_allow_html=True)

# Progress Bar to indicate range
progress = (guess / 50)
st.progress(progress)

# Play Again Button
if st.session_state.game_over:
    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.number = initialize_game()
        st.session_state.guesses = 0
        st.session_state.feedback = ""
        st.session_state.game_over = False
        st.rerun()  # ✅ Reload the app
