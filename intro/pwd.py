import re

def is_valid_password(password: str) -> bool:
    # 정규표현식 기반 각 조건 체크
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit     = re.search(r'[0-9]', password)
    has_symbol    = re.search(r'[^a-zA-Z0-9]', password)

    return all([has_lowercase, has_uppercase, has_digit, has_symbol])

# 사용자 입력 받기
password = input("비밀번호를 입력하세요: ")

# 유효성 검사 결과 출력
if is_valid_password(password):
    print("✅ 유효한 비밀번호입니다.")
else:
    print("❌ 비밀번호는 다음 조건을 모두 만족해야 합니다:")
    print("- 영문 소문자 포함 (a-z)")
    print("- 영문 대문자 포함 (A-Z)")
    print("- 숫자 포함 (0-9)")
    print("- 특수문자 포함 (!, @, #, ...)")