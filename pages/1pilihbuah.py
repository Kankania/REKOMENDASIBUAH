import streamlit as st

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Pilih Buah",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# LOAD CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================
# SESSION STATE
# =====================================
if "selected_fruits" not in st.session_state:
    st.session_state.selected_fruits = []

# =====================================
# DATA
# =====================================
fruits = [
    {"name": "Apel", "img": "assets/apel.svg"},
    {"name": "Alpukat", "img": "assets/alpukat.svg"},
    {"name": "Anggur", "img": "assets/anggur.svg"},
    {"name": "Belimbing", "img": "assets/belimbing.svg"},
    {"name": "Pir", "img": "assets/pir.svg"},
    {"name": "Pepaya", "img": "assets/pepaya.svg"},
    {"name": "Melon", "img": "assets/melon.svg"},
    {"name": "Jeruk", "img": "assets/jeruk.svg"},
    {"name": "Jambu Biji", "img": "assets/jambu.svg"},
    {"name": "Buah Naga", "img": "assets/naga.svg"},
]

# =====================================
# SELECT FUNCTION
# =====================================
def select_fruit(name):
    if name in st.session_state.selected_fruits:
        st.session_state.selected_fruits.remove(name)
    else:
        if len(st.session_state.selected_fruits) < 5:
            st.session_state.selected_fruits.append(name)
        else:
            st.warning("Maksimal 5 buah!")

# =====================================
# CENTER CONTAINER
# =====================================
st.markdown('<div class="page-container">', unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================
st.markdown("""
<div class="page-title">
    Buah apa yang anda punya hari ini?
</div>
""", unsafe_allow_html=True)

# =====================================
# GRID WRAPPER CENTER
# =====================================
st.markdown('<div class="fruit-grid">', unsafe_allow_html=True)

selected = st.session_state.selected_fruits

for i in range(0, len(fruits), 5):
    cols = st.columns(5, gap="small")

    for j in range(5):
        if i + j < len(fruits):
            fruit = fruits[i + j]

            with cols[j]:
                st.markdown('<div class="fruit-card">', unsafe_allow_html=True)

                st.image(fruit["img"], width=100)

                if st.button(fruit["name"], key=f"btn_{fruit['name']}"):
                    select_fruit(fruit["name"])

                st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# SELECTED BOX
# =====================================
st.markdown('<div class="selected-wrapper">', unsafe_allow_html=True)

selected = st.session_state.selected_fruits

if selected:
    cols = st.columns(5)

    for idx, fruit_name in enumerate(selected):
        for fruit in fruits:
            if fruit["name"] == fruit_name:
                cols[idx % 5].image(fruit["img"], width=80)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# PROSES BUTTON
# =====================================
st.write("")

col1, col2 = st.columns([8, 1])

with col2:
    if st.button("Proses", type="primary", use_container_width=True):
        if len(selected) == 0:
            st.warning("Pilih buah terlebih dahulu")
        elif len(selected) == 1:
            st.warning("Pilih minimal 2 buah")
        else:
            st.switch_page("pages/2hasil.py")

st.markdown('</div>', unsafe_allow_html=True)