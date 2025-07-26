# Contributing to Telugu Stories Forum 🤝

మీ సహకారాన్ని స్వాగతించుకుంటున్నాము! We welcome contributions from the Telugu community and developers worldwide. This guide will help you contribute to our Streamlit-based Telugu Stories platform.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Overview](#project-overview)
- [Development Setup](#development-setup)
- [Code Architecture](#code-architecture)
- [Contribution Workflow](#contribution-workflow)
- [Coding Standards](#coding-standards)
- [Feature Development](#feature-development)
- [Telugu Text Guidelines](#telugu-text-guidelines)
- [UI/UX Guidelines](#uiux-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Merge Request Process](#merge-request-process)
- [Community Guidelines](#community-guidelines)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

### Our Pledge
- Be respectful and inclusive to all community members
- Focus on constructive feedback and collaboration
- Respect Telugu culture and literary traditions
- Maintain high-quality code and documentation standards
- Help create a safe space for creative expression

### Unacceptable Behavior
- Harassment, discrimination, or offensive language
- Spam, trolling, or disruptive behavior
- Inappropriate content or cultural insensitivity
- Violation of intellectual property rights
- Any form of abuse or threatening behavior

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git installed on your system
- Basic knowledge of Streamlit framework
- Understanding of Telugu Unicode (helpful for UI/UX work)
- GitLab account (preferably on Swecha's instance)

### Quick Start for New Contributors
1. **Fork the repository** on GitLab
2. **Read through existing issues** in the issue tracker
3. **Join Swecha community** discussions
4. **Set up development environment** (see below)
5. **Make your first contribution** (documentation improvements are great for beginners)

## Project Overview

### Technology Stack
- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with session state management
- **Styling**: Custom CSS with Glass Morphism design
- **Typography**: Noto Sans Telugu, Poppins fonts
- **Data Storage**: Streamlit session state (in-memory)

### Key Features
- Multi-category story platform (కథ, చరిత్ర, సంస్కృతి, కవిత, విజ్ఞానం, ఇతర)
- Real-time search and filtering
- User interaction system (upvotes, downvotes, views, comments)
- Social sharing capabilities
- Responsive dark theme with Telugu typography
- Story validation and moderation

### Current Architecture
```
TeluguStoriesApp (Main Class)
├── _configure_page()          # Streamlit page configuration
├── _load_custom_styles()      # CSS styling and themes
├── _initialize_session_state() # Data initialization
├── _validate_story_data()     # Input validation
├── _render_story_card()       # Story display components
├── _render_story_form()       # Story submission form
├── _filter_stories()          # Search and filter logic
└── run()                      # Main application runner
```

## Development Setup

### 1. Fork and Clone
```bash
# Fork the repository on GitLab, then clone your fork
git clone https://code.swecha.org/YOUR_USERNAME/Telugu-Stories-Forum.git
cd Telugu-Stories-Forum
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Install Streamlit and other requirements
pip install streamlit

# If requirements.txt exists:
pip install -r requirements.txt
```

### 4. Run the Application
```bash
# Start the Streamlit app
streamlit run app.py
```

### 5. Verify Setup
- Open http://localhost:8501 in your browser
- Test story submission form
- Verify Telugu text rendering
- Check responsive design on mobile/tablet
- Test search and filtering functionality

## Code Architecture

### Main Application Class: `TeluguStoriesApp`

#### Class Constants
```python
CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం", "ఇతర"]
EXCERPT_LENGTH = 150
MIN_TITLE_LENGTH = 3
MIN_CONTENT_LENGTH = 50
```

#### Key Methods to Understand
- **`_load_custom_styles()`**: Contains all CSS styling - modify for UI changes
- **`_validate_story_data()`**: Input validation logic - extend for new validation rules
- **`_render_story_card()`**: Story display component - modify for layout changes
- **`_filter_stories()`**: Search and filtering logic - extend for advanced search features

### Session State Management
The application uses Streamlit's session state for data persistence:
```python
st.session_state.stories          # All stories data
st.session_state.show_form        # Form visibility state
st.session_state.search_query     # Current search query
st.session_state.user_interactions # User voting data
```

## Contribution Workflow

### 1. Create a Branch
```bash
# Create and switch to a new feature branch
git checkout -b feature/your-feature-name

# Examples:
git checkout -b feature/add-comment-system
git checkout -b bugfix/telugu-search-issue
git checkout -b ui/improve-mobile-layout
git checkout -b docs/api-documentation
```

### 2. Development Guidelines

#### For New Features
1. Add constants to class if needed
2. Create helper methods following naming convention (`_method_name`)
3. Update `run()` method for new navigation items
4. Add appropriate CSS classes in `_load_custom_styles()`
5. Implement validation if handling user input

#### For Bug Fixes
1. Identify the root cause
2. Add comments explaining the fix
3. Test edge cases thoroughly
4. Update documentation if behavior changes

### 3. Commit Guidelines
```bash
# Use descriptive commit messages with Telugu context where relevant
git commit -m "Add: Comment system for stories

- Implement comment CRUD operations in session state
- Add Telugu comment validation
- Update story card UI with comment display
- Add comment count to story statistics
- Include comment threading support"

# For bug fixes:
git commit -m "Fix: Telugu text search not working in story content

- Fix Unicode handling in _filter_stories method
- Update search to handle Telugu diacritics properly
- Add test cases for Telugu search queries"

# For UI improvements:
git commit -m "UI: Improve mobile responsiveness for story cards

- Update CSS media queries for mobile devices
- Fix story card padding and margins on small screens
- Improve touch targets for mobile interactions"
```

## Coding Standards

### Python Style Guidelines
Follow the existing code patterns in the project:

```python
class TeluguStoriesApp:
    """Main application class with clear docstrings."""
    
    # Constants in UPPERCASE
    CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి"]
    
    def _private_method(self) -> Optional[str]:
        """Private methods start with underscore and have type hints."""
        pass
    
    def _validate_story_data(self, title: str, author: str, 
                           content: str, category: str) -> Tuple[bool, str]:
        """
        Validate story form data with enhanced checks.
        
        Args:
            title: Story title (3-100 characters)
            author: Author name (max 50 characters)
            content: Story content (min 50 characters)
            category: Selected category from CATEGORIES
            
        Returns:
            Tuple of (is_valid: bool, error_message: str)
        """
        # Validation logic here
        pass
```

### CSS Guidelines
Follow the existing CSS architecture:

```css
/* Use CSS custom properties (variables) */
:root {
    --primary-color: #FF6B35;
    --background-primary: #0F1419;
    /* ... other variables */
}

/* Follow BEM-like naming for new components */
.story-card {
    /* Base styles */
}

.story-card__header {
    /* Component part styles */
}

.story-card--featured {
    /* Modifier styles */
}

/* Include hover states and transitions */
.story-card:hover {
    transform: translateY(-8px) scale(1.02);
    transition: var(--transition);
}
```

### Telugu Text Guidelines
```python
# Always handle Telugu text properly
def _create_story_excerpt(self, content: str) -> str:
    """Create excerpt with proper Telugu word boundaries."""
    content = content.strip()
    if len(content) <= self.EXCERPT_LENGTH:
        return content
    
    # Look for Telugu sentence boundaries (।, .)
    excerpt = content[:self.EXCERPT_LENGTH]
    for delimiter in ['।', '.', '!', '?']:
        last_delimiter = excerpt.rfind(delimiter)
        if last_delimiter > self.EXCERPT_LENGTH * 0.7:
            return excerpt[:last_delimiter + 1]
    
    # Fall back to word boundary
    last_space = excerpt.rfind(' ')
    if last_space > 0:
        return excerpt[:last_space] + "..."
    return excerpt + "..."
```

## Feature Development

### Adding New Story Categories
```python
# 1. Update CATEGORIES constant
CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం", "ఇతర", "నవల"]

# 2. Add category-specific validation if needed
def _validate_category_content(self, content: str, category: str) -> bool:
    """Add category-specific validation rules."""
    if category == "కవిత" and len(content.split('\n')) < 4:
        return False  # Poetry should have multiple lines
    return True

# 3. Update CSS for new category styling
.story-category.novel {
    background: var(--gradient-novel);
}
```

### Adding User Authentication
```python
# 1. Add to session state initialization
if 'user' not in st.session_state:
    st.session_state.user = None
    st.session_state.user_profile = {}

# 2. Create authentication methods
def _render_login_form(self) -> None:
    """Render user login/registration form."""
    pass

def _authenticate_user(self, username: str, password: str) -> bool:
    """Authenticate user credentials."""
    pass
```

### Adding Comment System
```python
# 1. Update story data structure
def _initialize_session_state(self) -> None:
    # Add comments to story structure
    if 'comments' not in st.session_state:
        st.session_state.comments = {}  # story_id -> [comments]

# 2. Create comment management methods
def _add_comment(self, story_id: str, comment: str, author: str) -> None:
    """Add comment to a story."""
    pass

def _render_comments(self, story_id: str) -> None:
    """Render comments section for a story."""
    pass
```

## Telugu Text Guidelines

### Unicode Handling
```python
# Always use UTF-8 encoding
def _process_telugu_text(self, text: str) -> str:
    """Process Telugu text with proper Unicode handling."""
    # Normalize Unicode to handle different representations
    import unicodedata
    return unicodedata.normalize('NFC', text.strip())

# Handle Telugu numerals and special characters
def _format_telugu_numbers(self, number: int) -> str:
    """Convert numbers to Telugu numerals if needed."""
    english_digits = "0123456789"
    telugu_digits = "౦౧౨౩౪౫౬౭౮౯"
    translation_table = str.maketrans(english_digits, telugu_digits)
    return str(number).translate(translation_table)
```

### Search and Filtering
```python
def _normalize_for_search(self, text: str) -> str:
    """Normalize Telugu text for better search results."""
    import unicodedata
    # Remove diacritics for broader search matching
    normalized = unicodedata.normalize('NFD', text)
    return ''.join(c for c in normalized if not unicodedata.combining(c))
```

### Font and Typography
```css
/* Ensure proper Telugu font rendering */
.telugu-text {
    font-family: 'Noto Sans Telugu', 'Gautami', 'Vani', sans-serif;
    font-feature-settings: "liga" 1, "calt" 1;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Different weights for Telugu text */
.telugu-heading {
    font-weight: 700; /* Bold works well for Telugu */
    letter-spacing: 0.025em;
}

.telugu-body {
    font-weight: 400;
    line-height: 1.7; /* Good for Telugu readability */
}
```

## UI/UX Guidelines

### Design Principles
1. **Dark Theme First**: The application uses a dark theme optimized for reading
2. **Glass Morphism**: Use backdrop-filter and translucent backgrounds
3. **Neon Accents**: Glowing effects for interactive elements
4. **High Contrast**: Ensure text is readable against dark backgrounds
5. **Responsive Design**: Mobile-first approach

### Color Palette
```css
:root {
    --primary-color: #FF6B35;    /* Orange primary */
    --primary-light: #FF8A65;    /* Light orange */
    --accent-color: #9C27B0;     /* Purple accent */
    --success-color: #4CAF50;    /* Green success */
    --background-primary: #0F1419; /* Dark background */
    --background-secondary: #1A202C; /* Card background */
    --text-primary: #FFFFFF;     /* White text */
    --text-secondary: #A0AEC0;   /* Gray text */
}
```

### Component Design Guidelines
```css
/* All interactive elements should have hover states */
.interactive-element {
    transition: var(--transition);
    cursor: pointer;
}

.interactive-element:hover {
    transform: translateY(-2px);
    box-shadow: var(--card-shadow-hover);
}

/* Cards should use glass morphism */
.card {
    background: rgba(45, 55, 72, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--border-radius-large);
}

/* Buttons should have gradient backgrounds */
.primary-button {
    background: var(--gradient-primary);
    border: none;
    color: white;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}
```

### Mobile Responsiveness
```css
/* Mobile-first responsive design */
@media (max-width: 768px) {
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
    
    h1 {
        font-size: 2.5rem !important;
    }
}
```

## Testing Guidelines

### Manual Testing Checklist
Before submitting a merge request, test:

#### Basic Functionality
- [ ] Story submission form works correctly
- [ ] Telugu text input and display
- [ ] Search functionality with Telugu keywords
- [ ] Category filtering
- [ ] Voting system (upvote/downvote)
- [ ] Story sharing functionality

#### UI/UX Testing
- [ ] Responsive design on mobile/tablet/desktop
- [ ] Dark theme consistency
- [ ] Telugu font rendering across browsers
- [ ] Button hover states and animations
- [ ] Form validation messages
- [ ] Loading states and transitions

#### Cross-browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (if on macOS)
- [ ] Edge (latest)
- [ ] Mobile browsers (Chrome Mobile, Safari Mobile)

#### Telugu-specific Testing
- [ ] Telugu text input in all form fields
- [ ] Search with Telugu keywords
- [ ] Telugu number formatting
- [ ] Mixed English-Telugu content handling
- [ ] Special Telugu characters (symbols, punctuation)

### Writing Unit Tests
```python
import unittest
from datetime import datetime

class TestTeluguStoriesApp(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.app = TeluguStoriesApp()
    
    def test_story_validation(self):
        """Test story data validation."""
        # Valid story
        is_valid, message = self.app._validate_story_data(
            "టెస్ట్ కథ", "టెస్ట్ రచయిత", "ఇది ఒక పరీక్ష కథ." * 10, "కథ"
        )
        self.assertTrue(is_valid)
        
        # Invalid story (too short content)
        is_valid, message = self.app._validate_story_data(
            "చిన్న కథ", "రచయిత", "చిన్న", "కథ"
        )
        self.assertFalse(is_valid)
        self.assertIn("కనీసం", message)
    
    def test_excerpt_creation(self):
        """Test Telugu text excerpt creation."""
        long_content = "ఇది ఒక చాలా పొడవైన కథ. " * 20
        excerpt = self.app._create_story_excerpt(long_content)
        self.assertLessEqual(len(excerpt), self.app.EXCERPT_LENGTH + 3)
        self.assertTrue(excerpt.endswith('.') or excerpt.endswith('...'))
    
    def test_telugu_search(self):
        """Test search functionality with Telugu text."""
        stories = [
            {"title": "పరీక్ష కథ", "author": "రచయిత", "content": "కథ కంటెంట్", "category": "కథ"}
        ]
        
        # Search by Telugu title
        filtered = self.app._filter_stories(stories, "పరీక్ష", "అన్నీ")
        self.assertEqual(len(filtered), 1)
        
        # Search by partial Telugu text
        filtered = self.app._filter_stories(stories, "రీక్ష", "అన్నీ")
        self.assertEqual(len(filtered), 1)

if __name__ == '__main__':
    unittest.main()
```

## Documentation

### Code Documentation
```python
def _render_story_card(self, story: Dict[str, Any], index: int) -> None:
    """
    Render a single story card with interactive elements.
    
    This method creates a complete story card with:
    - Category badge with gradient styling
    - Clickable title for full story view
    - Author metadata with timestamp and view count
    - Story excerpt with proper Telugu text handling
    - Interactive buttons (upvote, downvote, comment, read, share)
    
    Args:
        story: Dictionary containing story data with keys:
               - id: Unique story identifier
               - title: Story title (Telugu/English)
               - author: Author name
               - category: Story category
               - content: Full story content
               - excerpt: Auto-generated excerpt
               - upvotes/downvotes: Vote counts
               - views: View count
               - created_at: Creation timestamp
        index: Story position in the list (for unique keys)
    
    Side Effects:
        - Updates story view count
        - Modifies session state for user interactions
        - Triggers UI rerun on user actions
    
    Note:
        This method handles Telugu text rendering and ensures
        proper Unicode display across different browsers.
    """
```

### README Updates
When adding new features, update the README.md:

```markdown
## New Features Added

### Comment System
- Users can now comment on stories
- Threaded comment support
- Comment moderation tools
- Telugu text support in comments

### Enhanced Search
- Advanced search with filters
- Search history
- Auto-suggestions
- Better Telugu text matching
```

## Issue Reporting

### Bug Reports
Use the following template in GitLab issues:

```markdown
**Bug Description**
A clear description of the bug in English and Telugu if relevant

**Steps to Reproduce**
1. Go to story submission form
2. Enter Telugu text: "తెలుగు టెక్స్ట్ ఉదాహరణ"
3. Click submit
4. Observe error

**Expected Behavior**
Telugu text should be saved and displayed correctly

**Actual Behavior**
Text appears garbled or throws encoding error

**Screenshots**
[Attach screenshots showing the issue]

**Environment**
- OS: [e.g., Windows 10, Ubuntu 20.04]
- Browser: [e.g., Chrome 91, Firefox 89]
- Python version: [e.g., 3.9.5]
- Streamlit version: [e.g., 1.28.0]

**Telugu-specific Information**
- Input method used: [e.g., Google Input Tools, Windows Telugu keyboard]
- Character encoding issues: [if any]
- Font rendering problems: [if any]

**Additional Context**
Any other relevant information about the bug
```

### Feature Requests
```markdown
**Feature Description**
A clear description of the proposed feature

**Telugu Literature Context**
How this feature would benefit Telugu literature sharing

**Use Case**
Specific scenario where this feature would be valuable

**Proposed Implementation**
Technical suggestions for implementation

**Mockups/Wireframes**
[If available, attach visual representations]

**Acceptance Criteria**
- [ ] Feature works with Telugu text
- [ ] Mobile responsive
- [ ] Follows existing UI patterns
- [ ] Includes proper validation
```

## Merge Request Process

### Before Submitting
- [ ] Code follows project style guidelines
- [ ] All manual tests pass
- [ ] Telugu text functionality verified
- [ ] Mobile responsiveness tested
- [ ] Cross-browser compatibility checked
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)

### MR Template
```markdown
## Description
Brief description of changes made

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] UI/UX improvement
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Related Issues
Closes #[issue_number]

## Testing Performed
- [ ] Manual testing completed
- [ ] Telugu text input/output verified
- [ ] Mobile responsive testing
- [ ] Cross-browser testing
- [ ] Unit tests added/updated

## Screenshots
### Before
[Screenshots of current state]

### After
[Screenshots of changes]

## Telugu-Specific Changes
[Any changes related to Telugu text handling, cultural aspects, or language features]

## Breaking Changes
[List any breaking changes and migration notes]

## Checklist
- [ ] Code is self-documenting and/or commented
- [ ] Follows existing code patterns
- [ ] UI changes follow design guidelines
- [ ] Telugu text handling is robust
- [ ] Mobile-friendly design
- [ ] No console errors or warnings
```

### Review Process
1. **Automated Checks**: Code style and basic validation
2. **Technical Review**: Code quality, architecture, performance
3. **UI/UX Review**: Design consistency, user experience
4. **Telugu Review**: Cultural appropriateness, text handling
5. **Testing Review**: Functionality, edge cases, browser compatibility
6. **Final Approval**: Maintainer approval for merge

## Community Guidelines

### Communication Standards
- Use respectful language in all interactions
- Provide constructive, actionable feedback
- Be patient with new contributors
- Share knowledge and help others learn
- Respect cultural differences and perspectives

### Telugu Community Standards
- Respect Telugu literary traditions and cultural values
- Use appropriate Telugu terminology and expressions
- Consider diverse Telugu regional variations
- Avoid controversial cultural or political topics
- Promote inclusivity within the Telugu community

### Recognition System
Contributors will be recognized through:
- **Contributor listings** in README and documentation
- **Release notes** mentioning significant contributions
- **Community highlights** for exceptional work
- **Mentorship opportunities** for experienced contributors
- **Swecha community** events and meetups

## Getting Help

### Resources
- **Project Documentation**: README.md and code comments
- **GitLab Issues**: Search existing issues for solutions
- **Swecha Community**: Join Swecha's developer community
- **Streamlit Docs**: Official Streamlit documentation
- **Telugu Unicode**: Resources on Telugu text handling

### Support Channels
- **Technical Issues**: Create GitLab issues
- **General Questions**: Use GitLab discussions
- **Community Chat**: Join Swecha's communication channels
- **Cultural Guidance**: Consult with Telugu literature experts

### Mentorship Program
- New contributors can request mentorship
- Experienced developers offer guidance
- Code review and learning sessions
- Pair programming opportunities
- Telugu localization mentorship

---

## స్వాగతం! Welcome to Telugu Stories Forum! 

Your contributions help preserve and promote Telugu literature in the digital age. Whether you're fixing a bug, adding a feature, improving the UI, or enhancing Telugu text support, every contribution makes our platform better for the Telugu literary community.

**Happy Contributing!** 🌟

---

### Quick Start Commands
```bash
# Fork and clone
git clone https://code.swecha.org/YOUR_USERNAME/Telugu-Stories-Forum.git
cd Telugu-Stories-Forum

# Set up development environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install streamlit

# Run the application
streamlit run app.py

# Create feature branch
git checkout -b feature/your-awesome-feature

# Make changes, commit, and push
git add .
git commit -m "Add: Your awesome feature"
git push origin feature/your-awesome-feature

# Create merge request on GitLab
```

*For questions about this contributing guide, please open an issue or start a discussion in the GitLab repository.*