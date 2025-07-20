import streamlit as st

# --- Page Configuration (MUST be the first Streamlit command) ---
st.set_page_config(
    page_title="తెలుగు కథలు",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Custom CSS for Styling ---
# This function injects custom CSS to style the app.
def load_css():
    st.markdown("""
        <style>
            /* Import Google Fonts for Telugu and UI elements */
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700&family=Poppins:wght@400;500;700&display=swap');
            
            /* --- Global Style Variables --- */
            :root {
                --primary-color: #E67E22;
                --secondary-color: #34495E;
                --background-color: #F8F9FA;
                --text-color: #2C3E50;
                --meta-text-color: #7F8C8D;
            }

            /* --- Base Font Styles --- */
            html, body, [class*="st-"] {
                font-family: 'Noto Sans Telugu', sans-serif;
                color: var(--text-color);
            }
            
            /* --- Title and Header Styles --- */
            h1 {
                font-family: 'Noto Sans Telugu', sans-serif;
                font-weight: 700;
                color: var(--secondary-color) !important;
            }

            h2, h3 {
                font-family: 'Poppins', sans-serif;
                font-weight: 700;
                color: var(--secondary-color) !important;
            }

            /* --- Custom Button for 'Add Story' --- */
            .stButton > button {
                border-color: var(--primary-color);
                color: var(--primary-color);
                border-radius: 20px;
                transition: all 0.3s;
                font-weight: bold;
            }
            .stButton > button:hover {
                background-color: var(--primary-color);
                color: white;
                border-color: var(--primary-color);
                transform: scale(1.05);
            }
            
            /* --- Story Card Customizations --- */
            .story-card {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.07);
                border-left: 5px solid var(--primary-color);
            }

            .story-category {
                background-color: rgba(230, 126, 34, 0.1);
                color: var(--primary-color);
                padding: 3px 10px;
                border-radius: 15px;
                font-size: 0.8rem;
                font-weight: bold;
                display: inline-block;
                margin-bottom: 10px;
                font-family: 'Poppins', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)

# Apply the custom CSS
load_css()

# --- Initial Data and Session State ---
# This dictionary will hold our stories. In a real app, this would come from a database.
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

# --- Helper Function to Display a Story Card ---
# This function is defined once and used in the main feed.
def display_story_card(story, index):
    # Using markdown to inject our custom class for styling
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    
    st.markdown(f'<div class="story-category">{story["category"]}</div>', unsafe_allow_html=True)
    st.subheader(story['title'])
    st.caption(f'రచయిత: {story["author"]} • {story["timestamp"]}')
    st.write(story['excerpt'])

    # Action buttons
    actions = st.columns([1, 1, 2, 2])
    actions[0].button(f"👍 {story['upvotes']}", key=f"up_{index}", use_container_width=True)
    actions[1].button("👎", key=f"down_{index}", use_container_width=True)
    actions[2].button(f"💬 {story['comments']} వ్యాఖ్యలు", key=f"comm_{index}", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# --- Main App UI ---

# 1. Header Section
st.title("📖 తెలుగు కథలు")
st.markdown("పంచుకోండి, చదవండి, చర్చించండి.")

# 2. Submit Story Dialog Logic
if "show_form" not in st.session_state:
    st.session_state.show_form = False

if st.button("✍️ కొత్త కథను జోడించండి"):
    st.session_state.show_form = True

if st.session_state.show_form:
    with st.dialog("మీ కథను పంచుకోండి", on_dismiss=lambda: setattr(st.session_state, 'show_form', False)):
        with st.form("story_form"):
            title = st.text_input("శీర్షిక", placeholder="మీ కథ శీర్షిక")
            category = st.selectbox("విభాగం", ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం"])
            author = st.text_input("రచయిత పేరు", placeholder="మీ పేరు")
            content = st.text_area("మీ కథ / రచన", height=250, placeholder="ఇక్కడ మీ రచనను టైప్ చేయండి...")
            
            submitted = st.form_submit_button("ప్రచురించండి")

            if submitted:
                if not title or not content or not author:
                    st.error("దయచేసి అన్ని వివరాలు నింపండి.")
                else:
                    new_story = {
                        "title": title,
                        "author": author,
                        "timestamp": "ఇప్పుడే",
                        "category": category,
                        "excerpt": content[:150] + "...",
                        "upvotes": 0,
                        "comments": 0
                    }
                    st.session_state.stories.insert(0, new_story)
                    st.session_state.show_form = False
                    st.success("మీ కథ విజయవంతంగా ప్రచురించబడింది!")
                    st.rerun()

# 3. Main Layout with Feed and Sidebar
st.markdown("---")
feed_col, sidebar_col = st.columns([3, 1.2])

with feed_col:
    st.header("తాజా కథలు")
    if not st.session_state.stories:
        st.info("ప్రస్తుతానికి కథలు ఏమీ లేవు. మీరే మొదటి కథను జోడించండి!")
    else:
        # Loop to display all stories
        for i, story in enumerate(st.session_state.stories):
            display_story_card(story, i)

with sidebar_col:
    with st.container(border=True):
        st.header("విభాగాలు")
        st.page_link("app.py", label="📜 చరిత్ర", icon="📜")
        st.page_link("app.py", label="📖 కథలు & కవితలు", icon="📖")
        st.page_link("app.py", label="🎭 సంస్కృతి", icon="🎭")
        st.page_link("app.py", label="🧠 విజ్ఞానం", icon="🧠")
    
    st.info("**వేదిక నియమాలు:** దయచేసి ఒకరినొకరు గౌరవించుకోండి. ఇది మన తెలుగు భాషా సంస్కృతుల వేదిక.", icon="⚖️")

# 4. Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: var(--meta-text-color);'>&copy; 2025 తెలుగు కథలు. అన్ని హక్కులు ప్రత్యేకించబడినవి.</div>", unsafe_allow_html=True)
