import sys
import os

try:
    test_name = sys.argv[1]

except:
    print("Usage: ./generator {test_name}")
    exit()

os.system(f"mkdir tests/{test_name}")

template_file = open("template/test.py")
template = template_file.read()
template_file.close()

template_json_file = open("template/settings.json")
template_json = template_json_file.read()
template_json_file.close()

test_file = open(f"tests/{test_name}/test.py", "w")
test_file.write(template)
test_file.close()

json_file = open(f"tests/{test_name}/settings.json", "w")
json_file.write(template_json)
json_file.close()