import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:\\Users\\AMD\\Desktop\\data\\loan_data_verified.csv')

# Различия в доходах между высокообразованными и не обладающими высшим образованием заявителями.

plt.figure(figsize=(10, 6))
sns.boxplot(x='Education', y='ApplicantIncome', data=df)
plt.title('Распределение доходов заявителей по уровню образования')
plt.xlabel('Уровень образования')
plt.ylabel('Доход заявителя')
plt.show()
