import random

def generate_snippet(complexity):
    patterns = [
        lambda: f"AB{random.randint(10, 99)}CD",  # Simple pattern
        lambda: f"{random.choice('AEIOU')}123{random.choice('AEIOU')}",  # Moderate
        lambda: f"XX-{random.randint(100, 999)}-{random.randint(10, 99)}"  # Complex
    ]
    return patterns[min(complexity, len(patterns) - 1)]()
