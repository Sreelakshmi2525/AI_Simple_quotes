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
            
            # Get quotes with fallback logic
            quotes = list(Quote.objects.filter(moods__icontains=mood).order_by('?'))
            
            if not quotes:
                quotes = list(Quote.objects.filter(moods__icontains="fallback").order_by('?'))
            
            if not quotes:
                quotes = list(Quote.objects.all().order_by('?'))
            
            # Final check for empty database
            if not quotes:
                return render(request, 'quotes/error.html', {
                    'error': "No quotes available in the database!"
                })
            
            # Select random quote from available options
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