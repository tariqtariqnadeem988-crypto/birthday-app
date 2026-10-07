'''import tkinter as t
window=t.Tk()
window.title("My name is  Areesha")
window.geometry("400x300")
button1=t.Button(window,text="Noor",width=30,bg="lightblue")
button1.pack(pady=30)
button2=t.Button(window,text="Tariq",width=40,bg="grey")
button2.pack(pady =20)
btn3=t.Button(window,text="Shahida",width=30,bg="red")
btn3.pack(pady=39)'''
import random
import streamlit as st

# App title and styling
st.set_page_config(page_title="Birthday Wish Generator", page_icon="🎂")

st.title("🎉 Python Birthday Wish Generator 🎈")
st.write(
    "Enter a name below to instantly generate a personalized birthday wish!"
)

# Input field for the name
name_input = st.text_input(
    "Birthday Person's Name:", placeholder="e.g., Alex"
)

# A list of fun birthday wishes
wishes = [
    (
        "Happy Birthday, {name}! May your day be filled with lots of love,"
        " laughter, and cake! 🎂✨"
    ),
    (
        "Wishing you a fantastic year ahead, {name}! May all your dreams and"
        " wishes come true this year. 🌟"
    ),
    (
        "Happy Birthday to the amazing {name}! Hope your special day brings you"
        " as much happiness as you bring to everyone else. 🎈"
    ),
    (
        "Cheers to another fabulous year of life, {name}! Have an unforgettable"
        " birthday celebration! 🥳🎁"
    ),
]

# Generate button
if st.button("Generate Wish 🎁"):
  if name_input.strip() == "":
    st.warning("⚠️ Please enter a name first!")
  else:
    # Pick a random wish and format it with the entered name
    selected_wish = random.choice(wishes).format(name=name_input.strip())

    # Display the result in a success box
    st.success("Here is your custom wish:")
    st.markdown(f"### 💌 {selected_wish}")

    # Optional: Add a celebratory balloon effect
    st.balloons()