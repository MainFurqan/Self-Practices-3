import random
import streamlit as st

# Set up a random target number
Target = random.randint(1, 1000)

# Streamlit app layout
st.title("Number Guessing Game")
st.write("Guess a number between 1 and 1000")

# User input for the guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=1000, step=1)

# Placeholder for results
result_placeholder = st.empty()

# Submit button
guess_button = st.button("Submit Guess")

# Check the user's guess
if guess_button:
    if user_guess == Target:
        result_placeholder.success("You Successfully Guessed the Number!")
        st.balloons()
    elif user_guess < Target:
        result_placeholder.info("Your Guess is Less than the Target. Try again!")
    elif user_guess > Target:
        result_placeholder.info("Your Guess is Greater than the Target. Try again!")
