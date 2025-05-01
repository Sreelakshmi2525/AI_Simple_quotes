from django.test import TestCase
from django.urls import reverse
from .models import Quote
from .mood_detector import MoodDetector
import random
from unittest.mock import patch

class MoodDetectionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Test data with varied moods
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
            ),
            Quote(
                text="When you feel hopeless, remember: night is always followed by dawn.",
                author="Unknown",
                moods="sadness,hope"
            )
        ])

    @patch('quotes.views.MoodDetector')
    def test_mood_detector_accuracy(self, mock_detector):
        """Test mood detection accuracy with mocked responses"""
        mock_instance = mock_detector.return_value
        test_cases = [
            ("I'm feeling ecstatic about this!", "joy"),
            ("This uncertainty terrifies me", "fear"),
            ("The constant delays are infuriating", "anger"),
            ("I feel completely hopeless", "sadness"),
            ("", "error")  # Test empty input
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                mock_instance.detect_mood.return_value = expected if expected != "error" else ""
                response = self.client.post(reverse('home'), {'thoughts': text})
                
                if expected == "error":
                    self.assertContains(response, "Please enter your thoughts")
                else:
                    self.assertContains(response, expected.capitalize())

    def test_quote_recommendation_logic(self):
        """Test quote filtering by mood tags"""
        # Test direct matches
        joy_quotes = Quote.objects.filter(moods__icontains="joy")
        self.assertEqual(joy_quotes.count(), 1)
        self.assertEqual(joy_quotes.first().author, "Steve Jobs")

        # Test partial matches
        courage_quotes = Quote.objects.filter(moods__icontains="courage")
        self.assertEqual(courage_quotes.count(), 1)
        self.assertEqual(courage_quotes.first().author, "Eleanor Roosevelt")

    def test_fallback_mechanisms(self):
        """Test system fallback behaviors"""
        # Test non-existent mood fallback
        quotes = Quote.objects.filter(moods__icontains="nostalgia")
        self.assertFalse(quotes.exists())
        
        # Should fallback to all quotes
        all_quotes = Quote.objects.all()
        self.assertGreaterEqual(all_quotes.count(), 3)

    def test_error_handling(self):
        """Test error scenarios"""
        # Test empty database
        Quote.objects.all().delete()
        response = self.client.post(reverse('home'), {'thoughts': "Happy"})
        self.assertContains(response, "No quotes available", status_code=200)

        # Test malformed input
        response = self.client.post(reverse('home'), {'thoughts': "   "})
        self.assertContains(response, "Please enter your thoughts", status_code=200)

    def test_response_templates(self):
        """Test correct template rendering"""
        # Test successful response
        response = self.client.post(reverse('home'), {'thoughts': "excited"})
        self.assertTemplateUsed(response, 'quotes/result.html')

        # Test error response
        response = self.client.post(reverse('home'), {'thoughts': ""})
        self.assertTemplateUsed(response, 'quotes/error.html')

if __name__ == '__main__':
    import django
    django.setup()
    import unittest
    unittest.main()