import streamlit as st

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

# We will render the stories in a later commit
st.info("Story rendering logic coming soon...")
