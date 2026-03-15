import sys
from ai_review import review_code

if len(sys.argv) < 2:
    print("사용법: python main.py 파일이름")
    exit()

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    code = f.read()

result = review_code(code)

print(result)