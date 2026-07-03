import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="CURTAIN OF TIME", page_icon="🎭", layout="centered")

# -----------------------------
# THEME (CSS)
# -----------------------------
st.markdown("""
<style>
    body {
        background-color: #0b1a3a;
    }
    .main {
        background-color: #0b1a3a;
    }
    .title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        color: #d7e3ff;
        letter-spacing: 2px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #b8c7e6;
        margin-bottom: 30px;
    }
    .card {
        background: rgba(255,255,255,0.06);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        color: #e6ecff;
        box-shadow: 0 0 25px rgba(120,150,255,0.15);
    }
    .center {
        text-align: center;
    }
    .stButton>button {
        background-color: #cfd8ff;
        color: #0b1a3a;
        border-radius: 12px;
        padding: 0.5em 1em;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        color: #0b1a3a;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "scene" not in st.session_state:
    st.session_state.scene = "TITLE"

# -----------------------------
# HELPERS
# -----------------------------
def set_scene(scene):
    st.session_state.scene = scene
    st.rerun()

def restart():
    st.session_state.scene = "TITLE"
    st.rerun()

def type_text(text, delay=0.02):
    """Simple text animation"""
    placeholder = st.empty()
    out = ""
    for char in text:
        out += char
        placeholder.markdown(f"<div class='card'>{out}</div>", unsafe_allow_html=True)
        time.sleep(delay)

# -----------------------------
# TITLE SCREEN
# -----------------------------
def title_screen():
    st.markdown("<div class='title'>CURTAIN OF TIME</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A story of rhythm, time, and memory 🎭✨</div>", unsafe_allow_html=True)

    st.markdown("<div class='card center'>", unsafe_allow_html=True)
    st.write("Welcome to Baobao's journey through time and mystery.")
    if st.button("Start Game 🎭"):
        set_scene("INTRO")
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# INTRO
# -----------------------------
def intro():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🎭 Baobao is performing in the National School Dance Championship...")
    st.write("The stage lights shine like silver stars across the hall.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Start Performance ✨"):
        set_scene("TRANSITION")

# -----------------------------
# TRANSITION
# -----------------------------
def transition():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🌀 A strange glow appears beneath Baobao’s feet...")
    st.write("The world fades into silver light...")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Wake Up 🌙"):
        set_scene("ANCIENT")

# -----------------------------
# ANCIENT WORLD HUB
# -----------------------------
def ancient_world():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🏛️ Baobao wakes up in an ancient ruined world.")
    st.write("Wind whispers through broken pillars covered in glowing symbols.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Explore Ruins 🏛️"):
        set_scene("RUINS")

    if st.button("Talk to Guardian NPC 🌙"):
        set_scene("NPC")

    if st.button("Find Portal ✨"):
        set_scene("PORTAL")

# -----------------------------
# NPC SCENE
# -----------------------------
def npc_scene():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🌙 Keeper Arin appears before Baobao...")
    st.write("")
    st.write("“You do not belong here, child of rhythm.”")
    st.write("“Only the lost melody can open the portal.”")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Go Back 🔙"):
        set_scene("ANCIENT")

# -----------------------------
# RUINS
# -----------------------------
def ruins():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🏛️ You find ancient glowing symbols carved into stone.")
    st.write("They pulse faintly, as if remembering music long forgotten.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Return 🔙"):
        set_scene("ANCIENT")

# -----------------------------
# PORTAL
# -----------------------------
def portal():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("✨ A glowing silver-blue portal appears...")
    st.write("It hums softly like a distant song.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Enter Portal 🌌"):
        set_scene("ENDING")

# -----------------------------
# ENDING
# -----------------------------
def ending():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("🎭 Baobao returns to the stage...")
    st.write("But something feels different.")
    st.write("")
    st.markdown("### ✨ TO BE CONTINUED ✨")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Restart Game 🔁"):
        restart()

# -----------------------------
# ROUTER
# -----------------------------
if st.session_state.scene == "TITLE":
    title_screen()
elif st.session_state.scene == "INTRO":
    intro()
elif st.session_state.scene == "TRANSITION":
    transition()
elif st.session_state.scene == "ANCIENT":
    ancient_world()
elif st.session_state.scene == "NPC":
    npc_scene()
elif st.session_state.scene == "RUINS":
    ruins()
elif st.session_state.scene == "PORTAL":
    portal()
elif st.session_state.scene == "ENDING":
    ending()
