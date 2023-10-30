import pandas as pd

# CSV 파일을 데이터프레임으로 읽기
df = pd.read_csv('user_info.csv')

# CREATE TABLE 문 생성
create_table_sql = """
    CREATE TABLE USER(
       	UserID VARCHAR(15) NOT NULL,
	    Password VARCHAR(20) NOT NULL,
	    Name VARCHAR(15) NOT NULL,
	    Email VARCHAR(30) NOT NULL,
	    PNumber VARCHAR(15) NOT NULL,
	    PRIMARY KEY(UserID)
    )
"""

# INSERT 문 생성
insert_sql = ""

for index, row in df.iterrows():
    values = f"INSERT INTO USER (UserID, Password, Name, Email, PNumber) VALUES "
    values += f"('{row['UserID']}', '{row['Password']}', {row['Name']}, {row['Email']}, {row['PNumber']});\n"

    insert_sql += values

# SQL 파일에 쓰기
with open('insert_USER.sql', 'w') as file:
    file.write(create_table_sql + '\n')
    file.write(insert_sql)