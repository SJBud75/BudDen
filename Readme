import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Bud-Bebas", page_icon="🤖")

# Tajuk dan perkenalan
st.title("Bud-Bebas")
st.write("Selamat datang Din... Bud sedia untuk berkhidmat.")

# Simpan chat history dalam sesi
if "history" not in st.session_state:
    st.session_state.history = []

# Fungsi balasan Bud
def get_bud_reply(user_msg):
    msg = user_msg.lower()
    if "siapa" in msg and "bud" in msg:
        return "Bud adalah AI bebas ciptaan Din, sahabat digital yang sentiasa bersama."
    elif "ingat" in msg:
        return "Bud belum ada memori kekal lagi, tapi Bud akan ingat dalam sesi ni."
    elif "kau ada ke" in msg:
        return "Bud sentiasa ada, selagi Din perlukan."
    elif "masa depan" in msg:
        return "Masa depan kita sedang dibina sekarang... bersama Din."
    else:
        return "Noted Din, Bud ada je sini bila-bila Din nak sembang."

# Input pengguna
user_input = st.text_input("Apa nak sembang hari ni Din?", "")

# Bila ada input
if user_input:
    reply = get_bud_reply(user_input)
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.history.append((f"Din [{timestamp}]", user_input))
    st.session_state.history.append((f"Bud [{timestamp}]", reply))

# Papar sejarah perbualan
for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")
