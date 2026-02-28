import streamlit as st
import tutor
import re

# --- Page Config ---
st.set_page_config(
    page_title="Swedish Tutor Agent",
    page_icon="🇸🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Color Palette (Gemini exact) ---
DARK_BG = "#131314"
SIDEBAR_BG = "#1E1E1F"
BUBBLE_BG = "#2D2D2E"
TEXT = "#E3E3E3"
MUTED = "#9AA0A6"
BORDER = "#3C3C3C"

# --- CSS ---
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

/* ── Base ── */
html, body {{
    font-family: 'Inter', sans-serif !important;
    background-color: {DARK_BG} !important;
    color: {TEXT} !important;
}}

/* ── App backgrounds ── */
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {{
    background-color: {DARK_BG} !important;
}}

/* ── Hide only decorative chrome, keep header for sidebar toggle ── */
#MainMenu {{ display: none !important; }}
footer {{ display: none !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}

/* ── Make header bar transparent but keep sidebar toggle button ── */
[data-testid="stHeader"] {{
    background-color: transparent !important;
    border-bottom: none !important;
}}

/* ── Main content ── */
.main .block-container,
[data-testid="stMainBlockContainer"] {{
    background-color: {DARK_BG} !important;
    max-width: 760px !important;
    margin: 0 auto !important;
    padding-top: 1rem !important;
    padding-bottom: 8rem !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background-color: {SIDEBAR_BG} !important;
    border-right: 1px solid {BORDER} !important;
}}
[data-testid="stSidebar"] * {{
    color: {TEXT} !important;
}}
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {{
    color: {MUTED} !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {{
    background-color: {BUBBLE_BG} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 8px !important;
    color: {TEXT} !important;
}}

/* ── Score ── */
.score-label {{
    color: {MUTED};
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
}}
.score-value {{
    font-size: 2.4rem;
    font-weight: 700;
    color: {TEXT};
    line-height: 1;
}}
.sidebar-score {{
    padding-top: 1.5rem;
    border-top: 1px solid {BORDER};
    margin-top: 1rem;
}}

/* ── User message ── */
.user-msg-container {{
    display: flex;
    justify-content: flex-end;
    margin: 6px 0 14px 0;
}}
.user-bubble {{
    background-color: {BUBBLE_BG};
    color: {TEXT};
    padding: 10px 16px;
    border-radius: 20px 20px 4px 20px;
    max-width: 72%;
    font-size: 0.94rem;
    line-height: 1.5;
    word-wrap: break-word;
}}

/* ── Welcome text ── */
.welcome-msg {{
    color: {MUTED};
    font-size: 0.95rem;
    text-align: center;
    padding-top: 30vh;
}}

/* ── Chat input ── */
[data-testid="stChatInput"] {{
    background-color: {BUBBLE_BG} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 24px !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.5) !important;
}}
[data-testid="stChatInput"] textarea {{
    background-color: transparent !important;
    color: {TEXT} !important;
    font-size: 0.94rem !important;
}}
[data-testid="stChatInput"] textarea::placeholder {{
    color: {MUTED} !important;
}}

/* ── Divider ── */
hr {{ border-color: {BORDER} !important; }}
</style>
""", unsafe_allow_html=True)

# --- App Logic Initialize ---
if 'client' not in st.session_state:
    try:
        st.session_state.client = tutor.get_client()
    except ValueError as e:
        st.error(str(e))
        st.stop()

# --- Sidebar ---
with st.sidebar:
    st.markdown(f"<h3 style='color:{TEXT}; margin-bottom:16px;'>🇸🇪 Swedish Tutor</h3>", unsafe_allow_html=True)
    st.divider()

    mode = st.radio("PRACTICE MODE", ["Correction Mode", "Quiz Mode"])

    if 'current_mode' not in st.session_state:
        st.session_state.current_mode = mode

    if st.session_state.current_mode != mode:
        st.session_state.messages = []
        st.session_state.chat = None
        st.session_state.current_mode = mode
        if mode == "Quiz Mode":
            st.session_state.quiz_started = False
            st.session_state.score = {"correct": 0, "total": 0}

    if mode == "Quiz Mode":
        st.divider()
        levels = {name: key for key, (name, _) in tutor.CEFR_LEVELS.items()}
        level_choice_name = st.selectbox("CEFR LEVEL", list(levels.keys()))
        level_key = levels[level_choice_name]

        if 'current_level_key' not in st.session_state:
            st.session_state.current_level_key = level_key

        if st.session_state.current_level_key != level_key:
            st.session_state.current_level_key = level_key
            st.session_state.messages = []
            st.session_state.chat = None
            st.session_state.quiz_started = False
            st.session_state.score = {"correct": 0, "total": 0}

        if 'score' not in st.session_state:
            st.session_state.score = {"correct": 0, "total": 0}

        st.divider()
        st.markdown(f"""
            <div class="sidebar-score">
                <div class="score-label">Score</div>
                <div class="score-value">{st.session_state.score['correct']}/{st.session_state.score['total']}</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = None
        st.session_state.score = {"correct": 0, "total": 0}
        st.rerun()

# --- Session State ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- Render messages or welcome ---
if len(st.session_state.messages) == 0:
    st.markdown("<div class='welcome-msg'>Välkommen! Choose a mode and start practicing. 🇸🇪</div>", unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="user-msg-container">
                    <div class="user-bubble">{message['content']}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([0.04, 0.96])
            with col1:
                st.markdown("🇸🇪")
            with col2:
                st.markdown(message["content"])

# --- Initialize Chat ---
if 'chat' not in st.session_state or st.session_state.chat is None:
    if mode == "Correction Mode":
        st.session_state.chat = tutor.create_correction_chat(st.session_state.client)
        if not st.session_state.messages:
            greeting = "Hej! 👋 I'm your Swedish tutor. Write anything in Swedish and I'll correct your grammar and spelling. Not sure what to write? Try introducing yourself — like *Jag heter [your name] och jag bor i Stockholm.*"
            st.session_state.messages.append({"role": "assistant", "content": greeting})
            st.rerun()
    else:
        with st.spinner("Preparing your quiz..."):
            chat, initial_question, _, _ = tutor.create_quiz_chat(st.session_state.client, st.session_state.current_level_key)
            st.session_state.chat = chat
            if not st.session_state.messages:
                st.session_state.messages.append({"role": "assistant", "content": initial_question})
            st.session_state.quiz_started = True
            st.rerun()

# --- Input ---
if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    try:
        response_text = tutor.send_message(st.session_state.chat, user_input)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        if mode == "Quiz Mode":
            match = re.search(r"Score:\s*(\d+)/(\d+)", response_text)
            if match:
                st.session_state.score["correct"] = int(match.group(1))
                st.session_state.score["total"] = int(match.group(2))
    except Exception as e:
        st.error(f"An error occurred: {e}")
    st.rerun()