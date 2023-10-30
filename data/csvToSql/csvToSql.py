import pandas as pd

# CSV 파일을 데이터프레임으로 읽기
df = pd.read_csv('')

# CREATE TABLE 문 생성
create_table_sql = """
    CREATE TABLE 테이블이름 (
       
    )
"""

# INSERT 문 생성
insert_sql = ""

for index, row in df.iterrows():
    values = f"INSERT INTO 테이블이름 (테이블속성리스트) VALUES "
    values += f"('{row['속성1']}', '{row['속성2']}', TO_DATE('{row['속성3:날짜인경우']}', 'YYYY.MM.DD'), TO_DATE('{row['속성4:날짜인경우']}', 'YYYY.MM.DD'), {row['속성5']}, {row['속성6']});\n"

    insert_sql += values

# SQL 파일에 쓰기
with open('insert_테이블이름.sql', 'w') as file:
    file.write(create_table_sql + '\n')
    file.write(insert_sql)