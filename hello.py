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
print("직업을 선택하세요: ",
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


# print("1.도망간다 2.아이템쓴다 3.싸운다 : ")		
# number = int(input("숫자를 입력하세요: "))		
# # 유저가 입력한 글자를 출력				
# if number == 1:			
#     print("")
# if number == 2:		
		

# if number == 3:		