import random

high_score = float(10) 

while True:
    random_number = random.randint(1, 100) # 1부터 100번까지 무작위 번호를 출력해줌
    attempts = 0

    while True:
        player = input("1에서 100 사이의 숫자를 입력하세요 (게임종료:end): ").lower() #대문자로 end를 사용할 수 있게 만듬
        if player == 'end':
            print("게임 종료. 다음에 또 만나요!")
            exit() # break문과 비슷하지만, 이건 아예 실행을 끌 수 있다.

        if not player.isdigit(): # .isdigit() 문자가 1개라도 있다면 False, 숫자로만 이루어졌다면 True를 반환한다.
            print("숫자를 입력하세요.")
            continue

        guess = int(player)

        if not 1 <= guess <= 100:
            print("유효한 범위 내의 숫자를 입력하세요")
            continue

        attempts += 1 # 시도횟수가 1씩 증가한다.

        if guess == random_number:
            print(f"정답입니다!! 시도 횟수: {attempts}")
            high_score = min(high_score, attempts)
            print(f"현재 최고 시도 횟수: {high_score}")
            break
        elif guess < random_number:
            print("UP!!")
        else:
            print("DOWN!!")

    # 게임 재시작 여부 확인
    restart = input("게임을 다시 시작하시겠습니까? (yes/no): ").lower()
    if restart == 'yes' or restart == 'y':
        high_score = min(high_score, attempts)
        print(f"이전 게임 최고 플레이 횟수: {high_score}")
        continue
    else:
        print("게임을 종료합니다. 이용해 주셔서 감사합니다.")
        exit()
