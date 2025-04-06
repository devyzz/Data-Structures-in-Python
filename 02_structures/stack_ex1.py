# 괄호 여닫기

brackets = input("괄호 문자열을 입력하세요: ")
stack = []

for char in brackets:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if not stack:
            print("False")
            break
        stack.pop()
    else:
        print("허용되지 않은 문자입니다:", char)
        break
else:
    print("True" if not stack else "False")
