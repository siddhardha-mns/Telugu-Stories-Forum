import streamlit as st
from datetime import datetime
from typing import List, Dict, Any


class TeluguStoriesApp:
    """Main application class for Telugu Stories platform."""
    
    # Class constants
    CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం"]
    EXCERPT_LENGTH = 150
    
    def __init__(self):
        """Initialize the application."""
        self._configure_page()
        self._load_custom_styles()
        self._initialize_session_state()
    
    def _configure_page(self) -> None:
        """Configure Streamlit page settings."""
        st.set_page_config(
            page_title="తెలుగు కథలు",
            page_icon="📖",
            layout="centered",
            initial_sidebar_state="auto",
        )
    
    def _load_custom_styles(self) -> None:
        """Load custom CSS styles."""
        css = """
        <style>
            /* Import Google Fonts for Telugu and UI elements */
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700&family=Poppins:wght@400;500;700&display=swap');
            
            /* CSS Variables for consistent theming */
            :root {
                --primary-color: #E67E22;
                --secondary-color: #34495E;
                --background-color: #F8F9FA;
                --text-color: #2C3E50;
                --meta-text-color: #7F8C8D;
                --card-shadow: 0 4px 15px rgba(0,0,0,0.07);
                --border-radius: 10px;
                --transition: all 0.3s ease;
            }

            /* Base Typography */
            html, body, [class*="st-"] {
                font-family: 'Noto Sans Telugu', sans-serif;
                color: var(--text-color);
            }
            
            /* Header Styles */
            h1 {
                font-family: 'Noto Sans Telugu', sans-serif;
                font-weight: 700;
                color: var(--secondary-color) !important;
                margin-bottom: 0.5rem;
            }

            h2, h3 {
                font-family: 'Poppins', sans-serif;
                font-weight: 700;
                color: var(--secondary-color) !important;
            }

            /* Enhanced Button Styles */
            .stButton > button {
                border: 2px solid var(--primary-color);
                color: var(--primary-color);
                border-radius: 20px;
                transition: var(--transition);
                font-weight: 600;
                padding: 0.5rem 1rem;
            }
            
            .stButton > button:hover {
                background-color: var(--primary-color);
                color: white;
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(230, 126, 34, 0.3);
            }
            
            /* Story Card Styles */
            .story-card {
                background: linear-gradient(145deg, #ffffff, #f8f9fa);
                border-radius: var(--border-radius);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--card-shadow);
                border-left: 4px solid var(--primary-color);
                transition: var(--transition);
                position: relative;
                overflow: hidden;
            }
            
            .story-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 2px;
                background: linear-gradient(90deg, var(--primary-color), transparent);
            }
            
            .story-card:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.12);
            }

            /* Category Badge */
            .story-category {
                background: linear-gradient(45deg, var(--primary-color), #f39c12);
                color: white;
                padding: 0.3rem 0.8rem;
                border-radius: 20px;
                font-size: 0.75rem;
                font-weight: 600;
                display: inline-block;
                margin-bottom: 0.8rem;
                font-family: 'Poppins', sans-serif;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            /* Story Content Styles */
            .story-title {
                font-size: 1.3rem;
                font-weight: 700;
                color: var(--secondary-color);
                margin-bottom: 0.5rem;
                line-height: 1.4;
            }
            
            .story-meta {
                color: var(--meta-text-color);
                font-size: 0.85rem;
                margin-bottom: 1rem;
                font-family: 'Poppins', sans-serif;
            }
            
            .story-excerpt {
                line-height: 1.6;
                color: var(--text-color);
                margin-bottom: 1rem;
            }
            
            /* Action Buttons */
            .story-actions {
                display: flex;
                gap: 0.5rem;
                flex-wrap: wrap;
            }
            
            .story-actions button {
                font-size: 0.8rem !important;
                padding: 0.3rem 0.6rem !important;
                border-radius: 15px !important;
            }
            
            /* Sidebar Enhancements */
            .sidebar-section {
                background: white;
                border-radius: var(--border-radius);
                padding: 1rem;
                margin-bottom: 1rem;
                box-shadow: var(--card-shadow);
            }
            
            /* Footer */
            .footer {
                text-align: center;
                color: var(--meta-text-color);
                font-size: 0.85rem;
                margin-top: 2rem;
                padding-top: 1rem;
                border-top: 1px solid #e0e0e0;
            }
            
            /* Form Enhancements */
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea,
            .stSelectbox > div > div > select {
                border-radius: 8px;
                border-color: #ddd;
                font-family: 'Noto Sans Telugu', sans-serif;
            }
            
            /* Dialog Enhancements */
            .stDialog {
                border-radius: var(--border-radius);
            }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    
    def _initialize_session_state(self) -> None:
        """Initialize session state with default data."""
        if 'stories' not in st.session_state:
            st.session_state.stories = self._get_default_stories()
        
        if 'show_form' not in st.session_state:
            st.session_state.show_form = False
    
    def _get_default_stories(self) -> List[Dict[str, Any]]:
        """Return default stories data."""
        return [
            {
                "title": "పల్లెటూరి ప్రయాణం",
                "author": "రవి కుమార్",
                "timestamp": "5 గంటల క్రితం",
                "category": "కథ",
                "excerpt": "ఒకానొక పల్లెటూరిలో రాము అనే ఒక యువకుడు ఉండేవాడు. అతను తన ఊరిని విడిచి పట్టణం వెళ్లాలని కలలు కనేవాడు. అతని కలలు, కష్టాలు, మరియు విజయాల గురించిన ఈ కథ...",
                "upvotes": 125,
                "comments": 32,
                "created_at": datetime.now().isoformat()
            },
            {
                "title": "కాకతీయుల వైభవం",
                "author": "సుమలత",
                "timestamp": "2 రోజుల క్రితం",
                "category": "చరిత్ర",
                "excerpt": "కాకతీయ సామ్రాజ్యం తెలుగు నేల స్వర్ణయుగాలలో ఒకటి. వారి పరిపాలన, కళలు, మరియు శిల్పకళ గురించి తెలుసుకుందాం. రుద్రమ దేవి, కాకతీయ కళాత్మక వైభవం...",
                "upvotes": 250,
                "comments": 78,
                "created_at": datetime.now().isoformat()
            }
        ]
    
    def _validate_story_data(self, title: str, author: str, content: str) -> tuple[bool, str]:
        """Validate story form data."""
        if not title.strip():
            return False, "శీర్షిక తప్పనిసరి"
        if not author.strip():
            return False, "రచయిత పేరు తప్పనిసరి"
        if not content.strip():
            return False, "కథ/రచన తప్పనిసరి"
        if len(title.strip()) < 3:
            return False, "శీర్షిక కనీసం 3 అక్షరాలు ఉండాలి"
        if len(content.strip()) < 50:
            return False, "కథ/రచన కనీసం 50 అక్షరాలు ఉండాలి"
        return True, ""
    
    def _create_story_excerpt(self, content: str) -> str:
        """Create excerpt from story content."""
        if len(content) <= self.EXCERPT_LENGTH:
            return content
        return content[:self.EXCERPT_LENGTH].rsplit(' ', 1)[0] + "..."
    
    def _add_new_story(self, title: str, author: str, category: str, content: str) -> None:
        """Add a new story to the session state."""
        new_story = {
            "title": title.strip(),
            "author": author.strip(),
            "timestamp": "ఇప్పుడే",
            "category": category,
            "excerpt": self._create_story_excerpt(content.strip()),
            "upvotes": 0,
            "comments": 0,
            "created_at": datetime.now().isoformat()
        }
        st.session_state.stories.insert(0, new_story)
    
    def _render_story_card(self, story: Dict[str, Any], index: int) -> None:
        """Render a single story card."""
        # Story card container
        st.markdown('<div class="story-card">', unsafe_allow_html=True)
        
        # Category badge
        st.markdown(
            f'<div class="story-category">{story["category"]}</div>',
            unsafe_allow_html=True
        )
        
        # Story title
        st.markdown(
            f'<div class="story-title">{story["title"]}</div>',
            unsafe_allow_html=True
        )
        
        # Story metadata
        st.markdown(
            f'<div class="story-meta">రచయిత: {story["author"]} • {story["timestamp"]}</div>',
            unsafe_allow_html=True
        )
        
        # Story excerpt
        st.markdown(
            f'<div class="story-excerpt">{story["excerpt"]}</div>',
            unsafe_allow_html=True
        )
        
        # Action buttons
        action_cols = st.columns([1, 1, 2, 2])
        with action_cols[0]:
            if st.button(f"👍 {story['upvotes']}", key=f"up_{index}"):
                st.session_state.stories[index]['upvotes'] += 1
                st.rerun()
        
        with action_cols[1]:
            if st.button("👎", key=f"down_{index}"):
                if st.session_state.stories[index]['upvotes'] > 0:
                    st.session_state.stories[index]['upvotes'] -= 1
                    st.rerun()
        
        with action_cols[2]:
            st.button(f"💬 {story['comments']} వ్యాఖ్యలు", key=f"comm_{index}")
        
        with action_cols[3]:
            st.button("📤 భాగస్వామ్యం", key=f"share_{index}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    def _render_header(self) -> None:
        """Render the application header."""
        st.title("📖 తెలుగు కథలు")
        st.markdown("**పంచుకోండి, చదవండి, చర్చించండి** - తెలుగు సాహిత్య వేదిక")
        st.markdown("---")
    
    def _render_story_form(self) -> None:
        """Render the story submission form."""
        if st.button("✍️ కొత్త కథను జోడించండి", type="primary"):
            st.session_state.show_form = True
        
        if st.session_state.show_form:
            @st.dialog("మీ కథను పంచుకోండి")
            def show_story_form():
                st.markdown("**మీ రచనను తెలుగు సాహిత్య ప్రేమికులతో పంచుకోండి**")
                
                with st.form("story_form", clear_on_submit=True):
                    title = st.text_input(
                        "శీర్షిక *",
                        placeholder="మీ కథకు ఆకర్షణీయమైన శీర్షిక",
                        help="కథను బాగా వివరించే శీర్షిక ఇవ్వండి"
                    )
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        category = st.selectbox("విభాగం *", self.CATEGORIES, index=0)
                    with col2:
                        author = st.text_input("రచయిత పేరు *", placeholder="మీ పేరు")
                    
                    content = st.text_area(
                        "మీ కథ / రచన *",
                        height=300,
                        placeholder="ఇక్కడ మీ రచనను టైప్ చేయండి...\n\nఉదాహరణ:\nఒకానొక కాలంలో... మీ కథ ప్రారంభించండి",
                        help="కనీసం 50 అక్షరాలు రాయండి"
                    )
                    
                    submit_col1, submit_col2 = st.columns(2)
                    with submit_col1:
                        submitted = st.form_submit_button("📤 ప్రచురించండి", type="primary")
                    with submit_col2:
                        cancelled = st.form_submit_button("❌ రద్దు చేయండి")
                    
                    if cancelled:
                        st.session_state.show_form = False
                        st.rerun()
                    
                    if submitted:
                        is_valid, error_msg = self._validate_story_data(title, author, content)
                        
                        if not is_valid:
                            st.error(f"❌ {error_msg}")
                        else:
                            self._add_new_story(title, author, category, content)
                            st.session_state.show_form = False
                            st.success("🎉 మీ కథ విజయవంతంగా ప్రచురించబడింది!")
                            st.balloons()
                            st.rerun()
            
            show_story_form()
    
    def _render_sidebar(self) -> None:
        """Render the application sidebar."""
        st.header("📚 విభాగాలు")
        
        # Categories navigation
        for category in self.CATEGORIES:
            icon_map = {
                "కథ": "📖",
                "చరిత్ర": "📜", 
                "సంస్కృతి": "🎭",
                "కవిత": "🌸",
                "విజ్ఞానం": "🧠"
            }
            icon = icon_map.get(category, "📄")
            st.page_link("app.py", label=f"{icon} {category}", icon=icon)
        
        st.markdown("---")
        
        # Statistics
        st.header("📊 గణాంకాలు")
        total_stories = len(st.session_state.stories)
        total_upvotes = sum(story['upvotes'] for story in st.session_state.stories)
        st.metric("మొత్తం కథలు", total_stories)
        st.metric("మొత్తం ఇష్టాలు", total_upvotes)
        
        st.markdown("---")
        
        # Guidelines
        st.info(
            """
            **📋 వేదిక నియమాలు:**
            
            • ఒకరినొకరు గౌరవించుకోండి
            • అసభ్య భాష వాడకండి  
            • ఇతరుల రచనలను దొంగిలించకండి
            • నాణ్యమైన కంటెంట్ పంచుకోండి
            
            *ఇది మన తెలుగు భాషా సంస్కృతుల వేదిక* 🙏
            """,
            icon="⚖️"
        )
    
    def _render_main_feed(self) -> None:
        """Render the main stories feed."""
        st.header("🔥 తాజా కథలు")
        
        if not st.session_state.stories:
            st.info("📝 ప్రస్తుతానికి కథలు ఏమీ లేవు. మీరే మొదటి కథను జోడించండి!", icon="💡")
            return
        
        # Filter options
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            selected_category = st.selectbox(
                "విభాగం ఫిల్టర్",
                ["అన్నీ"] + self.CATEGORIES,
                key="category_filter"
            )
        
        with filter_col2:
            sort_option = st.selectbox(
                "క్రమబద్ధీకరణ",
                ["తాజావి", "అత్యధిక ఇష్టాలు", "అత్యధిక వ్యాఖ్యలు"],
                key="sort_option"
            )
        
        # Filter and sort stories
        filtered_stories = st.session_state.stories
        if selected_category != "అన్నీ":
            filtered_stories = [s for s in filtered_stories if s['category'] == selected_category]
        
        # Sort stories
        if sort_option == "అత్యధిక ఇష్టాలు":
            filtered_stories = sorted(filtered_stories, key=lambda x: x['upvotes'], reverse=True)
        elif sort_option == "అత్యధిక వ్యాఖ్యలు":
            filtered_stories = sorted(filtered_stories, key=lambda x: x['comments'], reverse=True)
        
        # Display stories
        for i, story in enumerate(filtered_stories):
            self._render_story_card(story, i)
        
        if not filtered_stories:
            st.info(f"'{selected_category}' విభాగంలో కథలు లేవు.", icon="🔍")
    
    def _render_footer(self) -> None:
        """Render the application footer."""
        st.markdown("---")
        st.markdown(
            """
            <div class="footer">
                © 2025 తెలుగు కథలు • తెలుగు సాహిత్య వేదిక • 
                <a href="#" style="color: var(--primary-color);">గోప్యతా విధానం</a> • 
                <a href="#" style="color: var(--primary-color);">సంప్రదింపులు</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def run(self) -> None:
        """Run the main application."""
        # Header
        self._render_header()
        
        # Story submission form
        self._render_story_form()
        
        # Main layout
        main_col, sidebar_col = st.columns([3, 1.2])
        
        with main_col:
            self._render_main_feed()
        
        with sidebar_col:
            self._render_sidebar()
        
        # Footer
        self._render_footer()


# Application entry point
def main():
    """Main function to run the Telugu Stories application."""
    app = TeluguStoriesApp()
    app.run()


if __name__ == "__main__":
    main()
