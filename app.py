 import streamlit as st


def load_css():
    st.markdown("""
        <style>
        /* All the CSS from the previous answer goes here */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700&family=Poppins:wght@400;500;700&display=swap');
        html, body, [class*="st-"] { font-family: 'Noto Sans Telugu', sans-serif; }
        h1, h2, h3 { font-family: 'Poppins', sans-serif; }
        .st-emotion-cache-1v0mbdj > button { border-color: #E67E22; color: #E67E22; } /* Example */
        </style>
    """, unsafe_allow_html=True)


load_css()
st.set_page_config(
    page_title="తెలుగు కథలు",
    page_icon="📖",
    layout="centered"
)

# --- Initial Data and Session State ---
if 'stories' not in st.session_state:
    st.session_state.stories = [
        {
            "title": "పల్లెటూరి ప్రయాణం",
            "author": "రవి కుమార్",
            "timestamp": "5 గంటల క్రితం",
            "category": "కథ",
            "excerpt": "ఒకానొక పల్లెటూరిలో రాము అనే ఒక యువకుడు ఉండేవాడు. అతను తన ఊరిని విడిచి పట్నం వెళ్లాలని కలలు కనేవాడు...",
            "upvotes": 125,
            "comments": 32
        },
        {
            "title": "కాకతీయుల వైభవం",
            "author": "సుమలత",
            "timestamp": "2 రోజుల క్రితం",
            "category": "చరిత్ర",
            "excerpt": "కాకతీయ సామ్రాజ్యం తెలుగు నేల స్వర్ణయుగాలలో ఒకటి. వారి పరిపాలన, కళలు, మరియు శిల్పకళ గురించి తెలుసుకుందాం...",
            "upvotes": 250,
            "comments": 78
        }
    ]

st.title("📖 తెలుగు కథలు")
st.markdown("పంచుకోండి, చదవండి, చర్చించండి.")
st.markdown("---")
st.header("తాజా కథలు")

# --- Helper Function to Display a Story Card ---
def display_story_card(story, index):
    with st.container(border=True):
        st.subheader(story['title'])
        st.caption(f'రచయిత: {story["author"]} • {story["timestamp"]}')
        st.write(story['excerpt'])
        actions = st.columns(4)
        actions[0].button(f"👍 {story['upvotes']}", key=f"up_{index}")
        actions[1].button(f"💬 {story['comments']}", key=f"comm_{index}")

st.title("📖 తెలుగు కథలు")
st.markdown("పంచుకోండి, చదవండి, చర్చించండి.")
st.markdown("---")
st.header("తాజా కథలు")

for i, story in enumerate(st.session_state.stories):
    display_story_card(story, i)


st.title("📖 తెలుగు కథలు")
st.markdown("పంచుకోండి, చదవండి, చర్చించండి.")

# --- Submit Story Dialog ---
if "show_form" not in st.session_state:
    st.session_state.show_form = False

if st.button("✍️ కొత్త కథను జోడించండి"):
    st.session_state.show_form = True

if st.session_state.show_form:
    with st.dialog("మీ కథను పంచుకోండి", on_dismiss=lambda: setattr(st.session_state, 'show_form', False)):
        with st.form("story_form"):
            title = st.text_input("శీర్షిక")
            author = st.text_input("రచయిత పేరు")
            content = st.text_area("మీ కథ / రచన", height=250)
            submitted = st.form_submit_button("ప్రచురించండి")
            if submitted:
                new_story = {
                    "title": title, "author": author, "timestamp": "ఇప్పుడే",
                    "category": "కథ", "excerpt": content[:150] + "...",
                    "upvotes": 0, "comments": 0
                }
                st.session_state.stories.insert(0, new_story)
                st.session_state.show_form = False
                st.success("మీ కథ విజయవంతంగా ప్రచురించబడింది!")
                st.rerun()

st.markdown("---")
feed_col, sidebar_col = st.columns([3, 1.2])

with feed_col:
    st.header("తాజా కథలు")
    for i, story in enumerate(st.session_state.stories):
        display_story_card(story, i)

with sidebar_col:
    with st.container(border=True):
        st.header("విభాగాలు")
        st.write("📜 చరిత్ర")
        st.write("📖 కథలు & కవితలు")
        st.write("🎭 సంస్కృతి")
    st.info("వేదిక నియమాలు: ఒకరినొకరు గౌరవించుకోండి.", icon="⚖️")
