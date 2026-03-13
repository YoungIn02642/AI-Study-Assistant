from ai_review import review_code

print("코드를 입력하세요.")
print("입력이 끝나면 END 를 입력하세요.\n")

lines = []

while True:
    line = input()
    
    if line.strip() == "END":
        break
        
    lines.append(line)

code = "\n".join(lines)

result = review_code(code)

print("\nAI 분석 결과\n")
print(result)