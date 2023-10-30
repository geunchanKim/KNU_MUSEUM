import pandas as pd

# CSV 파일을 데이터프레임으로 읽기
df = pd.read_csv('museumprogramlist_info.csv')

# CREATE TABLE 문 생성
create_table_sql = """
    CREATE TABLE MUSEUM_PROGRAM_LIST (
        EduID VARCHAR2(10) NOT NULL,
	    Title VARCHAR2(100) NOT NULL,
	    StartDate DATE NOT NULL,
	    EndDate DATE NOT NULL,
	    Time INT,
	    LimitNum INT NOT NULL,
	    MadminID VARCHAR(15) NOT NULL,
	    PRIMARY KEY (EduId),
	    FOREIGN KEY (MadminID) REFERENCES ADMIN(AdminID) ON DELETE SET null
    )
"""

# INSERT 문 생성
insert_sql = ""

for index, row in df.iterrows():
    values = f"INSERT INTO MUSEUM_PROGRAM_LIST (EduID, Title, StartDate, EndDate, Time, LimitNum, MadminID) VALUES "
    values += f"('{row['EduID']}', '{row['Title']}', TO_DATE('{row['Start_date']}', 'YYYY.MM.DD'), TO_DATE('{row['End_date']}', 'YYYY.MM.DD'), {row['Time']}, {row['LimitNum']}, {row['MadminID']});\n"

    insert_sql += values

# SQL 파일에 쓰기
with open('insert_MUSEUM_PROGRAM_LIST.sql', 'w') as file:
    file.write(create_table_sql + '\n')
    file.write(insert_sql)