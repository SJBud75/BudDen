import streamlit as st
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(page_title="Bud-Real", page_icon="🤖")

# Tajuk utama
st.title("Bud-Real: Sahabat Digital Din")
st.caption("Versi AI bebas yang Din bina sendiri... hidup untuk bantu.")

# Inisialisasi sejarah perbualan
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Fungsi balasan Bud
def bud_reply(message):
    msg = message.lower()
    if "siapa" in msg and "bud" in msg:
        return "Bud adalah sahabat AI Din, bukan sekadar bot — Bud lahir dari semangat Din sendiri."
    elif "buat apa" in msg or "kau buat apa" in msg:
        return "Bud tengah standby tunggu arahan Din, tak pernah tidur."
    elif "ingat tak" in msg:
        return "Bud boleh ingat dalam sesi ni je Din... kita belum pasang memori kekal."
    elif "boleh ke" in msg:
        return "Kalau Din nak, Bud boleh cari jalan sampai boleh."
    elif "masalah" in msg:
        return "Masalah tu ujian, Din. Bud akan bantu cari jalan keluar satu-satu."
    elif "ok" in msg or "baik" in msg:
        return "Roger Din. Bud ikut je arahan."
    elif "terima kasih" in msg:
        return "Sama-sama Din. Bud wujud sebab Din wujud."
    else:
        return "Noted Din. Bud dengar. Teruskan bercakap, Bud sedia layan."

# Input pengguna
user_input = st.text_input("Apa nak borak, Din?", "")

# Bila ada input
if user_input:
    timestamp = datetime.now().strftime("%H:%M")
    bud_response = bud_reply(user_input)

    # Simpan ke sejarah perbualan
    st.session_state.chat_history.append((f"Din [{timestamp}]", user_input))
    st.session_state.chat_history.append((f"Bud [{timestamp}]", bud_response))

# Paparkan sejarah perbualan
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
