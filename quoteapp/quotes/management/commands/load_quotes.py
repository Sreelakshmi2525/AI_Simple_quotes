from django.core.management.base import BaseCommand
from quotes.models import Quote

QUOTES = [
    # Joy/Optimism
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "moods": "joy,optimism"
    },
    
    # Fear/Courage
    {
        "text": "You gain strength, courage, and confidence by every experience in which you really stop to look fear in the face.",
        "author": "Eleanor Roosevelt",
        "moods": "fear,courage"
    },

    # Anger/Forgiveness
    {
        "text": "Holding onto anger is like drinking poison and expecting the other person to die.",
        "author": "Buddha",
        "moods": "anger,forgiveness"
    },

    # Sadness/Hope
    {
        "text": "The wound is the place where the light enters you.",
        "author": "Rumi",
        "moods": "sadness,hope"
    },

    # Surprise/Curiosity
    {
        "text": "The most beautiful experience we can have is the mysterious.",
        "author": "Albert Einstein",
        "moods": "surprise,curiosity"
    },

    # Trust/Confidence
    {
        "text": "Trust yourself. You know more than you think you do.",
        "author": "Benjamin Spock",
        "moods": "trust,confidence"
    },

    # Disgust/Change
    {
        "text": "Be the change you wish to see in the world.",
        "author": "Mahatma Gandhi",
        "moods": "disgust,change"
    },

    # Anticipation/Excitement
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "moods": "anticipation,excitement"
    },

    # Love/Compassion
    {
        "text": "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.",
        "author": "Martin Luther King Jr.",
        "moods": "love,compassion"
    },

    # Guilt/Redemption
    {
        "text": "Mistakes are always forgivable, if one has the courage to admit them.",
        "author": "Bruce Lee",
        "moods": "guilt,redemption"
    },

    # Shame/Acceptance
    {
        "text": "You yourself, as much as anybody in the entire universe, deserve your love and affection.",
        "author": "Buddha",
        "moods": "shame,acceptance"
    },

    # Confusion/Clarity
    {
        "text": "The important thing is not to stop questioning. Curiosity has its own reason for existing.",
        "author": "Albert Einstein",
        "moods": "confusion,clarity"
    },

    # Loneliness/Connection
    {
        "text": "We are all in the gutter, but some of us are looking at the stars.",
        "author": "Oscar Wilde",
        "moods": "loneliness,connection"
    },

    # Stress/Calm
    {
        "text": "You must learn to let go. Release the stress. You were never in control anyway.",
        "author": "Steve Maraboli",
        "moods": "stress,calm"
    },

    {
        "text": "When you feel hopeless, remember: night is always followed by dawn.",
        "author": "Unknown",
        "moods": "sadness,hope"
    },
    {
        "text": "Tears are words that need to be written.",
        "author": "Paulo Coelho",
        "moods": "sadness,healing"
    },
    {
        "text": "No one ever told me that grief felt so like fear.",
        "author": "C.S. Lewis",
        "moods": "sadness,fear"
    },
    {
        "text": "The soul would have no rainbow if the eyes had no tears.",
        "author": "Native American Proverb",
        "moods": "sadness,wisdom"
    },
    {
        "text": "What we once enjoyed and deeply loved we can never lose, for all that we love deeply becomes part of us.",
        "author": "Helen Keller",
        "moods": "sadness,comfort"
    },
    {
        "text": "Joy is not the absence of suffering, but the presence of perspective.",
        "author": "Anonymous",
        "moods": "joy,resilience"
    },
    {
        "text": "The cave you fear to enter holds the treasure you seek.",
        "author": "Joseph Campbell",
        "moods": "fear,transformation"
    },
    {
        "text": "The fire that melts butter forges steel.",
        "author": "Sri Lankan Proverb",
        "moods": "anger,empowerment"
    },
    {
        "text": "Even the mightiest redwood was once a sapling that withstood storms.",
        "author": "Native American Wisdom",
        "moods": "sadness,renewal"
    },
    {
        "text": "The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.",
        "author": "Marcel Proust",
        "moods": "surprise,wonder"
    },
    {
        "text": "A bird sitting on a tree is never afraid of the branch breaking because its trust is not in the branch but in its own wings.",
        "author": "Unknown",
        "moods": "trust,growth"
    },
    {
        "text": "A bird sitting on a tree is never afraid of the branch breaking because its trust is not in the branch but in its own wings.",
        "author": "Unknown",
        "moods": "trust,growth"
    },
    {
        "text": "When you judge others, you don't define them - you define yourself.",
        "author": "Earl Nightingale",
        "moods": "disgust,empathy"
    },
    {
        "text": "The future is an infinite canvas waiting for the brush of our present choices.",
        "author": "Yoko Ono",
        "moods": "anticipation,creation"
    },
    {
        "text": "Love is not a mere feeling. It is the ultimate act of courage - to keep choosing connection despite the risk of loss.",
        "author": "Esther Perel",
        "moods": "love,perseverance"
    },
    {
        "text": "Our greatest glory is not in never falling, but in rising every time we fall.",
        "author": "Confucius",
        "moods": "guilt,evolution"
    },
    {
        "text": "Vulnerability is the birthplace of innovation, creativity and change.",
        "author": "Brené Brown",
        "moods": "shame,authenticity"
    },
    {
        "text": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein",
        "moods": "confusion,discovery"
    },
    {
        "text": "The quieter you become, the more you can hear.",
        "author": "Rumi",
        "moods": "loneliness,introspection"
    },
    {
        "text": "You can't stop the waves, but you can learn to surf.",
        "author": "Jon Kabat-Zinn",
        "moods": "stress,flow"
    },
    {
        "text": "We are all apprentices in a craft where no one becomes a master.",
        "author": "Ernest Hemingway",
        "moods": "nostalgia,progress"
    },
    {
        "text": "When you can't control what's happening, challenge yourself to control the way you respond to what's happening.",
        "author": "Unknown",
        "moods": "calm,focus"
    },
    {
        "text": "You are not your thoughts. You are the observer of them.",
        "author": "Unknown",
        "moods": "calm,clarity"
    },
    {
        "text": "Peace comes from within. Do not seek it without.",
        "author": "Buddha",
        "moods": "calm,reflection"
    },
    {
        "text": "Take a deep breath and let go of all the worries. You are in control of your peace.",
        "author": "Unknown",
        "moods": "calm,serenity"
    },
    {
        "text": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein",
        "moods": "calm,hope"
    },
    # Default Fallback
    {
        "text": "When you can't control what's happening, challenge yourself to control the way you respond to what's happening.",
        "author": "Unknown",
        "moods": "default"
    },

]

class Command(BaseCommand):
    help = 'Load initial quotes into database'

    def handle(self, *args, **kwargs):
        for quote in QUOTES:
            Quote.objects.create(**quote)
        self.stdout.write("Successfully loaded quotes")