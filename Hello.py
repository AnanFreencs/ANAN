import streamlit as st
import random
from streamlit.components.v1 import html

# ========== Konfigurasi Tema ==========
def set_hello_kitty_theme():
    st.markdown("""
    <style>
    /* Background dan font */
    .stApp {
        background: linear-gradient(135deg, #ff9eb5, #ffffff, #ff9eb5);
        font-family: 'Comic Sans MS', cursive;
    }
    
    /* Judul animasi */
    @keyframes rainbow {
        0% {color: #ff69b4;}
        25% {color: #ff1493;}
        50% {color: #ff00ff;}
        75% {color: #ff1493;}
        100% {color: #ff69b4;}
    }
    
    h1 {
        animation: rainbow 2s infinite;
        text-shadow: 2px 2px #ffffff;
    }
    
    /* Tombol kustom */
    .stButton>button {
        background: #ff69b4 !important;
        color: white !important;
        border-radius: 20px !important;
        border: 2px solid white !important;
        padding: 10px 25px !important;
    }
    
    /* Efek hover tombol */
    .stButton>button:hover {
        background: #ff1493 !important;
        transform: scale(1.1);
        transition: 0.3s;
    }
    
    /* Container kartu ucapan */
    .greeting-card {
        background: white;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 10px 20px rgba(255,105,180,0.2);
        border: 3px solid #ff69b4;
        position: relative;
    }
    </style>
    """, unsafe_allow_html=True)

# ========== Fungsi Animasi ==========
def confetti():
    html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
    const count = 200;
    const defaults = {
        origin: { y: 0.7 }
    };

    function fire(particleRatio, opts) {
        confetti(Object.assign({}, defaults, opts, {
            particleCount: Math.floor(count * particleRatio)
        }));
    }

    fire(0.25, { spread: 26, startVelocity: 55 });
    fire(0.2, { spread: 60 });
    fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
    fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
    fire(0.1, { spread: 120, startVelocity: 45 });
    </script>
    """)

# ========== Main App ==========
def main():
    set_hello_kitty_theme()
    
    st.title("🎀 Hello Kitty Celebration Station! 🐱")
    
    with st.expander("🎈 Buat Ucanganmu Sendiri!"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nama Kamu:", placeholder="Masukkan nama kamu...")
            message = st.text_area("Pesan Ucapan:", height=100, 
                                 placeholder="Tulis pesan spesialmu di sini...")
            
        with col2:
            card_color = st.selectbox("Warna Kartu:", ["Pink", "Ungu", "Mint"])
            kitty_icon = st.selectbox("Pilih Hello Kitty:", ["🐱", "🎀", "👑", "🍓"])
            if st.button("Buat Kartu Ucapan!"):
                st.session_state.show_card = True
                st.balloons()
                confetti()

    if st.session_state.get('show_card'):
        st.markdown(f"""
        <div class="greeting-card" style="background: {
            '#ffb3d9' if card_color == 'Pink' else 
            '#e6b3ff' if card_color == 'Ungu' else 
            '#b3ffd9'
        };">
            <div style="text-align:center; font-size:24px;">
                {kitty_icon * 3} {name.upper() if name else "Teman Tersayang"} {kitty_icon * 3}
            </div>
            <div style="font-size:20px; padding:30px; text-align:center;">
                {message or "🎉 Selamat ya! Kamu Luar Biasa! 🎉"}
            </div>
            <div style="display: flex; justify-content: space-around; font-size:30px;">
                {'🌸🌺🌼' * 3}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Animasi tambahan
        st.markdown("""
        <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        .float-animation {
            animation: float 3s ease-in-out infinite;
            font-size: 50px;
            text-align: center;
        }
        </style>
        <div class="float-animation">
            🎀🐱🍰🎂🍩🍭
        </div>
        """, unsafe_allow_html=True)

    # Musik latar
    st.markdown("""
    <audio autoplay loop controls style="display: none;">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
