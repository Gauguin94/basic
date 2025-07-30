def main():
    while True:
        user_input = input("입력하세요 (!quit 입력 시 종료): ")
        if user_input.strip().lower() == "!quit":
            print("프로그램을 종료합니다.")
            break
        print("입력한 내용:", user_input)

if __name__ == "__main__":
    main()