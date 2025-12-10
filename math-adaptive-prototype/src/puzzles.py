"""
puzzle_generator.py
Generate simple math puzzles at three difficulty levels.
"""

import random
from typing import Tuple


def generate_puzzle(difficulty: str) -> Tuple[str, float]:
    """
    Return (question_str, correct_answer).

    difficulty: 'easy' | 'medium' | 'hard'
    """
    if difficulty == "easy":
        # single-digit add/sub
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        op = random.choice(["+", "-"])

        if op == "+":
            return f"{a} + {b}", a + b
        else:
            return f"{a} - {b}", a - b

    elif difficulty == "medium":
        # small multiplication or two-digit add/sub
        op = random.choice(["+", "-", "*"])

        if op == "*":
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            return f"{a} * {b}", a * b
        else:
            a = random.randint(0, 50)
            b = random.randint(0, 50)

            if op == "+":
                return f"{a} + {b}", a + b
            else:
                return f"{a} - {b}", a - b

    elif difficulty == "hard":
        # two-digit multiplication, integer division, or harder +/-
        op = random.choice(["*", "/", "+", "-"])

        if op == "*":
            a = random.randint(10, 99)
            b = random.randint(2, 9)
            return f"{a} * {b}", a * b

        elif op == "/":
            # ensure clean integer division
            b = random.randint(2, 9)
            quotient = random.randint(5, 20)
            a = b * quotient
            return f"{a} / {b}", quotient

        else:
            a = random.randint(50, 200)
            b = random.randint(0, 200)
            if op == "+":
                return f"{a} + {b}", a + b
            else:
                return f"{a} - {b}", a - b

    else:
        raise ValueError("Unknown difficulty")
