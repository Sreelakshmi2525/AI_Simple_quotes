# Mood-Based Quote Generator with AI Integration

A Django web application that detects user emotions using AI and suggests inspirational quotes accordingly.

## Features

- **AI-Powered Mood Detection**: Utilizes `roberta-base-go_emotions` model for nuanced emotion recognition
- **Dynamic Quote Suggestions**: Curated quotes across emotional states
- **Responsive UI**: Modern design with smooth animations and mobile compatibility
- **Error Handling**: Graceful error recovery and user feedback
- **Smart Fallbacks**: Default quotes when no mood-specific matches exist
- **Caching**: Redundant model loading with 15-minute cache

## Technologies

- **Backend**: Django 5.1
- **AI Model**: `j-hartmann/emotion-english-distilroberta-base`
- **NLP**: Hugging Face Transformers
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3 (Glassmorphism design)

## Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/quote-generator.git
   cd quote-generator
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   python manage.py migrate
   python manage.py load_quotes
   ```

## Configuration

1. **Environment Variables** (`.env`)
   ```ini
   HF_HUB_DISABLE_SYMLINKS_WARNING=1
   ```

2. **Static Files** (Add to `settings.py`)
   ```python
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'quotes/static')]
   ```

## Usage

1. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

2. **Access Application**
   ```
   http://localhost:8000
   ```

3. **Input Thoughts**
   ```
   Example: "I'm feeling optimistic about new opportunities"
   ```

4. **View Results**
   - Detected mood display
   - Contextual quote suggestion
   - Option to try again

## Project Structure

```
quoteapp/
├── quotes/
│   ├── management/
│   ├── migrations/
│   ├── templates/
│   ├── mood_detector.py  # AI integration
│   └── views.py          # Core logic
├── quoteapp/
│   └── settings.py       # Configuration
└── db.sqlite3            # Database
```

## Testing

1. **Run Test Suite**
   ```bash
   python manage.py test quotes.tests --verbosity=2
   ```

2. **Manual Testing**
   ```python
   # Django Shell
   from quotes.mood_detector import MoodDetector
   detector = MoodDetector()
   print(detector.detect_mood("I feel accomplished!"))  # Should return 'joy'
   ```

## Credits

- Emotion Detection Model: [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- Django Template Structure: [Django Best Practices](https://docs.djangoproject.com)
- UI Inspiration: [Glassmorphism Trend](https://ui.glass)

## License

MIT License - See [LICENSE](LICENSE) for details

---

##  Author  
🔗 [GitHub Profile](https://github.com/Sreelakshmi2525)

---

**Note**: Requires Python 3.8+ | Optimized for CPU usage | Model size: ~500MB
