import streamlit as st
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import uuid
import json


class TeluguStoriesApp:
    """Main application class for Telugu Stories platform."""
    
    # Class constants
    CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం", "ఇతర"]
    EXCERPT_LENGTH = 150
    MIN_TITLE_LENGTH = 3
    MIN_CONTENT_LENGTH = 50
    
    def __init__(self):
        """Initialize the application."""
        self._configure_page()
        self._load_custom_styles()
        self._initialize_session_state()
    
    def _configure_page(self) -> None:
        """Configure Streamlit page settings."""
        st.set_page_config(
            page_title="తెలుగు కథలు - Telugu Stories",
            page_icon="📖",
            layout="centered",
            initial_sidebar_state="auto",
            menu_items={
                'Get Help': 'mailto:support@telugukathas.com',
                'Report a bug': 'mailto:bugs@telugukathas.com',
                'About': "# తెలుగు కథలు\nతెలుగు సాహిత్య ప్రేమికుల వేదిక"
            }
        )
    
    def _load_custom_styles(self) -> None:
        """Load custom CSS styles."""
        css = """
        <style>
            /* Import Google Fonts for Telugu and UI elements */
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;600;700;900&family=Poppins:wght@300;400;500;600;700;800&display=swap');
            
            /* CSS Variables for consistent theming */
            :root {
                --primary-color: #FF6B35;
                --primary-light: #FF8A65;
                --primary-dark: #E64A19;
                --secondary-color: #2C3E50;
                --accent-color: #9C27B0;
                --success-color: #4CAF50;
                --warning-color: #FF9800;
                --error-color: #f44336;
                --background-primary: #0F1419;
                --background-secondary: #1A202C;
                --card-bg: #2D3748;
                --text-primary: #FFFFFF;
                --text-secondary: #A0AEC0;
                --text-muted: #718096;
                --gradient-primary: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FFD23F 100%);
                --gradient-secondary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                --card-shadow: 0 10px 30px rgba(0,0,0,0.3);
                --card-shadow-hover: 0 20px 40px rgba(0,0,0,0.4);
                --border-radius: 16px;
                --border-radius-large: 24px;
                --transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
                --glow-primary: 0 0 20px rgba(255, 107, 53, 0.5);
                --glow-accent: 0 0 15px rgba(156, 39, 176, 0.4);
            }

            /* Dark Theme Base */
            .stApp {
                background: var(--background-primary);
                background-image: 
                    radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 107, 53, 0.2) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(156, 39, 176, 0.1) 0%, transparent 50%);
                background-attachment: fixed;
            }

            /* Base Typography with High Contrast */
            html, body, [class*="st-"], p, div, span {
                font-family: 'Noto Sans Telugu', sans-serif;
                color: var(--text-primary) !important;
                font-weight: 500;
                line-height: 1.7;
                text-shadow: 0 1px 3px rgba(0,0,0,0.3);
            }
            
            /* Enhanced Header Styles with Glow Effects */
            h1 {
                font-family: 'Noto Sans Telugu', sans-serif;
                font-weight: 900 !important;
                color: var(--text-primary) !important;
                margin-bottom: 1rem;
                background: var(--gradient-primary);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem !important;
                text-align: center;
                filter: drop-shadow(var(--glow-primary));
                animation: titleGlow 3s ease-in-out infinite alternate;
            }

            @keyframes titleGlow {
                0% { filter: drop-shadow(0 0 10px rgba(255, 107, 53, 0.3)); }
                100% { filter: drop-shadow(0 0 25px rgba(255, 107, 53, 0.8)); }
            }

            h2, h3 {
                font-family: 'Poppins', sans-serif;
                font-weight: 700 !important;
                color: var(--text-primary) !important;
                background: var(--gradient-secondary);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
            }

            /* Enhanced Button Styles with Neon Effects */
            .stButton > button {
                background: var(--gradient-primary) !important;
                border: none !important;
                color: white !important;
                border-radius: var(--border-radius) !important;
                transition: var(--transition) !important;
                font-weight: 700 !important;
                padding: 1rem 2rem !important;
                font-size: 1.1rem !important;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: var(--card-shadow);
                position: relative;
                overflow: hidden;
            }
            
            .stButton > button::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
                transition: left 0.6s;
            }
            
            .stButton > button:hover {
                transform: translateY(-3px) scale(1.02) !important;
                box-shadow: var(--card-shadow-hover), var(--glow-primary) !important;
                filter: brightness(1.1);
            }
            
            .stButton > button:hover::before {
                left: 100%;
            }
            
            /* Story Card Styles with Glass Morphism */
            .story-card {
                background: rgba(45, 55, 72, 0.95);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: var(--border-radius-large);
                padding: 2rem;
                margin-bottom: 2rem;
                box-shadow: var(--card-shadow);
                position: relative;
                overflow: hidden;
                transition: var(--transition);
                border-left: 4px solid transparent;
                border-image: var(--gradient-primary) 1;
            }
            
            .story-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: var(--gradient-primary);
                border-radius: var(--border-radius-large) var(--border-radius-large) 0 0;
            }
            
            .story-card::after {
                content: '';
                position: absolute;
                top: -50%;
                right: -50%;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle, rgba(255, 107, 53, 0.1) 0%, transparent 70%);
                opacity: 0;
                transition: var(--transition);
            }
            
            .story-card:hover {
                transform: translateY(-8px) scale(1.02);
                box-shadow: var(--card-shadow-hover);
                border-color: var(--primary-color);
                background: rgba(45, 55, 72, 1);
            }
            
            .story-card:hover::after {
                opacity: 1;
                animation: shimmer 2s ease-in-out infinite;
            }
            
            @keyframes shimmer {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            /* Enhanced Category Badge with Neon Glow */
            .story-category {
                background: var(--gradient-accent);
                color: white;
                padding: 0.5rem 1.2rem;
                border-radius: 25px;
                font-size: 0.8rem;
                font-weight: 700;
                display: inline-block;
                margin-bottom: 1rem;
                font-family: 'Poppins', sans-serif;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: var(--glow-accent);
                position: relative;
                overflow: hidden;
                animation: categoryPulse 3s ease-in-out infinite;
            }
            
            @keyframes categoryPulse {
                0%, 100% { box-shadow: 0 0 10px rgba(156, 39, 176, 0.4); }
                50% { box-shadow: 0 0 20px rgba(156, 39, 176, 0.8), 0 0 30px rgba(156, 39, 176, 0.4); }
            }
            
            /* High Contrast Story Content */
            .story-title {
                font-size: 1.8rem !important;
                font-weight: 800 !important;
                color: var(--text-primary) !important;
                margin-bottom: 1rem;
                line-height: 1.3;
                background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
                letter-spacing: 0.5px;
                cursor: pointer;
            }
            
            .story-title:hover {
                opacity: 0.8;
                transition: var(--transition);
            }
            
            .story-meta {
                color: var(--text-secondary) !important;
                font-size: 0.9rem;
                margin-bottom: 1.2rem;
                font-family: 'Poppins', sans-serif;
                font-weight: 500;
                padding: 0.5rem 1rem;
                background: rgba(160, 174, 192, 0.1);
                border-radius: 20px;
                border-left: 3px solid var(--primary-color);
                backdrop-filter: blur(10px);
            }
            
            .story-excerpt {
                line-height: 1.8 !important;
                color: var(--text-primary) !important;
                margin-bottom: 1.5rem;
                font-size: 1.1rem !important;
                font-weight: 500 !important;
                padding: 1rem;
                background: rgba(255, 255, 255, 0.05);
                border-radius: var(--border-radius);
                border-left: 4px solid var(--primary-light);
                backdrop-filter: blur(10px);
                text-shadow: 0 1px 2px rgba(0,0,0,0.2);
            }
            
            /* Enhanced Action Buttons */
            .story-actions {
                display: flex;
                gap: 0.8rem;
                flex-wrap: wrap;
                margin-top: 1.5rem;
            }
            
            .story-actions button {
                font-size: 0.85rem !important;
                padding: 0.6rem 1.2rem !important;
                border-radius: 25px !important;
                font-weight: 600 !important;
                transition: var(--transition) !important;
                border: none !important;
                position: relative;
                overflow: hidden;
            }
            
            /* Enhanced Form Inputs with Better Validation */
            .stTextInput > div > div > input,
            .stTextArea > div > div > textarea,
            .stSelectbox > div > div > select {
                background: rgba(45, 55, 72, 0.8) !important;
                color: var(--text-primary) !important;
                border: 2px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: var(--border-radius) !important;
                font-family: 'Noto Sans Telugu', sans-serif !important;
                font-size: 1rem !important;
                padding: 1rem !important;
                transition: var(--transition) !important;
                backdrop-filter: blur(10px);
            }
            
            .stTextInput > div > div > input:focus,
            .stTextArea > div > div > textarea:focus,
            .stSelectbox > div > div > select:focus {
                border-color: var(--primary-color) !important;
                box-shadow: 0 0 20px rgba(255, 107, 53, 0.3) !important;
                outline: none !important;
            }

            /* Error State Styling */
            .input-error {
                border-color: var(--error-color) !important;
                box-shadow: 0 0 15px rgba(244, 67, 54, 0.3) !important;
            }

            /* Character Counter */
            .character-counter {
                font-size: 0.8rem;
                color: var(--text-muted);
                text-align: right;
                margin-top: 0.25rem;
            }

            .character-counter.warning {
                color: var(--warning-color);
            }

            .character-counter.error {
                color: var(--error-color);
            }
            
            /* Enhanced Labels */
            .stTextInput > label,
            .stTextArea > label,
            .stSelectbox > label {
                color: var(--text-primary) !important;
                font-weight: 600 !important;
                font-size: 1.1rem !important;
                margin-bottom: 0.5rem !important;
            }
            
            /* Loading Animation */
            .loading-spinner {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 2rem;
            }

            .spinner {
                width: 40px;
                height: 40px;
                border: 4px solid rgba(255, 107, 53, 0.3);
                border-top: 4px solid var(--primary-color);
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            /* Notification Styles */
            .notification {
                padding: 1rem;
                border-radius: var(--border-radius);
                margin: 1rem 0;
                animation: slideIn 0.3s ease-out;
            }

            .notification.success {
                background: rgba(76, 175, 80, 0.1);
                border-left: 4px solid var(--success-color);
                color: var(--success-color);
            }

            .notification.error {
                background: rgba(244, 67, 54, 0.1);
                border-left: 4px solid var(--error-color);
                color: var(--error-color);
            }

            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            /* Responsive improvements */
            @media (max-width: 768px) {
                h1 {
                    font-size: 2.5rem !important;
                }
                
                .story-title {
                    font-size: 1.5rem !important;
                }
                
                .story-excerpt {
                    font-size: 1rem !important;
                }
                
                .story-card {
                    padding: 1.5rem;
                    margin-bottom: 1.5rem;
                }

                .story-actions {
                    flex-direction: column;
                }

                .story-actions button {
                    width: 100%;
                    margin-bottom: 0.5rem;
                }
            }

            /* Accessibility improvements */
            .sr-only {
                position: absolute;
                width: 1px;
                height: 1px;
                padding: 0;
                margin: -1px;
                overflow: hidden;
                clip: rect(0, 0, 0, 0);
                white-space: nowrap;
                border: 0;
            }

            /* Focus indicators */
            button:focus-visible,
            input:focus-visible,
            textarea:focus-visible,
            select:focus-visible {
                outline: 2px solid var(--primary-color);
                outline-offset: 2px;
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

        if 'search_query' not in st.session_state:
            st.session_state.search_query = ""

        if 'user_interactions' not in st.session_state:
            st.session_state.user_interactions = {}
    
    def _get_default_stories(self) -> List[Dict[str, Any]]:
        """Return default stories data with unique IDs."""
        return [
            {
                "id": str(uuid.uuid4()),
                "title": "పల్లెటూరి ప్రయాణం",
                "author": "రవి కుమార్",
                "timestamp": "5 గంటల క్రితం",
                "category": "కథ",
                "content": "ఒకానొక పల్లెటూరిలో రాము అనే ఒక యువకుడు ఉండేవాడు. అతను తన ఊరిని విడిచి పట్టణం వెళ్లాలని కలలు కనేవాడు. అతని కలలు, కష్టాలు, మరియు విజయాల గురించిన ఈ కథ మనందరినీ ప్రేరేపిస్తుంది. గ్రామీణ జీవనం నుండి పట్టణ జీవితంలోకి మారడం ఎంత కష్టమో, అదే సమయంలో ఎంత అవసరమో ఈ కథ చెబుతుంది.",
                "excerpt": "ఒకానొక పల్లెటూరిలో రాము అనే ఒక యువకుడు ఉండేవాడు. అతను తన ఊరిని విడిచి పట్టణం వెళ్లాలని కలలు కనేవాడు. అతని కలలు, కష్టాలు, మరియు విజయాల గురించిన ఈ కథ...",
                "upvotes": 125,
                "downvotes": 5,
                "comments": 32,
                "views": 450,
                "created_at": datetime.now().isoformat(),
                "tags": ["ప్రేరణ", "కలలు", "గ్రామం"]
            },
            {
                "id": str(uuid.uuid4()),
                "title": "కాకతీయుల వైభవం",
                "author": "సుమలత",
                "timestamp": "2 రోజుల క్రితం",
                "category": "చరిత్ర",
                "content": "కాకతీయ సామ్రాజ్యం తెలుగు నేల స్వర్ణయుగాలలో ఒకటి. వారి పరిపాలన, కళలు, మరియు శిల్పకళ గురించి తెలుసుకుందాం. రుద్రమ దేవి, కాకతీయ కళాత్మక వైభవం, వరంగల్ కిల్లా వంటి అంశాలు ఈ కథనంలో వివరంగా చర్చించబడ్డాయి. తెలుగు వారి గర్వకారణమైన ఈ చరిత్రను తెలుసుకోవాలని అందరినీ కోరుకుంటున్నాను.",
                "excerpt": "కాకతీయ సామ్రాజ్యం తెలుగు నేల స్వర్ణయుగాలలో ఒకటి. వారి పరిపాలన, కళలు, మరియు శిల్పకళ గురించి తెలుసుకుందాం. రుద్రమ దేవి, కాకతీయ కళాత్మక వైభవం...",
                "upvotes": 250,
                "downvotes": 12,
                "comments": 78,
                "views": 1250,
                "created_at": datetime.now().isoformat(),
                "tags": ["కాకతీయులు", "చరిత్ర", "రుద్రమదేవి"]
            }
        ]
    
    def _validate_story_data(self, title: str, author: str, content: str, category: str) -> Tuple[bool, str]:
        """Validate story form data with enhanced checks."""
        title = title.strip()
        author = author.strip()
        content = content.strip()
        
        if not title:
            return False, "శీర్షిక తప్పనిసరి"
        if not author:
            return False, "రచయిత పేరు తప్పనిసరి"
        if not content:
            return False, "కథ/రచన తప్పనిసరి"
        if not category:
            return False, "విభాగం ఎంపిక తప్పనిసరి"
        
        if len(title) < self.MIN_TITLE_LENGTH:
            return False, f"శీర్షిక కనీసం {self.MIN_TITLE_LENGTH} అక్షరాలు ఉండాలి"
        if len(title) > 100:
            return False, "శీర్షిక 100 అక్షరాలకు మించకూడదు"
        if len(content) < self.MIN_CONTENT_LENGTH:
            return False, f"కథ/రచన కనీసం {self.MIN_CONTENT_LENGTH} అక్షరాలు ఉండాలి"
        if len(author) > 50:
            return False, "రచయిత పేరు 50 అక్షరాలకు మించకూడదు"
        
        # Check for duplicate titles
        existing_titles = [story['title'].lower() for story in st.session_state.stories]
        if title.lower() in existing_titles:
            return False, "ఈ శీర్షికతో కథ ఇప్పటికే ఉంది"
        
        return True, ""
    
    def _create_story_excerpt(self, content: str) -> str:
        """Create excerpt from story content."""
        content = content.strip()
        if len(content) <= self.EXCERPT_LENGTH:
            return content
        
        # Find a good breaking point (sentence or word boundary)
        excerpt = content[:self.EXCERPT_LENGTH]
        last_sentence = excerpt.rfind('.')
        last_space = excerpt.rfind(' ')
        
        if last_sentence > self.EXCERPT_LENGTH * 0.7:
            return excerpt[:last_sentence + 1]
        elif last_space > 0:
            return excerpt[:last_space] + "..."
        else:
            return excerpt + "..."
    
    def _add_new_story(self, title: str, author: str, category: str, content: str, tags: List[str] = None) -> None:
        """Add a new story to the session state."""
        story_id = str(uuid.uuid4())
        new_story = {
            "id": story_id,
            "title": title.strip(),
            "author": author.strip(),
            "timestamp": "ఇప్పుడే",
            "category": category,
            "content": content.strip(),
            "excerpt": self._create_story_excerpt(content.strip()),
            "upvotes": 0,
            "downvotes": 0,
            "comments": 0,
            "views": 0,
            "created_at": datetime.now().isoformat(),
            "tags": tags or []
        }
        st.session_state.stories.insert(0, new_story)
    
    def _get_time_ago(self, timestamp_str: str) -> str:
        """Convert timestamp to human readable time ago format."""
        if timestamp_str in ["ఇప్పుడే", "5 గంటల క్రితం", "2 రోజుల క్రితం"]:
            return timestamp_str
        
        try:
            timestamp = datetime.fromisoformat(timestamp_str)
            now = datetime.now()
            diff = now - timestamp
            
            if diff.days > 0:
                return f"{diff.days} రోజుల క్రితం"
            elif diff.seconds > 3600:
                hours = diff.seconds // 3600
                return f"{hours} గంటల క్రితం"
            elif diff.seconds > 60:
                minutes = diff.seconds // 60
                return f"{minutes} నిమిషాల క్రితం"
            else:
                return "ఇప్పుడే"
        except:
            return timestamp_str
    
    def _handle_story_interaction(self, story_id: str, action: str) -> None:
        """Handle user interactions with stories."""
        if story_id not in st.session_state.user_interactions:
            st.session_state.user_interactions[story_id] = {
                'upvoted': False,
                'downvoted': False
            }
        
        story_idx = next((i for i, s in enumerate(st.session_state.stories) if s['id'] == story_id), None)
        if story_idx is None:
            return
        
        user_interaction = st.session_state.user_interactions[story_id]
        
        if action == 'upvote':
            if user_interaction['upvoted']:
                # Remove upvote
                st.session_state.stories[story_idx]['upvotes'] -= 1
                user_interaction['upvoted'] = False
            else:
                # Add upvote
                st.session_state.stories[story_idx]['upvotes'] += 1
                user_interaction['upvoted'] = True
                # Remove downvote if exists
                if user_interaction['downvoted']:
                    st.session_state.stories[story_idx]['downvotes'] -= 1
                    user_interaction['downvoted'] = False
        
        elif action == 'downvote':
            if user_interaction['downvoted']:
                # Remove downvote
                st.session_state.stories[story_idx]['downvotes'] -= 1
                user_interaction['downvoted'] = False
            else:
                # Add downvote
                st.session_state.stories[story_idx]['downvotes'] += 1
                user_interaction['downvoted'] = True
                # Remove upvote if exists
                if user_interaction['upvoted']:
                    st.session_state.stories[story_idx]['upvotes'] -= 1
                    user_interaction['upvoted'] = False
    
    def _render_story_card(self, story: Dict[str, Any], index: int) -> None:
        """Render a single story card with enhanced features."""
        # Increment view count
        if 'views_updated' not in st.session_state:
            st.session_state.views_updated = set()
        
        story_id = story.get('id', f"story_{index}")
        if story_id not in st.session_state.views_updated:
            story['views'] = story.get('views', 0) + 1
            st.session_state.views_updated.add(story_id)
        
        # Story card container
        st.markdown('<div class="story-card">', unsafe_allow_html=True)
        
        # Category badge
        st.markdown(
            f'<div class="story-category">{story["category"]}</div>',
            unsafe_allow_html=True
        )
        
        # Story title (clickable for full view)
        st.markdown(
            f'<div class="story-title" title="Click to read full story">{story["title"]}</div>',
            unsafe_allow_html=True
        )
        
# Story metadata with views
        meta_info = f"""
        <div class="story-meta">
            <strong>రచయిత:</strong> {story["author"]} • 
            <strong>సమయం:</strong> {self._get_time_ago(story.get("created_at", story["timestamp"]))} • 
            <strong>వీక్షణలు:</strong> {story.get('views', 0):,}
        </div>
        """
        st.markdown(meta_info, unsafe_allow_html=True)
        
        # Story excerpt
        st.markdown(
            f'<div class="story-excerpt">{story["excerpt"]}</div>',
            unsafe_allow_html=True
        )
        
        # Tags if available
        if story.get('tags'):
            tags_html = ' '.join([f'<span class="tag">#{tag}</span>' for tag in story['tags']])
            st.markdown(f'<div class="story-tags">{tags_html}</div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 4])
        
        user_interaction = st.session_state.user_interactions.get(story_id, {'upvoted': False, 'downvoted': False})
        
        with col1:
            upvote_label = f"👍 {story.get('upvotes', 0)}"
            if user_interaction['upvoted']:
                upvote_label = f"👍 {story.get('upvotes', 0)} ✓"
            
            if st.button(upvote_label, key=f"upvote_{story_id}_{index}"):
                self._handle_story_interaction(story_id, 'upvote')
                st.rerun()
        
        with col2:
            downvote_label = f"👎 {story.get('downvotes', 0)}"
            if user_interaction['downvoted']:
                downvote_label = f"👎 {story.get('downvotes', 0)} ✓"
            
            if st.button(downvote_label, key=f"downvote_{story_id}_{index}"):
                self._handle_story_interaction(story_id, 'downvote')
                st.rerun()
        
        with col3:
            if st.button(f"💬 {story.get('comments', 0)}", key=f"comment_{story_id}_{index}"):
                st.info("వ్యాఖ్యల ఫీచర్ త్వరలో వస్తుంది!")
        
        with col4:
            if st.button("📖 చదవండి", key=f"read_{story_id}_{index}"):
                self._show_full_story(story)
        
        with col5:
            if st.button("📤 షేర్ చేయండి", key=f"share_{story_id}_{index}"):
                self._show_share_options(story)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    def _show_full_story(self, story: Dict[str, Any]) -> None:
        """Display full story in a modal-like interface."""
        st.markdown("---")
        st.markdown('<div class="story-card full-story">', unsafe_allow_html=True)
        
        # Story header
        st.markdown(f'<div class="story-category">{story["category"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<h2 class="story-title">{story["title"]}</h2>', unsafe_allow_html=True)
        
        # Author and timestamp
        meta_info = f"""
        <div class="story-meta">
            <strong>రచయిత:</strong> {story["author"]} • 
            <strong>ప్రచురణ:</strong> {self._get_time_ago(story.get("created_at", story["timestamp"]))} • 
            <strong>వీక్షణలు:</strong> {story.get('views', 0):,}
        </div>
        """
        st.markdown(meta_info, unsafe_allow_html=True)
        
        # Full content
        st.markdown(f'<div class="story-content">{story["content"]}</div>', unsafe_allow_html=True)
        
        # Tags
        if story.get('tags'):
            st.markdown("**ట్యాగులు:** " + " | ".join([f"#{tag}" for tag in story['tags']]))
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("← వెనుకకు", key="back_to_stories"):
            st.rerun()
    
    def _show_share_options(self, story: Dict[str, Any]) -> None:
        """Show sharing options for a story."""
        st.markdown("### షేర్ ఆప్షన్స్")
        
        # Create shareable text
        share_text = f"""
{story['title']}
రచయిత: {story['author']}

{story['excerpt']}

#తెలుగుకథలు #TeluguStories
        """.strip()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_area("కథ టెక్స్ట్ కాపీ చేయండి:", value=share_text, height=150)
        
        with col2:
            st.markdown("**సోషల్ మీడియా లింక్స్:**")
            
            # WhatsApp
            whatsapp_url = f"https://wa.me/?text={share_text.replace(' ', '%20')}"
            st.markdown(f'<a href="{whatsapp_url}" target="_blank">📱 WhatsApp లో షేర్ చేయండి</a>', unsafe_allow_html=True)
            
            # Twitter
            twitter_url = f"https://twitter.com/intent/tweet?text={share_text.replace(' ', '%20')}"
            st.markdown(f'<a href="{twitter_url}" target="_blank">🐦 Twitter లో షేర్ చేయండి</a>', unsafe_allow_html=True)
            
            # Facebook
            facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=&quote={share_text.replace(' ', '%20')}"
            st.markdown(f'<a href="{facebook_url}" target="_blank">📘 Facebook లో షేర్ చేయండి</a>', unsafe_allow_html=True)
    
    def _filter_stories(self, stories: List[Dict[str, Any]], search_query: str, selected_category: str) -> List[Dict[str, Any]]:
        """Filter stories based on search and category."""
        filtered_stories = stories
        
        # Filter by category
        if selected_category != "అన్నీ":
            filtered_stories = [s for s in filtered_stories if s["category"] == selected_category]
        
        # Filter by search query
        if search_query:
            search_query = search_query.lower().strip()
            filtered_stories = [
                s for s in filtered_stories 
                if (search_query in s["title"].lower() or 
                    search_query in s["author"].lower() or 
                    search_query in s["content"].lower() or
                    search_query in s.get("excerpt", "").lower() or
                    any(search_query in tag.lower() for tag in s.get("tags", [])))
            ]
        
        return filtered_stories
    
    def _render_story_form(self) -> None:
        """Render the story submission form with enhanced validation."""
        st.markdown("## కొత్త కథ/రచన జోడించండి")
        
        with st.form("story_form", clear_on_submit=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                title = st.text_input(
                    "శీర్షిక *",
                    placeholder="మీ కథకు అందమైన శీర్షిక ఇవ్వండి...",
                    help="కనీసం 3 అక్షరాలు, గరిష్టంగా 100 అక్షరాలు"
                )
                
                # Character counter for title
                if title:
                    title_length = len(title)
                    counter_class = "error" if title_length > 100 else "warning" if title_length > 80 else ""
                    st.markdown(
                        f'<div class="character-counter {counter_class}">{title_length}/100</div>',
                        unsafe_allow_html=True
                    )
            
            with col2:
                category = st.selectbox("విభాగం *", [""] + self.CATEGORIES)
            
            author = st.text_input(
                "రచయిత పేరు *",
                placeholder="మీ పేరు లేదా పెన్ నేమ్...",
                help="గరిష్టంగా 50 అక్షరాలు"
            )
            
            # Character counter for author
            if author:
                author_length = len(author)
                counter_class = "error" if author_length > 50 else "warning" if author_length > 40 else ""
                st.markdown(
                    f'<div class="character-counter {counter_class}">{author_length}/50</div>',
                    unsafe_allow_html=True
                )
            
            content = st.text_area(
                "కథ/రచన *",
                placeholder="మీ కథ లేదా రచనను ఇక్కడ వ్రాయండి...",
                height=300,
                help=f"కనీసం {self.MIN_CONTENT_LENGTH} అక్షరాలు అవసరం"
            )
            
            # Character counter for content
            if content:
                content_length = len(content)
                counter_class = "error" if content_length < self.MIN_CONTENT_LENGTH else ""
                st.markdown(
                    f'<div class="character-counter {counter_class}">{content_length} అక్షరాలు</div>',
                    unsafe_allow_html=True
                )
            
            # Tags input
            tags_input = st.text_input(
                "ట్యాగులు (ఐచ్చికం)",
                placeholder="కొన్ని కీవర్డ్లను కామాతో వేరు చేయండి... (ఉదా: ప్రేమ, కుటుంబం, స్నేహం)",
                help="ట్యాగులు మీ కథను కనుగొనడంలో సహాయపడతాయి"
            )
            
            # Form submission
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                submit_button = st.form_submit_button(
                    "📝 కథ ప్రచురించండి",
                    use_container_width=True
                )
            
            if submit_button:
                # Process tags
                tags = []
                if tags_input:
                    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
                    tags = tags[:5]  # Limit to 5 tags
                
                # Validate form data
                is_valid, error_message = self._validate_story_data(title, author, content, category)
                
                if is_valid:
                    try:
                        self._add_new_story(title, author, category, content, tags)
                        st.success("✅ మీ కథ విజయవంతంగా జోడించబడింది!")
                        st.session_state.show_form = False
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ కథ జోడించడంలో లోపం: {str(e)}")
                else:
                    st.error(f"❌ {error_message}")
    
    def _render_statistics(self) -> None:
        """Render platform statistics."""
        st.markdown("## 📊 వేదిక గణాంకాలు")
        
        total_stories = len(st.session_state.stories)
        total_authors = len(set(story['author'] for story in st.session_state.stories))
        total_views = sum(story.get('views', 0) for story in st.session_state.stories)
        total_upvotes = sum(story.get('upvotes', 0) for story in st.session_state.stories)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("మొత్తం కథలు", total_stories, delta="📚")
        
        with col2:
            st.metric("రచయితలు", total_authors, delta="👥")
        
        with col3:
            st.metric("మొత్తం వీక్షణలు", f"{total_views:,}", delta="👀")
        
        with col4:
            st.metric("మొత్తం లైక్స్", total_upvotes, delta="👍")
        
        # Category wise distribution
        category_counts = {}
        for story in st.session_state.stories:
            category = story['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        if category_counts:
            st.markdown("### విభాగవారీ పంపిణీ")
            
            cols = st.columns(len(category_counts))
            for i, (category, count) in enumerate(category_counts.items()):
                with cols[i]:
                    percentage = (count / total_stories) * 100
                    st.metric(category, count, delta=f"{percentage:.1f}%")
    
    def _render_header(self) -> None:
        """Render the application header."""
        st.markdown('<h1>తెలుగు కథలు 📖</h1>', unsafe_allow_html=True)
        st.markdown(
            '<p style="text-align: center; font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem;">తెలుగు సాహిత్య ప్రేమికుల వేదిక - మీ కథలను, అనుభవాలను పంచుకోండి</p>',
            unsafe_allow_html=True
        )
    
    def _render_navigation(self) -> str:
        """Render navigation menu and return selected page."""
        st.markdown("---")
        
        col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
        
        with col1:
            if st.button("🏠 హోమ్", use_container_width=True):
                st.session_state.show_form = False
                return "home"
        
        with col2:
            if st.button("➕ కథ వ్రాయండి", use_container_width=True):
                st.session_state.show_form = True
                return "write"
        
        with col3:
            if st.button("📊 గణాంకాలు", use_container_width=True):
                st.session_state.show_form = False
                return "stats"
        
        with col4:
            if st.button("ℹ️ గురించి", use_container_width=True):
                return "about"
        
        st.markdown("---")
        
        return "home" if not st.session_state.show_form else "write"
    
    def _render_about_page(self) -> None:
        """Render the about page."""
        st.markdown("## తెలుగు కథల వేదిక గురించి")
        
        st.markdown("""
        ### 🎯 మా లక్ష్యం
        తెలుగు భాషలో సృజనాత్మక రచనలను ప్రోత్సహించడం మరియు తెలుగు సాహిత్య ప్రేమికులకు ఒక వేదిక కల్పించడం.
        
        ### ✨ ప్రత్యేకతలు
        - **సులభమైన ఇంటర్ఫేస్**: సరళమైన మరియు ఆకర్షణీయమైన డిజైన్
        - **మల్టీ కేటగిరీ**: కథ, చరిత్ర, సంస్కృతి, కవిత, విజ్ఞానం వంటి విభాగాలు
        - **సామాజిక ఫీచర్స్**: లైక్, డిస్‌లైక్, కమెంట్, షేర్ ఆప్షన్స్
        - **సెర్చ్ & ఫిల్టర్**: మీకు నచ్చిన కథలను సులభంగా కనుగొనండి
        
        ### 👥 కమ్యూనిటీ గైడ్‌లైన్స్
        1. **గౌరవం**: అందరి అభిప్రాయాలను గౌరవించండి
        2. **నాణ్యత**: మంచి నాణ్యత కథలను మాత్రమే పంచుకోండి
        3. **మర్యాద**: అనుచితమైన కంటెంట్ పోస్ట్ చేయవద్దు
        4. **సహకారం**: ఇతర రచయితలను ప్రోత్సహించండి
        
        ### 📞 సంప్రదించండి
        - **ఇమెయిల్**: support@telugukathas.com
        - **బగ్ రిపోర్ట్**: bugs@telugukathas.com
        
        ---
        
        **మీ కథలతో తెలుగు సాహిత్యాన్ని సమృద్ధం చేయండి! 🌟**
        """)
    
    def run(self) -> None:
        """Main application runner."""
        # Render header
        self._render_header()
        
        # Navigation
        current_page = self._render_navigation()
        
        if current_page == "about":
            self._render_about_page()
            return
        
        if current_page == "stats":
            self._render_statistics()
            return
        
        if current_page == "write" or st.session_state.show_form:
            self._render_story_form()
            return
        
        # Main content area - Home page
        st.markdown("## 🏠 తాజా కథలు")
        
        # Search and filter controls
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_query = st.text_input(
                "🔍 కథలను వెతకండి...",
                value=st.session_state.search_query,
                placeholder="శీర్షిక, రచయిత లేదా కంటెంట్‌లో వెతకండి...",
                key="main_search"
            )
            if search_query != st.session_state.search_query:
                st.session_state.search_query = search_query
                st.rerun()
        
        with col2:
            category_filter = st.selectbox(
                "విభాగం ఎంచుకోండి",
                ["అన్నీ"] + self.CATEGORIES,
                key="category_filter"
            )
        
        # Filter and display stories
        filtered_stories = self._filter_stories(
            st.session_state.stories, 
            st.session_state.search_query, 
            category_filter
        )
        
        if not filtered_stories:
            st.warning("🔍 మీ వెతుకులాట ప్రకారం కథలు లేవు. వేరే కీవర్డ్స్ ప్రయత్నించండి.")
        else:
            st.markdown(f"**{len(filtered_stories)} కథలు దొరికాయి**")
            
            # Display stories
            for index, story in enumerate(filtered_stories):
                self._render_story_card(story, index)
                
                # Add some spacing between cards
                st.markdown("<br>", unsafe_allow_html=True)


# Application entry point
if __name__ == "__main__":
    app = TeluguStoriesApp()
    app.run()
