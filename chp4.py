import random
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sister's Birthday Wish Generator", page_icon="💖")

st.title("🎂 Special Birthday Wish for My Sweet Sister! 🌸")
st.write(
    "Apni pyaari si behn ka naam likhein aur uske liye ek pyari si wish"
    " generate karein!"
)

# Text input for the name
name_input = st.text_input("Sister's Name:", placeholder="e.g., Ayesha")

# Pool of heartfelt, special wishes for a sister
wishes = [
    (
        "Duniya ki sab se pyaari aur caring behn, {name} ko salgirah bohot"
        " bohot Mubarak ho! 🎂💖 Tum meri sirf behn hi nahi balkay meri sab se"
        " achi dost bhi ho. Allah pak tumhe zindagi ki har khushi, sehat aur"
        " kamyabi ata farmaye. Tum hamesha aise hi muskurati raho aur hamari"
        " zindagi roshan karti raho! Ameen ✨🌷"
    ),
    (
        "Happy Birthday to my lovely sister, {name}! 🎉 Tumhare sath bachpan"
        " se lekar ab tak ki saari yaadein mere dil ke bohot kareeb hain. Dua"
        " hai ke yeh naya saal tumhari zindagi mein dher saari khushiyan, nayi"
        " kamyabiyan aur behtareen mauqay le kar aaye. You mean the world to"
        " me! 🌟💕"
    ),
    (
        "Meri pyaari behn {name}, Allah tala tumhe hamesha hasti muskurati"
        " rakhe aur tumhare sare khwab poore kare! 🌸 Tum jaisi understanding"
        " aur loving behn hona kisi blessing se kam nahi hai. Have the most"
        " amazing and memorable birthday ever! 🎁🥳"
    ),
    (
        "To my wonderful sister, {name} — Happy Birthday! 🎈 Zindagi ke kisi bhi"
        " mod par tumhein kabhi kisi cheez ki pareshani na ho aur tum hamesha"
        " aise hi chamkti raho. Tumhari khushi meri khushi hai. Aaj ka din"
        " sirf aur sirf tumhara hai, enjoy every single second of it! 🥂💖✨"
    ),
]

# Button action
if st.button("Generate Sister's Wish 🎁"):
  if not name_input.strip():
    st.warning("⚠️ Pehle apni behn ka naam toh likhein!")
  else:
    # Pick a random wish and format it with the entered name
    selected_wish = random.choice(wishes).format(name=name_input.strip())

    # Display results
    st.success("Yeh raha aapki behn ke liye sab se khoobsurat wish:")
    st.markdown(f"### 💌 {selected_wish}")

    # Fun celebration effect
    st.balloons()
