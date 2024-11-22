import os

from pathlib import Path


class Functions:
    @staticmethod
    def clean_up_cache():
        for p in Path(".").rglob("*.py[co]"):
            p.unlink()
        for p in Path(".").rglob("__pycache__"):
            p.rmdir()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")
