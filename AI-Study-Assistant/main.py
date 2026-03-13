from ai_review import review_code

print("코드를 입력하세요 (끝나면 Enter 두 번)")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

code = "\n".join(lines)

result = review_code(code)

print("\nAI 분석 결과\n")
print(result)