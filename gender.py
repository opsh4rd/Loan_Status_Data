import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:\\Users\\AMD\\Desktop\\data\\loan_data_verified.csv')

loans = pd.DataFrame(df)

gender_counts = df['Gender'].value_counts()

# Соотношение мужчин и женщин

plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Соотношение мужчин и женщин')
plt.show()
