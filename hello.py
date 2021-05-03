
############### 게임 설명 #################
        ## 체력이 0될시 게임종료
        ## 캐릭터 회피 확률 66퍼
        ## 몬스터가 회피시 공격이 빗나갈확률 33퍼


import time ## 연속적으로 나오는 채팅 시간간격 주기위함
import random ## 회피를 하기위함
#### 함수 사용 ####
def attack() :
    print("몬스터가 공격을 준비하고 있습니다")
def miss() :
    print("몬스터가 회피를 준비하고 있습니다")
#### 딕셔너리 사용 ####
dict_a = {
    "직업": "전사",
    "무기": "검",
    "체력": 120,
    "공격력": 50
}
dict_b ={
    "직업": "궁수",
    "무기": "활",
    "체력": 100,
    "공격력": 60
}
dict_c ={
    "직업": "법사",
    "무기": "지팡이",
    "체력": 80,
    "공격력": 70
}

print("게임을 시작합니다.")	
time.sleep(1)
a='1'
while a == '1'  :
    print("1.직업 능력치 정보보기 2.직업 선택")
    a = input()
    time.sleep(1)
    if(a == '1') :
        print("직업 능력치 정보 : ",
        "1.",dict_a["직업"], 
        "2.",dict_b["직업"], 
        "3.",dict_c["직업"])
        job = input()
        time.sleep(0.5)
        if(job == '1') :
            for key in dict_a:
                print(key, ":", dict_a[key])
        elif(job == '2') :
            for key in dict_b:
                print(key, ":", dict_b[key])
        elif(job == '3') :
            for key in dict_c:
                print(key, ":", dict_c[key])             
time.sleep(1)
print("직업을 선택하세요 :",
    "1.",dict_a["직업"], 
    "2.",dict_b["직업"], 
    "3.",dict_c["직업"])
job = input()
time.sleep(1)
if(job == '1') :
    job = dict_a["직업"]
    print("현재 캐릭터 정보: ")
    # "\n직업:",
    # dict_a["name"],
    # "\n무기:",
    # dict_a["무기"],
    # "\n체력:",
    # dict_a["체력"],
    # "\n공격력:",
    # dict_a["공격력"]) 
    for key in dict_a:
        print(key, ":", dict_a[key])
elif(job == '2') :
    job = dict_b["직업"]
    print("현재 캐릭터 정보: ")
    # "\n직업:",
    # dict_b["직업"],
    # "\n무기:",
    # dict_b["무기"],
    # "\n체력:",
    # dict_b["체력"],
    # "\n공격력:",
    # dict_b["공격력"])
    for key in dict_b:
        print(key, ":", dict_b[key])

elif(job == '3') :
    job = dict_c["직업"]
    print("현재 캐릭터 정보: ")
    # "\n직업:",
    # dict_c["직업"],
    # "\n무기:",
    # dict_c["무기"],
    # "\n체력:",
    # dict_c["체력"],
    # "\n공격력:",
    # dict_c["공격력"])
    for key in dict_c:
        print(key, ":", dict_c[key])
else:
    print("잘못입력하셨습니다.")

if(job == dict_a["직업"]) :
    hp = dict_a["체력"]
    power = dict_a["공격력"]
elif(job == dict_b["직업"]) :
    hp = dict_b["체력"]
    power = dict_b["공격력"]
elif(job == dict_c["직업"]) :
    hp = dict_c["체력"]
    power = dict_c["공격력"]

## 1-1스테이지 정보
a_1hp = 50
a_1power = 10

time.sleep(0.5)
print("1-1단계 몬스터(HP50)")
while a_1hp > 0 and hp > 0:
    time.sleep(1)
    #### 리스트 사용 ####
    list = []
    ran_num = random.randint(0, 1)
    list.append(ran_num)
    list_a = []
    ran_g = random.randint(0, 2)
    list_a.append(ran_g)
    if(list == [0]) :
        attack()
    elif(list == [1]) :
        miss()
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(list == [0]) :
            hp = hp - a_1power
            print(a_1power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
            if(hp <= 0) :
                print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                break
            time.sleep(1)
            if(a_1hp <= power) :
                a_1hp = a_1hp - power
                print("몬스터에게", power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_1hp)
                time.sleep(0.5)
                print("1-1단계를 클리어 하셨습니다")
                time.sleep(0.5)
                print("클리어보상 : 1.공격력+5 2.HP+10")
                c = input()
                if (c == '1') :
                    power = power + 5
                elif (c == '2') :
                        hp = hp + 10
            elif (a_1hp > power) :
                a_1hp = a_1hp - power
                print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_1hp)
        elif(list == [1]) :
            if(list_a == [0]) :
                print("공격이 빗나갔습니다")
            elif(list_a == [1] or list_a == [2]): 
                if(a_1hp <= power) :
                    a_1hp = a_1hp - power
                    print("1-1단계를 클리어 하셨습니다")
                    print("클리어보상 : 1.공격력+5 2.HP+10")
                    c = input()
                    if (c == '1') :
                        power = power + 5
                    elif (c == '2') :
                        hp = hp + 10
                elif (a_1hp > power) :
                    a_1hp = a_1hp - power
                    print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_1hp)
    elif(b == '2') :
        if(list == [0]):
            if(list_a == [0] or list_a == [1]):
                print("공격을 회피 했습니다")
            elif(list_a == [2]):
                hp = hp - a_1power
                print("회피에 실패했습니다")
                print(a_1power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
                if(hp <= 0) :
                    print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                    break
        elif(list == [1]):
            print("아무일도 일어나지 않았습니다")
    time.sleep(1)
## 1-2스테이지정보
a_2hp = 70
a_2power = 20
print("1-2단계 몬스터(HP70)")
while a_2hp > 0 and hp > 0 :
    time.sleep(1)
    list = []
    ran_num = random.randint(0, 1)
    list.append(ran_num)
    list_a = []
    ran_g = random.randint(0, 2)
    list_a.append(ran_g)
    if(list == [0]) :
        attack()
    elif(list == [1]) :
        miss()
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(list == [0]) :
            hp = hp - a_2power
            print(a_2power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
            if(hp <= 0) :
                print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                break
            time.sleep(1)
            if(a_2hp <= power) :
                a_2hp = a_2hp - power
                print("몬스터에게", power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_2hp)
                time.sleep(0.5)
                print("1-2단계를 클리어 하셨습니다")
                time.sleep(0.5)
                print("클리어보상 : 1.공격력+7 2.HP+14")
                c = input()
                if (c == '1') :
                    power = power + 7
                elif (c == '2') :
                        hp = hp + 14
            elif (a_2hp > power) :
                a_2hp = a_2hp - power
                print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_2hp)
        elif(list == [1]) :
            if(list_a == [0]) :
                print("공격이 빗나갔습니다")
            elif(list_a == [1] or list_a == [2]): 
                if(a_2hp <= power) :
                    a_2hp = a_2hp - power
                    print("1-2단계를 클리어 하셨습니다")
                    print("클리어보상 : 1.공격력+7 2.HP+14")
                    c = input()
                    if (c == '1') :
                        power = power + 7
                    elif (c == '2') :
                        hp = hp + 14
                elif (a_2hp > power) :
                    a_2hp = a_2hp - power
                    print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_2hp)
    elif(b == '2') :
        if(list == [0]):
            if(list_a == [0] or list_a == [1]):
                print("공격을 회피 했습니다")
            elif(list_a == [2]):
                hp = hp - a_2power
                print("회피에 실패했습니다")
                print(a_2power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
                if(hp <= 0) :
                    print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                    break
        elif(list == [1]):
            print("아무일도 일어나지 않았습니다")
time.sleep(1)
## 1-3 스테이지 정보  
a_3hp = 500
a_3power = 40
print("1-3단계 BOSS(HP500)")
while a_3hp > 0 and hp > 0:
    time.sleep(1)
    list = []
    ran_num = random.randint(0, 1)
    list.append(ran_num)
    list_a = []
    ran_g = random.randint(0, 2)
    list_a.append(ran_g)
    if(list == [0]) :
        attack()
    elif(list == [1]) :
        miss()
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(list == [0]) :
            hp = hp - a_3power
            print(a_3power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
            if(hp <= 0) :
                print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                break
            time.sleep(1)
            if(a_3hp <= power) :
                a_3hp = a_3hp - power
                print("몬스터에게", power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_3hp)
                time.sleep(0.5)
                print("1-3단계를 클리어 하셨습니다")
                time.sleep(0.5)
                print("클리어보상 : 1.공격력+5 2.HP+10")
                c = input()
                if (c == '1') :
                    power = power + 5
                elif (c == '2') :
                        hp = hp + 10
            elif (a_3hp > power) :
                a_3hp = a_3hp - power
                print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_3hp)
        elif(list == [1]) :
            if(list_a == [0]) :
                print("공격이 빗나갔습니다")
            elif(list_a == [1] or list_a == [2]): 
                if(a_3hp <= power) :
                    a_3hp = a_3hp - power
                    print("1-3단계를 클리어 하셨습니다")
                    print("클리어보상 : 1.공격력+5 2.HP+10")
                    c = input()
                    if (c == '1') :
                        power = power + 5
                    elif (c == '2') :
                        hp = hp + 10
                elif (a_3hp > power) :
                    a_3hp = a_3hp - power
                    print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n몬스터 남은체력:",a_3hp)
    elif(b == '2') :
        if(list == [0]):
            if(list_a == [0] or list_a == [1]):
                print("공격을 회피 했습니다")
            elif(list_a == [2]):
                hp = hp - a_3power
                print("회피에 실패했습니다")
                print(a_3power,"만큼의 데미지를 입었습니다\n캐릭터 남은체력:",hp)
                if(hp <= 0) :
                    print("캐릭터가 사망 하였습니다 게임을 종료합니다")
                    break
        elif(list == [1]):
            print("아무일도 일어나지 않았습니다")
time.sleep(1)




