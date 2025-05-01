from django.shortcuts import render
from .models import Quote
from .mood_detector import MoodDetector
import random
def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('thoughts', '').strip()
        
        if not user_input:
            return render(request, 'quotes/error.html', {
                'error': "Please enter your thoughts before submitting!"
            })
        
        detector = MoodDetector()
        
        try:
            mood = detector.detect_mood(user_input)
            quotes = list(Quote.objects.filter(moods__icontains=mood).order_by('?'))  # Random ordering
            
            if not quotes:
                quotes = list(Quote.objects.filter(moods__icontains="fallback").order_by('?'))
            
            if not quotes:
                quotes = list(Quote.objects.all().order_by('?'))
            
            selected_quote = quotes[0] if quotes else None
            selected_quote = random.choice(quotes)
            return render(request, 'quotes/result.html', {
                'quote': selected_quote,
                'detected_mood': mood.capitalize(),
                'user_input': user_input
            })
            
        except Exception as e:
            return render(request, 'quotes/error.html', {
                'error': f"Error processing your request: {str(e)}"
            })
    
    return render(request, 'quotes/input.html')