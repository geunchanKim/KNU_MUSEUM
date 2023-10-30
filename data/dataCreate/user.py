import random
import pandas as pd
import names

def get_rand_name():
    last_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", 
                  "한", "오", "서", "신", "권", "황", "안", "송", "류", "전", 
                  "홍", "고", "문", "양", "손", "배", "조", "백", "허", "유", 
                  "남", "심", "노", "정", "하", "곽", "성", "차", "주", "우",
                  "남궁", "황보", "제갈", "사공", "선우", "서문", "독고"]

    first_names = ["강", "건", "경", "고", "관", "나", "남", "노", "누", "다",
                   "단", "담", "대", "덕", "도", "동", "라", "래", "로", "루", 
                   "마", "만", "명", "무", "문", "미", "민", "백", "범", "별", 
                   "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", 
                   "아", "안", "애", "엄", "영", "예", "오", "옥", "완", "요", 
                   "자", "장", "재", "전", "정", "조", "종", "주", "준", "지", 
                   "찬", "창", "채", "천", "철", "초", "춘", "복", "치", "탐", 
                   "태", "택", "하", "한", "해", "혁", "현", "형", "혜", "호"]
    
    last_name = random.choice(last_names) # Last name 생성
    first_name = "".join(random.sample(first_names, 2)) # First name 생성     
    full_name = last_name + first_name # Full name 생성
    
    return full_name

def get_rand_phone_number():
    numbers = "0123456789"
    num1 = "".join(random.sample(numbers, 4))
    num2 = "".join(random.sample(numbers, 4))
    
    phone_num = "010-{0}-{1}".format(num1, num2)
    
    return phone_num

def get_rand_member_ID():
    digit = random.randint(1000, 9999)
    member_ID = "user" + str(digit)
    
    return member_ID

def get_rand_email_password():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    first_name = names.get_first_name()
    domain = random.choice(domains)
    random_number = random.randint(1000, 9999)
    
    email = first_name.lower() + "@" + domain
    password = first_name + str(random_number)
    return email, password

user_infos = []

generated_names = set()
generated_phone_numbers = set()
generated_member_ids = set()
generated_emails = set()
generated_password = set()

for k in range(1000):
    while True:
        name = get_rand_name()
        phone_number = get_rand_phone_number()
        member_ID = get_rand_member_ID()
        email, password = get_rand_email_password()
        
        if email not in generated_emails and name not in generated_names and phone_number not in generated_phone_numbers \
            and member_ID not in generated_member_ids and password not in generated_password:
            generated_emails.add(email)
            generated_names.add(name)
            generated_phone_numbers.add(phone_number)
            generated_member_ids.add(member_ID)
            generated_password.add(password)
            break
    
    user_infos.append([member_ID, password, name, email, phone_number])

columns_name = ['UserID', 'Password', 'Name', 'Email', 'PNumber']
df = pd.DataFrame(user_infos, columns=columns_name)

csv_file_name = "user_info.csv"
df.to_csv(csv_file_name, index=False)