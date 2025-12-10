"""
tracker.py
Track per-question performance and aggregate stats.
"""

import time
from typing import List, Dict, Any
import csv


class Tracker:
    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def add_record(self, question: str, correct_answer: float,
                   given_answer: float, time_taken: float):
        record = {
            "question": question,
            "correct_answer": correct_answer,
            "given_answer": given_answer,
            "correct": float(given_answer) == float(correct_answer),
            "time_taken": time_taken,
        }
        self.records.append(record)

    def accuracy(self) -> float:
        if not self.records:
            return 0.0
        return sum(1 for r in self.records if r["correct"]) / len(self.records)

    def average_time(self) -> float:
        if not self.records:
            return 0.0
        return sum(r["time_taken"] for r in self.records) / len(self.records)

    def last_n_stats(self, n: int = 5) -> Dict[str, float]:
        slice_ = self.records[-n:]
        if not slice_:
            return {"accuracy": 0.0, "avg_time": 0.0}

        acc = sum(1 for r in slice_ if r["correct"]) / len(slice_)
        avg_t = sum(r["time_taken"] for r in slice_) / len(slice_)
        return {"accuracy": acc, "avg_time": avg_t}

    def save_csv(self, path: str):
        keys = ["question", "correct_answer", "given_answer", "correct", "time_taken"]

        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()

            for r in self.records:
                # convert boolean to int for CSV clarity
                rr = r.copy()
                rr["correct"] = int(rr["correct"])
                writer.writerow(rr)
