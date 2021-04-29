import time

dict_a = {
    "직업": "전사",
    "무기": "검",
    "체력": "120",
    "공격력": "50"
}
dict_b ={
    "직업": "궁수",
    "무기": "활",
    "체력": "100",
    "공격력": "60"
}
dict_c ={
    "직업": "법사",
    "무기": "지팡이",
    "체력": "80",
    "공격력": "70"
}

print("게임을 시작합니다.")	
time.sleep(1)
a='1'
while a == '1'  :
    print("1.직업 능력치 정보보기 2.직업 선택")
    # "1.",dict_a["직업"], 
    # "2.",dict_b["직업"], 
    # "3.",dict_c["직업"],
    # "4. 직업 능력치 정보")
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
a_1= 50
time.sleep(0.5)
print("1-1단계 몬스터(HP50)")
while a_1 > 0 :
    time.sleep(1)
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(a_1 <= int(power)) :
            a_1 = a_1 - int(power)
            print("1-1단계를 클리어 하셨습니다")
            print("클리어보상 : 1.공격력+5 2.HP+10")
            c = input()
            if (c == '1') :
                power = int(power) + 5
            elif (c == '2') :
                hp = int(hp) + 10
        elif (a_1>int(power)) :
            a_1 = a_1 - int(power)
            print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n  남은체력:",a_1)

a_2 = 70
print("1-2단계 몬스터(HP70)")
while a_2 > 0 :
    time.sleep(1)
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(a_2 <= int(power)) :
            a_2 = a_2 - int(power)
            print("1-2단계를 클리어 하셨습니다")
            print("클리어보상 : 1.공격력+7 2.HP+14")
            c = input()
            if (c == '1') :
                power = int(power) + 7
            elif (c == '2') :
                hp = int(hp) + 14
        elif (a_2>int(power)) :
            a_2 = a_2 - int(power)
            print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n남은체력:",a_2)
time.sleep(1)
a_3 = 500
print("1-3단계 BOSS")
while a_3 > 0 :
    time.sleep(0.5)
    print("1.공격 2.회피")
    b = input()
    if(b == '1') :
        if(a_3 <= int(power)) :
            a_3 = a_3 - int(power)
            print("1-3단계를 클리어 하셨습니다")
            time.sleep(1)
            print("클리어보상 : 1.공격력+10 2.HP+20")
            c = input()
            if (c == '1') :
                power = int(power) + 10
            elif (c == '2') :
                hp = int(hp) + 20
        elif (a_3>int(power)) :
            a_3 = a_3 - int(power)
            print("몬스터에게",power,"만큼의 데미지가 들어갔습니다\n남은체력:",a_3)







# print("1.공격 2.회피")
# at = input()
# print("1.도망간다 2.아이템쓴다 3.싸운다 : ")
# number = int(input("숫자를 입력하세요: "))
# # 유저가 입력한 글자를 출력
# if number == 1:
#     print("")
# if number == 2:
# if number == 3: