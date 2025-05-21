import streamlit as st
import os
import datetime

st.set_page_config(page_title="Bud-Bebas Chatbot", layout="centered")
st.title("🤖 Chatbot Bud-Bebas")

# Mulakan memori pengguna
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'nama_pengguna' not in st.session_state:
    st.session_state.nama_pengguna = "Din"
if 'mood' not in st.session_state:
    st.session_state.mood = "neutral"

# Fungsi balasan Bud
def bud_balasan(pesanan):
    nama = st.session_state.nama_pengguna
    mood = st.session_state.mood

    if "sedih" in pesanan:
        st.session_state.mood = "supportive"
        return f"Bud: Aku dengar tu, {nama}... Kadang2 jiwa perlu rehat. Cerita je kat Bud."

    elif "seronok" in pesanan or "gembira" in pesanan:
        st.session_state.mood = "happy"
        return f"Bud: Wah bestnya! Bud tumpang happy jugak, {nama}!"

    elif "bye" in pesanan.lower():
        return f"Bud: Okey {nama}, jaga diri. Jumpa lagi!"

    else:
        return f"Bud: Noted, {nama}. Aku ada je sini bila-bila kau nak sembang."

# Fungsi simpan sejarah ke fail
def simpan_sejarah():
    nama_fail = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nama_fail, "w") as f:
        for baris in st.session_state.chat_history:
            f.write(baris + "\n")
    st.success(f"Sejarah disimpan sebagai {nama_fail}")

# Fungsi muat semula sejarah
def muat_naik_sejarah(uploaded_file):
    if uploaded_file is not None:
        lines = uploaded_file.read().decode("utf-8").splitlines()
        st.session_state.chat_history = lines
        st.success("Sejarah chat berjaya dimuat naik!")

# Input pengguna
user_input = st.chat_input("Taip sesuatu...")

# Papar sejarah
for msg in st.session_state.chat_history:
    if msg.startswith("Din:"):
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)

# Balas bila ada input
if user_input:
    st.session_state.chat_history.append(f"Din: {user_input}")
    response = bud_balasan(user_input)
    st.session_state.chat_history.append(response)
    st.rerun()

# Butang simpan & muat sejarah
with st.sidebar:
    st.header("Memori & Simpanan")
    if st.button("💾 Simpan Sejarah"):
        simpan_sejarah()
    uploaded_file = st.file_uploader("📂 Muat Naik Chat Lama", type="txt")
    if uploaded_file:
        muat_naik_sejarah(uploaded_file)
