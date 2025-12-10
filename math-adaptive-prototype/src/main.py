# main.py

import time
from tracker import Tracker          # created tracker.py
from engine import AdaptiveEngine    # created engine.py
from puzzles import generate_puzzle  # created puzzles.py


def choose_initial_level() -> str:
    choices = {"1": "easy", "2": "medium", "3": "hard"}
    print("Choose initial difficulty:")
    print("1) Easy  2) Medium  3) Hard")

    while True:
        c = input("Enter 1/2/3: ").strip()
        if c in choices:
            return choices[c]
        print("Invalid choice — try 1, 2, or 3")


def run_session(name: str, initial_level: str, n_questions: int = 10):
    tracker = Tracker()
    engine = AdaptiveEngine(window=5)
    current_level = initial_level
    history_levels = [current_level]

    print(f"\nStarting session for {name}. Initial level: {current_level}\n")

    for i in range(1, n_questions + 1):
        q, ans = generate_puzzle(current_level)
        print(f"Q{i} [{current_level.title()}]: {q} = ?")

        start = time.perf_counter()
        resp = input("Your answer: ").strip()
        end = time.perf_counter()

        try:
            given = float(resp)
        except Exception:
            given = float('nan')

        t = end - start
        tracker.add_record(q, ans, given, t)

        last_stats = tracker.last_n_stats(engine.window)
        next_level = engine.decide_next(
            current_level,
            last_stats["accuracy"],
            last_stats["avg_time"]
        )

        # feedback to learner
        correct_flag = tracker.records[-1]["correct"]
        print("Correct!" if correct_flag else f"Incorrect — answer: {ans}")

        if next_level != current_level:
            print(f"Difficulty changed: {current_level} -> {next_level}\n")
            current_level = next_level
            history_levels.append(current_level)
        else:
            print()

    # SUMMARY
    acc = tracker.accuracy()
    avg_t = tracker.average_time()

    print("Session summary")
    print("---------------")
    print(f"Total questions: {len(tracker.records)}")
    print(f"Accuracy: {acc*100:.1f}%")
    print(f"Average time: {avg_t:.2f} s")
    print(f"Difficulty transitions: {history_levels}")

    # Save log
    fname = f"session_{name.replace(' ', '_')}.csv"
    tracker.save_csv(fname)
    print(f"Saved session log to {fname}")


if __name__ == "__main__":
    print("Adaptive Math Prototype — console")
    name = input("Enter learner name: ").strip() or "kid"
    initial = choose_initial_level()
    run_session(name, initial, n_questions=12)
