import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'Olympic_File.csv')
#___________________________________________________________________________________________
'''                                                              *** Average Medals Ages '''
Age_Data = data.copy()

class Age_Avg:
    
    def GOLD():
        Age_Data = pd.read_csv(r'Olympic_File.csv')
        
        Age_Data = Age_Data[['Age','Medal']]
        Age_Data.dropna(subset=['Medal','Age'], inplace=True)

        Age = Age_Data['Age'].astype(int)
        Age_Data['Age'] = Age

        flt = Age_Data['Medal'] == 'Gold'
        Age_Data = Age_Data[flt]
        Av_Gold = Age_Data['Age'].mean()

        print('Average Age Gold   Medal :','%.2f'%(Av_Gold))


    def SILVER():
        Age_Data = pd.read_csv(r'Olympic_File.csv')

        Age_Data = Age_Data[['Age','Medal']]
        Age_Data.dropna(subset=['Medal','Age'], inplace=True)

        Age = Age_Data['Age'].astype(int)
        Age_Data['Age'] = Age

        flt = Age_Data['Medal'] == 'Silver'
        Age_Data = Age_Data[flt]
        Av_Silver = Age_Data['Age'].mean()

        print('Average Age Silver Medal :','%.2f'%(Av_Silver))


    def Bronze():
        Age_Data = pd.read_csv(r'Olympic_File.csv')

        Age_Data = Age_Data[['Age','Medal']]
        Age_Data.dropna(subset=['Medal','Age'], inplace=True)

        Age = Age_Data['Age'].astype(int)
        Age_Data['Age'] = Age

        flt = Age_Data['Medal'] == 'Bronze'
        Age_Data = Age_Data[flt]
        Av_Bronze = Age_Data['Age'].mean()

        print('Average Age Bronze Medal :','%.2f'%(Av_Bronze),'\n',40 * '_')


Gold = Age_Avg.GOLD()
Silver = Age_Avg.SILVER()
Bronze = Age_Avg.Bronze()
#______________________________________________________________________________________
'''                                                                      *** Mostiest Hosted'''
Host_Data = data.copy()
Host_Data.drop(['Season','Name'] , axis=1 , inplace=True)
Host_Data['Sex'].replace(['M','F'],['Male','Female'],inplace=True)

data_Cities = Host_Data
data_Cities.drop_duplicates(['Year'],inplace=True)
Host_Data.sort_values('Year' , ascending=True , inplace=True) 

City,city={},[]
for i in Host_Data.index:
    City[data_Cities['City'].loc[i]] = City.get(data_Cities['City'].loc[i] , 0) + 1

X = 0
for k,v in City.items():
    if v >= 2:
        city.append((v,k))
    else:
        X +=1

city.append((1,'Other'))
city.sort(reverse=True)

for i in city:
    if i[1] == 'Other': 
        print(f'{i[1]:8} : {i[0]} Hosted ({X} City)')
    else:
        print(f'{i[1]:8} : {i[0]} Hosted')
#__________________________________________________________________________________         
'''                                                                      *** Top 12  Countries in Reaching Medals (Men,Women)'''
Data_Country = data.copy()
Data_Country.drop(['Season','City','Name'] , axis=1 , inplace=True)
Data_Country['Sex'].replace(['M','F'],['Male','Female'],inplace=True)
                                                        
Data_Country.dropna(subset=['Medal'],inplace=True) 

Male = Data_Country['Sex'] == 'Male'
data_Medal_Male = Data_Country[Male]

Female = Data_Country['Sex'] == 'Female'
data_Medal_Female = Data_Country[Female]


men_Teams = {}
for i in data_Medal_Male.index:
    men_Teams[data_Medal_Male['Team'].loc[i]] = men_Teams.get(data_Medal_Male['Team'].loc[i] , 0 ) + 1

Men_Teams = []
for k,v in men_Teams.items():
    if v >= 613:
        Men_Teams.append((v,k))

Men_Team = pd.DataFrame(Men_Teams,columns=('Num','Country'))
Men_Team.sort_values(['Num'],inplace=True)


females_Teams = {}
for i in data_Medal_Female.index:
    females_Teams[data_Medal_Female['Team'].loc[i]] = females_Teams.get(data_Medal_Female['Team'].loc[i] , 0 ) + 1

Females_Teams = []
for k,v in females_Teams.items():
    if v >= 299:
        Females_Teams.append((v,k))

Females_Team = pd.DataFrame(Females_Teams,columns=('Num','Country'))
Females_Team.sort_values(['Num'],inplace=True)

fig , (ax1,ax2) = plt.subplots(nrows=2 ,ncols=1)

ax1.plot(Men_Team['Country'],Men_Team['Num'],label='Men',color='red',marker='o' ,ms=6 ,mfc='c')           
ax2.plot(Females_Team['Country'] ,Females_Team['Num'] ,label='Women',color='c',marker='o' ,ms=6 ,mfc='r')

ax1.legend()
ax2.legend()  

ax1.grid()
ax2.grid()


ax1.set_ylabel('Number Of Medals')
ax2.set_ylabel('Number Of Medals')
plt.suptitle('Top 12 Countries in Medals')

plt.show()
#____________________________________________________________________________________________
'''                                                                        ***  Football Teams Champions (Men,Women)'''
DATA = data.copy()

data.drop(['Season','City','Name','Age'] , axis=1 , inplace=True)
data['Sex'].replace(['M','F'],['Male','Female'],inplace=True)

flt = (data['Sex'] == 'Male') & (data['Sport'] == 'Football') & (data['Medal'] == 'Gold')
data = data[flt]

data.drop_duplicates(['Year'], inplace=True)
data.sort_values('Year' , ascending=False ,inplace=True)


DATA.drop(['Season','City','Name','Age'] , axis=1 , inplace=True)
DATA['Sex'].replace(['M','F'],['Male','Female'],inplace=True)

flt = (DATA['Sex'] == 'Female') & (DATA['Sport'] == 'Football') & (DATA['Medal'] == 'Gold')
DATA = DATA[flt]

DATA.drop_duplicates(['Year'], inplace=True)
DATA.sort_values('Year' , ascending=False ,inplace=True)


fig ,(ax1,ax2) = plt.subplots(nrows=2 ,ncols=1 ,sharex=True)

ax1.plot(data['Year'],data['Team'],label='Men_Gold' , c='y' , marker='o' ,ms=4 ,mfc='hotpink')       
ax2.plot(DATA['Year'],DATA['Team'],label='Women_Gold' , c='y' , marker='o' ,ms=4 ,mfc='hotpink')
  
ax1.set_title('Men Fooball Teams Champion in Olympic Courses')

ax2.set_title('Women Fooball Teams Champion in Olympic Courses')
ax2.set_xlabel('years')
ax1.legend()
ax2.legend()  
ax1.grid()
ax2.grid()
plt.show() 