import importlib
import os

for test in os.listdir("tests/"):
    print(test + " - ", end="")
    importlib.import_module(f"tests.{test}.test")