'''hbtbgpylint '''

import matplotlib.pyplot as plt
import pandas as pd

salaries= pd.read_csv("Data Science Jobs Salaries.csv")

#подсчетколичтсва сотрудников с разным уровнем опыта для каждого типа трудоустройства
kol1=salaries.loc[salaries["employment_type"]=="FT"]
kol2=salaries.loc[salaries["employment_type"]=="CT"]
kol3=salaries.loc[salaries["employment_type"]=="PT"]


kol1_1=kol1.loc[kol1["experience_level"]=="EN"]
kol1_2=kol1.loc[kol1["experience_level"]=="SE"]
kol1_3=kol1.loc[kol1["experience_level"]=="EX"]
kol1_4=kol1.loc[kol1["experience_level"]=="MI"]


kol2_1=kol2.loc[kol2["experience_level"]=="EN"]
kol2_2=kol2.loc[kol2["experience_level"]=="SE"]
kol2_3=kol2.loc[kol2["experience_level"]=="EX"]
kol2_4=kol2.loc[kol2["experience_level"]=="MI"]


kol3_1=kol3.loc[kol3["experience_level"]=="EN"]
kol3_2=kol3.loc[kol3["experience_level"]=="SE"]
kol3_3=kol3.loc[kol3["experience_level"]=="EX"]
kol3_4=kol3.loc[kol3["experience_level"]=="MI"]

values1=[len(kol1_1),len(kol1_2),len(kol1_3),len(kol1_4)]
values2=[len(kol2_1),len(kol2_2),len(kol2_3),len(kol2_4)]
values3=[len(kol3_1),len(kol3_2),len(kol3_3),len(kol3_4)]

#подсчет средней зарплаты в долларах для каждого размера компании
sal1=salaries.loc[salaries["company_size"]=="L"]
sal2=salaries.loc[salaries["company_size"]=="S"]
sal3=salaries.loc[salaries["company_size"]=="M"]


sal1_=sal1['salary_in_usd'].mean()
sal2_=sal2["salary_in_usd"].mean()
sal3_=sal3["salary_in_usd"].mean()
sal=[sal1_,sal2_,sal3_]

index=['EN','SE','EX','MI']
index_=['L','S','M']

#строим графики
fig, axes = plt.subplots(2,2)
axes[0][0].set_title('Experience for FT')
axes[0][0].bar(index,values1)
axes[0][1].set_title('Experience for CT')
axes[0][1].bar(index,values2)
axes[1][0].set_title('Experience for PT')
axes[1][0].bar(index,values3)
axes[1][1].set_title('Average salary ')
axes[1][1].bar(index_,sal)


plt.show()
