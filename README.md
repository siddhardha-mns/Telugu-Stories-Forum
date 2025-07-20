# తెలుగు కథలు - Telugu Stories Platform 📖

A beautiful, feature-rich web platform for Telugu literature enthusiasts to share and discover stories, built with Streamlit.

## 🌟 Features

### 📚 Content Management
- **Multi-Category Support**: Stories organized into కథ (Stories), చరిత్ర (History), సంస్కృతి (Culture), కవిత (Poetry), విజ్ఞానం (Science), and ఇతర (Others)
- **Rich Text Support**: Full Telugu Unicode support with beautiful typography
- **Story Excerpts**: Automatic generation of story previews
- **Tags System**: Categorize stories with custom tags for better discoverability

### 🔍 Discovery & Navigation
- **Advanced Search**: Search across titles, authors, content, and tags
- **Category Filtering**: Filter stories by specific categories
- **Real-time Updates**: Dynamic content updates without page refresh
- **Responsive Design**: Mobile-friendly interface

### 👥 Social Features
- **Voting System**: Upvote and downvote stories
- **View Tracking**: Track story popularity with view counts
- **Social Sharing**: Share stories on WhatsApp, Twitter, and Facebook
- **Author Profiles**: Track stories by specific authors
- **Comments System**: (Coming soon) Community discussions

### 📊 Analytics
- **Platform Statistics**: View total stories, authors, views, and likes
- **Category Distribution**: Visual breakdown of content by category
- **Engagement Metrics**: Track user interaction and story performance

### 🎨 Design
- **Modern Dark Theme**: Eye-friendly dark interface with accent colors
- **Glass Morphism**: Modern UI elements with backdrop blur effects
- **Gradient Animations**: Beautiful hover effects and transitions
- **Telugu Typography**: Optimized fonts for Telugu text rendering
- **Accessibility**: High contrast colors and keyboard navigation support

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/telugu-stories.git
cd telugu-stories
```

2. **Install dependencies**
```bash
pip install streamlit
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the application**
Open your browser and navigate to `http://localhost:8501`

### Docker Installation (Optional)

1. **Build the Docker image**
```bash
docker build -t telugu-stories .
```

2. **Run the container**
```bash
docker run -p 8501:8501 telugu-stories
```

## 📁 Project Structure

```
telugu-stories/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── Dockerfile            # Docker configuration (optional)
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── assets/
    ├── styles.css        # Additional CSS styles
    └── images/           # Static images
```

## 🛠️ Configuration

### Streamlit Configuration
Create a `.streamlit/config.toml` file to customize the app:

```toml
[theme]
primaryColor = "#FF6B35"
backgroundColor = "#0F1419"
secondaryBackgroundColor = "#1A202C"
textColor = "#FFFFFF"

[server]
port = 8501
enableCORS = false
enableXsrfProtection = false
```

### Environment Variables
```bash
# Optional environment variables
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 📝 Usage Guide

### Adding a New Story

1. Click on **"➕ కథ వ్రాయండి"** (Write Story) button
2. Fill in the required fields:
   - **శీర్షిక** (Title): 3-100 characters
   - **రచయిత పేరు** (Author Name): Up to 50 characters
   - **విభాగం** (Category): Select from available categories
   - **కథ/రచన** (Story Content): Minimum 50 characters
   - **ట్యాగులు** (Tags): Optional, comma-separated
3. Click **"📝 కథ ప్రచురించండి"** (Publish Story)

### Searching Stories

- Use the search bar to find stories by title, author, content, or tags
- Select specific categories using the dropdown filter
- Combine search and category filters for precise results

### Interacting with Stories

- **👍 Upvote**: Like stories you enjoy
- **👎 Downvote**: Provide feedback on stories
- **📖 చదవండి** (Read): View the full story
- **📤 షేర్ చేయండి** (Share): Share on social media
- **💬 Comments**: Engage with the community (coming soon)

## 🔧 Customization

### Adding New Categories
Modify the `CATEGORIES` constant in the `TeluguStoriesApp` class:

```python
CATEGORIES = ["కథ", "చరిత్ర", "సంస్కృతి", "కవిత", "విజ్ఞానం", "ఇతర", "మీ కొత్త విభాగం"]
```

### Styling Customization
- Modify CSS variables in the `_load_custom_styles()` method
- Adjust colors, fonts, and animations to match your brand
- Add new CSS classes for custom components

### Content Validation
Customize validation rules in the `_validate_story_data()` method:

```python
MIN_TITLE_LENGTH = 3      # Minimum title length
MIN_CONTENT_LENGTH = 50   # Minimum content length
EXCERPT_LENGTH = 150      # Story excerpt length
```

## 🔒 Data Storage

Currently, the application uses Streamlit's session state for data storage. For production use, consider integrating:

- **Database Options**: PostgreSQL, MongoDB, SQLite
- **Cloud Storage**: Firebase, AWS S3, Google Cloud Storage
- **File Storage**: JSON files, CSV files

### Example Database Integration

```python
import sqlite3

def save_story_to_db(story_data):
    conn = sqlite3.connect('stories.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO stories (title, author, content, category, tags, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (story_data['title'], story_data['author'], story_data['content'], 
          story_data['category'], json.dumps(story_data['tags']), 
          story_data['created_at']))
    conn.commit()
    conn.close()
```

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Heroku Deployment
1. Create a `requirements.txt` file:
```
streamlit==1.28.0
```

2. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

3. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🤝 Contributing

We welcome contributions from the Telugu community! Here's how you can help:

### Reporting Issues
- Use GitHub Issues to report bugs
- Provide detailed descriptions and screenshots
- Include steps to reproduce the problem

### Feature Requests
- Suggest new features through GitHub Issues
- Explain the use case and expected behavior
- Consider the impact on existing users

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Translation Support
Help translate the interface to other languages:
- English translations welcome
- Regional Telugu variations
- Other Indian languages

## 📋 Roadmap

### Upcoming Features
- [ ] User authentication and profiles
- [ ] Comment system with moderation
- [ ] Story rating and review system
- [ ] Advanced search with filters
- [ ] Story collections and playlists
- [ ] Mobile app version
- [ ] Audio narration support
- [ ] Print-friendly story formats
- [ ] Author verification system
- [ ] Content moderation tools

### Technical Improvements
- [ ] Database integration
- [ ] Performance optimizations
- [ ] SEO enhancements
- [ ] Progressive Web App (PWA)
- [ ] Offline reading capability
- [ ] Multi-language support
- [ ] API development
- [ ] Admin dashboard
- [ ] Analytics integration
- [ ] Automated testing

## 🐛 Troubleshooting

### Common Issues

**1. Font rendering issues**
- Ensure Google Fonts are loading properly
- Check internet connection
- Clear browser cache

**2. Stories not saving**
- Check form validation messages
- Ensure all required fields are filled
- Verify character limits

**3. Search not working**
- Try different keywords
- Check spelling in Telugu
- Use English transliteration

**4. Styling issues**
- Clear browser cache
- Try in incognito/private mode
- Update your browser

### Performance Tips
- Limit the number of stories displayed per page
- Optimize images and media files
- Use efficient data structures
- Implement lazy loading for large datasets

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Email**: support@telugukathas.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/telugu-stories/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/telugu-stories/discussions)

## 🙏 Acknowledgments

- Telugu Unicode Consortium for character encoding standards
- Google Fonts for Telugu typography support
- Streamlit community for the amazing framework
- Telugu literature enthusiasts and beta testers
- Open source contributors and maintainers

## 📊 Statistics

- **Language**: Python 3.7+
- **Framework**: Streamlit 1.28+
- **UI Components**: Custom CSS with Glass Morphism
- **Typography**: Noto Sans Telugu, Poppins
- **Browser Support**: Chrome, Firefox, Safari, Edge
- **Mobile Support**: Responsive design

---

**మీ కథలతో తెలుగు సాహిత్యాన్ని సమృద్ధం చేయండి! 🌟**

*Made with ❤️ for the Telugu community*
