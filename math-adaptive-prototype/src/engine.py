# engine.py

LEVELS = ["easy", "medium", "hard"]

class AdaptiveEngine:
    def __init__(self, window=5):
        self.window = window
        self.time_thresholds = {
            "easy": 8,
            "medium": 12,
            "hard": 20
        }

    def decide_next(self, current_level, recent_accuracy, recent_avg_time):
        idx = LEVELS.index(current_level)

        # Rule 1 → Increase difficulty
        if recent_accuracy >= 0.8 and recent_avg_time <= self.time_thresholds[current_level]:
            if idx < len(LEVELS) - 1:
                return LEVELS[idx + 1]

        # Rule 2 → Decrease difficulty
        if recent_accuracy <= 0.5:
            if idx > 0:
                return LEVELS[idx - 1]

        # Otherwise → Keep same difficulty
        return current_level
