import requests

def get_github_user_info(username: str, token: str = None):
    url = f"https://api.github.com/users/{username}"

    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"\n📌 GitHub 사용자 정보 ({username})")
        print(f"🧑‍💻 이름: {data.get('name')}")
        print(f"🔗 프로필 URL: {data.get('html_url')}")
        print(f"🏢 소속: {data.get('company')}")
        print(f"📍 위치: {data.get('location')}")
        print(f"✍️ 소개: {data.get('bio')}")
        print(f"📦 공개 저장소 수: {data.get('public_repos')}")
        print(f"👥 팔로워 수: {data.get('followers')}")
        print(f"👤 팔로잉 수: {data.get('following')}")
        print(f"📅 가입일: {data.get('created_at')}")
    elif response.status_code == 403:
        print("❌ API 요청 제한에 도달했거나 권한이 없습니다 (403 Forbidden).")
    elif response.status_code == 404:
        print(f"❌ 사용자 '{username}' 를 찾을 수 없습니다.")
    else:
        print(f"⚠️ 오류 발생 (Status code: {response.status_code})")

if __name__ == "__main__":
    user = input("GitHub 사용자명을 입력하세요: ")
    use_token = input("토큰이 있으면 붙여주세요 (없으면 엔터): ")
    get_github_user_info(user, token=use_token.strip() or None)