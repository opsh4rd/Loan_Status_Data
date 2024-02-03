import pandas as pd
import psycopg2
from io import StringIO

# подключения к базе данных
db_params = {
    'dbname': 'loan_status',
    'user': 'user',
    'password': '***',
    'host': 'localhost',
    'port': 5432
}

# Путь к CSV
csv_file_path = 'C:\\Users\\AMD\\Desktop\\data\\loan_data_verified.csv'


conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Создаем таблицу
create_table_query = '''
CREATE TABLE IF NOT EXISTS loan_data (
    id INT PRIMARY KEY,
    Loan_ID VARCHAR,
    Gender VARCHAR,
    Married VARCHAR,
    Dependents VARCHAR,
    Education VARCHAR,
    Self_Employed VARCHAR,
    ApplicantIncome INT,
    CoapplicantIncome FLOAT,
    LoanAmount FLOAT,
    Loan_Amount_Term FLOAT,
    Credit_History FLOAT,
    Property_Area VARCHAR,
    Loan_Status VARCHAR
)
'''
cursor.execute(create_table_query)
conn.commit()

# Чтение данных из CSV
df = pd.read_csv(csv_file_path)

# Преобразование данных
output = StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)

# Копирование данных в базу
copy_query = '''
COPY loan_data FROM STDIN WITH (FORMAT csv, DELIMITER '\t', NULL '')
'''
cursor.copy_expert(copy_query, output)
conn.commit()

# Закрываем курсор и соединение
cursor.close()
conn.close()
