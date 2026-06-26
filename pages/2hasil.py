import streamlit as st
from pathlib import Path
from fuzzyLogic import proses_fuzzy

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Hasil Rekomendasi",
    layout="wide"
)

# =====================================
# LOAD CSS
# =====================================
css_path = Path(__file__).parent.parent / "assets" / "style.css"

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================
# SESSION
# =====================================
selected = st.session_state.get("selected_fruits", [])

# =====================================
# FUZZY PROCESS
# =====================================
hasil_buah, rata_kelayakan, status_kombinasi, total_konsumsi = proses_fuzzy(selected)

# =====================================
# IMAGE PATH
# =====================================
fruit_images = {
    "Apel": "assets/apel.svg",
    "Alpukat": "assets/alpukat.svg",
    "Anggur": "assets/anggur.svg",
    "Melon": "assets/melon.svg",
    "Pir": "assets/pir.svg",
    "Pepaya": "assets/pepaya.svg",
    "Belimbing": "assets/belimbing.svg",
    "Jeruk": "assets/jeruk.svg",
    "Jambu Biji": "assets/jambu.svg",
    "Buah Naga": "assets/naga.svg",
}

# =====================================
# MAIN LAYOUT
# =====================================
left, right = st.columns([1.1, 1])

# =====================================
# LEFT SIDE
# =====================================
with left:

    st.markdown(
        f"""
        <h1 class="hasil-title">
            Kombinasi {status_kombinasi}<br><br>
            Total Porsi ± {round(total_konsumsi)} gram per hari<br>
            dibagi 3 kali sebagai selingan<br><br><br>
            Jangan makan berlebih!
        </h1>
        """,
        unsafe_allow_html=True
    )

# =====================================
# RIGHT SIDE
# =====================================
with right:

    st.markdown(
        """
        <div class="green-box">
            Rekomendasi
            <br>
            Takaran
        </div>
        """,
        unsafe_allow_html=True
    )

    # =================================
    # HASIL REKOMENDASI
    # =================================
    for item in hasil_buah:

        img = fruit_images.get(item["buah"])

        col_img, col_text = st.columns([1, 4])

        # =========================
        # IMAGE
        # =========================
        with col_img:
            st.image(img, width=85)

        # =========================
        # TEXT
        # =========================
        with col_text:

            st.markdown(
                f"""
                <div class="fruit-title"> 
                <p>{item['buah']}
                </p>
        
                </div>

                <div class="fruit-text">
                    Karbohidrat:</span>
                        {item['karbohidrat']} g
                    <br>
                    Serat:</span>
                        {item['serat']} g
                    <br>
                    Nilai Kelayakan:</span>
                        {round(item['kelayakan'], 2)}
                    <br>
                    Kategori:</span>
                        {item['kategori']}
                    <br>
                    Rekomendasi Konsumsi:</span>
                        {item['rekomendasi']} gram

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<hr>", unsafe_allow_html=True)