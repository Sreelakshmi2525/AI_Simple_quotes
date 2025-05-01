from transformers import pipeline
import numpy as np

class MoodDetector:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            device=-1,
            top_k=None  # Instead of return_all_scores=True
        )

    def detect_mood(self, text):
        results = self.classifier(text)
        return results[0][0]['label']  # Adjusted for new output format