import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('houses_to_rent.csv')

ser = df.rooms.value_counts()

total = df.rooms.count()

values = []

for x in ser:
    percent = 100*(x/total)
    values = values + [percent]

plt.bar(x=ser.keys(), height=values)

plt.xlabel("Rooms Per House")
plt.ylabel("Percent of Houses")

plt.show()



df2 = pd.read_csv('amazon.csv')

index = [2001, 2002, 2003, 2004, 2005, 2006, 2007]

acre = []
bahia = []
for i in index:
    year = df2[df2['year']==i]
    average = year[df2['state']=='Acre'].number.mean()
    acre = acre + [average]

for i in index: 
    year = df2[df2['year']==i]
    average = year[df2['state']=='Bahia'].number.mean()
    bahia = bahia + [average]


plt.plot(index, acre, label='Acre')
plt.plot(index, bahia, label='Bahia')

plt.title('Fires in Acre and Bahia')
plt.xlabel('Year')
plt.ylabel('Fires') 
plt.legend() 
plt.show()
