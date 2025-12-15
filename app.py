import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Whimsical Fantasy Character Creator",
    page_icon="🧙",
    layout="wide"
)

st.title("🧙 Whimsical Fantasy Character Creator")
st.caption("Classroom-friendly • No logins • Just for fun")

# -----------------------------
# Session state (cloud-safe)
# -----------------------------
if "character" not in st.session_state:
    st.session_state.character = {
        "base": "🧙 Wizard",
        "outfit": "✨ Star Robe",
        "companion": "🐌 Snail Friend",
        "background": "🌈 Candy Meadow"
    }

# -----------------------------
# Options (whimsical)
# -----------------------------
BASES = [
    "🧙 Wizard",
    "🧝 Elf",
    "🧚 Fairy",
    "🦊 Foxfolk",
    "🐸 Frog Knight",
]

OUTFITS = [
    "✨ Star Robe",
    "🍄 Mushroom Cloak",
    "🌈 Rainbow Hoodie",
    "🍃 Leaf Tunic",
    "🧥 Cozy Overalls",
]

COMPANIONS = [
    "🐌 Snail Friend",
    "🐉 Tiny Dragon",
    "📘 Floating Book",
    "🐝 Buzzing Bee",
    "🦄 Pocket Unicorn",
]

BACKGROUNDS = [
    "🌈 Candy Meadow",
    "🍵 Teacup Village",
    "☁️ Cloud Bridge",
    "📚 Floating Library",
    "🍄 Glowshroom Cave",
]

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([1, 1.2])

# -----------------------------
# Preview panel
# -----------------------------
with left:
    st.subheader("✨ Character Preview")

    char = st.session_state.character

    st.markdown(
        f"""
        <div style="
            border-radius:20px;
            padding:20px;
            background:#ffffff;
            border:2px solid #e2e8f0;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,.08);
        ">
            <div style="font-size:64px;">{char["base"].split()[0]}</div>
            <div style="font-size:18px;"><b>{char["base"]}</b></div>
            <div style="margin-top:8px;">{char["outfit"]}</div>
            <div>{char["companion"]}</div>
            <div style="margin-top:10px; font-size:14px; opacity:.8;">
                Background: {char["background"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.caption("Tip: This resets when the page refreshes — perfect for reward time or stations.")

# -----------------------------
# Customization panel
# -----------------------------
with right:
    st.subheader("🎒 Customize Your Character")

    st.session_state.character["base"] = st.selectbox(
        "Choose your character",
        BASES,
        index=BASES.index(st.session_state.character["base"])
    )

    st.session_state.character["outfit"] = st.selectbox(
        "Choose an outfit",
        OUTFITS,
        index=OUTFITS.index(st.session_state.character["outfit"])
    )

    st.session_state.character["companion"] = st.selectbox(
        "Choose a companion",
        COMPANIONS,
        index=COMPANIONS.index(st.session_state.character["companion"])
    )

    st.session_state.character["background"] = st.selectbox(
        "Choose a background",
        BACKGROUNDS,
        index=BACKGROUNDS.index(st.session_state.character["background"])
    )

    st.divider()

    if st.button("🎲 Randomize!", use_container_width=True):
        import random
        st.session_state.character = {
            "base": random.choice(BASES),
            "outfit": random.choice(OUTFITS),
            "companion": random.choice(COMPANIONS),
            "background": random.choice(BACKGROUNDS),
        }
        st.rerun()

    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.character = {
            "base": BASES[0],
            "outfit": OUTFITS[0],
            "companion": COMPANIONS[0],
            "background": BACKGROUNDS[0],
        }
        st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Built for classroom creativity • No accounts • No pressure • All joy ✨")
