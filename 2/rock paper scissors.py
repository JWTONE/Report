import random

rsp = ['가위','바위','보']
c_pick = random.choice(rsp)

draws = 0
wins = 0
loses = 0

while True:
        tu_rsp = random.choice(rsp)
        print ("앗! 야생의 튜터가 나타나 가위바위보를 제안합니다.")
        player = input('가위, 바위, 보 중 하나를 입력하세요. 도망가기(run) : ').lower()
        
        if player == 'run':
            print("성공적으로 도망쳤습니다.")
            print(f"승리 : {wins} 무승부 : {draws} 패배 : {loses}")
            print('게임을 종료합니다.')
            exit()
        if player not in rsp:
            print('튜터가 가위바위보를 지속적으로 요구한다.')
            continue
            
        if tu_rsp == player :
            print(f'사용자가 {player}!!, 튜터가 눈치를 살피더니 {tu_rsp}를 냈다!!')
            print("비겼습니다.")
            draws += 1
            print(f'현재 무승부 스코어 : {draws}')
            
        elif (tu_rsp == '바위' and player == '보') or (tu_rsp == '가위' and player == '바위') or (tu_rsp == '보' and player == '가위'):
            print(f'사용자가 {player}!!!, 튜터가 눈치를 살피더니 {tu_rsp}를 냈다!')
            print("효과는 뛰어났다! 승리했습니다!")
            wins += 1
            print(f'현재 승리 스코어 : {wins}')
            
        else:
            print(f'사용자가 {player}!..그런데 효과가 없다!, 튜터가 눈치를 살피더니 {tu_rsp}를 냈다!')
            print("숲으로 끌려가 강의를 받습니다...")
            loses += 1
            print(f'현재 패배 스코어 : {loses}')
            

        restart = input("다시 도전하시겠습니까? Y/N : ").lower()
        if restart == 'y':
            continue
        else:
            print(f"승리 : {wins} 무승부 : {draws} 패배 : {loses}")
            print('게임을 종료합니다.')
            exit()