import streamlit as st
from PIL import Image
import random

# Konfigurasi halaman
st.set_page_config(
    page_title="Hello Kitty Greetings",
    page_icon="🎀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Fungsi untuk generate warna random
def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Custom CSS untuk styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');
    
    .hello-kitty-theme {
        background: linear-gradient(45deg, #FF9A8B, #FF6F91, #FF9671, #FFC75F);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-family: 'Comic Neue', cursive;
    }
    
    .title {
        color: #FFFFFF;
        text-shadow: 2px 2px #FF6F91;
        font-size: 3rem !important;
    }
    
    .message {
        background: rgba(255, 255, 255, 0.8);
        padding: 1.5rem;
        border-radius: 15px;
        font-size: 1.5rem;
        color: #333333;
        margin: 1rem 0;
    }
    
    .kitty-image {
        max-width: 200px;
        margin: 0 auto;
        display: block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
</style>
""", unsafe_allow_html=True)

# Konten utama
st.markdown("<div class='hello-kitty-theme'>", unsafe_allow_html=True)

# Header dengan animasi
st.markdown("<h1 class='title'>🎀 Hello Kitty Greetings 🎀</h1>", unsafe_allow_html=True)

# Input dari user
name = st.text_input("Masukkan nama kamu:", max_chars=20)
occasion = st.selectbox(
    "Pilih acara:",
    ["Ulang Tahun", "Selamat Pagi", "Selamat Siang", "Selamat Malam", "Selamat Hari Raya"]
)

# Tombol generate ucapan
if st.button("Buat Ucapan 🎀"):
    if name:
        # Template ucapan
        greetings = {
            "Ulang Tahun": f"Happy Birthday, {name}! 🎂🎉",
            "Selamat Pagi": f"Good Morning, {name}! 🌞🌸",
            "Selamat Siang": f"Good Afternoon, {name}! ☀️🍱",
            "Selamat Malam": f"Good Night, {name}! 🌙⭐",
            "Selamat Hari Raya": f"Happy Holidays, {name}! 🎄🎁"
        }
        
        # Tampilkan ucapan
        st.markdown(
            f"<div class='message' style='border: 2px solid {random_color()};'>"
            f"<h2>{greetings[occasion]}</h2>"
            f"<p>Semoga harimu menyenangkan!</p>"
            f"</div>",
            unsafe_allow_html=True
        )
        
        # Tampilkan gambar Hello Kitty
        kitty_images = [
            "https://i.imgur.com/3QZQZ9Q.png",
            "https://i.imgur.com/4QZQZ9Q.png",
            "https://i.imgur.com/5QZQZ9Q.png"
        ]
        st.markdown(
            f"<img src='{random.choice(kitty_images)}' class='kitty-image'>",
            unsafe_allow_html=True
        )
        
        # Confetti effect
        st.balloons()
    else:
        st.warning("Mohon masukkan nama kamu dulu ya!")

st.markdown("</div>", unsafe_allow_html=True)

# Sidebar informasi
with st.sidebar:
    st.header("🎀 Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat dengan:
    - 💖 Streamlit
    - 🎨 Custom CSS
    - 🐾 Hello Kitty theme
    
    Fitur:
    - 🌈 Warna-warni
    - 🎀 Animasi
    - 🎉 Confetti effect
    - 🖼️ Gambar Hello Kitty random
    """)
    
    st.markdown("---")
    st.markdown("Made with 💖 by [Your Name]")
