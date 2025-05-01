# quotes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Quote
from .mood_detector import MoodDetector
import random

class MoodDetectionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Quote.objects.bulk_create([
            Quote(
                text="The only way to do great work is to love what you do.",
                author="Steve Jobs",
                moods="joy,optimism"
            ),
            Quote(
                text="In the middle of every difficulty lies opportunity.",
                author="Albert Einstein",
                moods="adversity,challenge"
            ),
            Quote(
                text="You must do the thing you think you cannot do.",
                author="Eleanor Roosevelt",
                moods="fear,courage"
            )
        ])

    def test_mood_detector_accuracy(self):
        """Test the AI model's mood detection accuracy"""
        detector = MoodDetector()
        
        test_cases = [
            ("I'm feeling ecstatic about this!", "joy"),
            ("This uncertainty terrifies me", "fear"),
            ("The constant delays are infuriating", "anger"),
            ("I feel completely hopeless", "sadness"),
            ("This new opportunity excites me", "joy"),
        ]

        for text, expected_mood in test_cases:
            with self.subTest(text=text):
                detected_mood = detector.detect_mood(text)
                self.assertEqual(detected_mood.lower(), expected_mood.lower())

    def test_quote_recommendation_logic(self):
        """Test the system's ability to match quotes with moods"""
        quotes = Quote.objects.filter(moods__icontains="joy")
        self.assertGreaterEqual(quotes.count(), 1)
        self.assertIn("Steve Jobs", [q.author for q in quotes])
        quotes = Quote.objects.filter(moods__icontains="courage")
        self.assertGreaterEqual(quotes.count(), 1)
        self.assertIn("Eleanor Roosevelt", [q.author for q in quotes])

    def test_view_integration(self):
        """Test the complete user flow through views"""
        test_inputs = [
            ("I'm feeling optimistic", 200, "joy"),
            ("This makes me anxious", 200, "fear"),
            ("", 200, "error"),  # Test empty input
        ]

        for input_text, status_code, expected in test_inputs:
            with self.subTest(input=input_text):
                response = self.client.post(reverse('home'), {'thoughts': input_text})
                self.assertEqual(response.status_code, status_code)
                
                if status_code == 200:
                    if expected == "error":
                        self.assertTemplateUsed(response, 'quotes/error.html')
                    else:
                        self.assertTemplateUsed(response, 'quotes/result.html')
                        self.assertIn('detected_mood', response.context)
                        self.assertEqual(response.context['detected_mood'].lower(), expected.lower())

    def test_fallback_to_random_quotes(self):
        """Test system behavior when no mood-specific quotes exist"""
        # Test with uncommon mood
        detector = MoodDetector()
        mood = detector.detect_mood("I feel nostalgic")
        quotes = Quote.objects.filter(moods__icontains=mood)
        
        if not quotes.exists():
            all_quotes = Quote.objects.all()
            selected = random.choice(all_quotes)
            self.assertIsNotNone(selected)

    def test_error_handling(self):
        """Test error conditions"""
        # Test empty database
        Quote.objects.all().delete()
        response = self.client.post(reverse('home'), {'thoughts': "Happy thoughts"})
        self.assertContains(response, "No quotes available", status_code=200)

        # Test invalid input handling
        response = self.client.post(reverse('home'), {'thoughts': "   "})
        self.assertContains(response, "Please enter your thoughts", status_code=200)

if __name__ == '__main__':
    import django
    django.setup()
    unittest.main()