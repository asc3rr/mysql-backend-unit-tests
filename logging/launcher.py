from importlib import import_module
import os

unit_tests = []

for file in os.listdir("tests/"):
    if ".py" in file:
        unit_tests.append(file)

for test in unit_tests:
    test = test.replace(".py", "")
    import_module(f"tests.{test}")