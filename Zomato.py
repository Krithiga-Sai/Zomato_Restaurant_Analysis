import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('./zomato_data.csv')
df.head()
df.info()
updated_rate=df['Rate'].str.split('/').str[0]
print(updated_rate)
df['Rate']=updated_rate.astype('float64')
print(df['Rate'])
df.columns=df.columns.str.title()
print(df.columns)
df=df.drop_duplicates()
print(df.isnull())

#votes received for each type of restaurant
rest_votes=df.groupby('Listed_In(Type)')['Votes'].sum()
print(pd.DataFrame(rest_votes))
"""
#restaurants that provide table booking
table_booking=df['Book_Table'].value_counts()
print(pd.DataFrame(table_booking))
table_booking.plot.pie(autopct='%1.1f%%')
plt.title("Restaurants that provide bookings")
plt.show()

#top rest
top=df.sort_values('Votes',ascending=False).head(5)
print(top[['Restaurant Name','Votes']])

#relationship between rating and votes
plt.scatter(df['Rate'],df['Votes'])
plt.title("Relationship between ratings and votes")
plt.xlabel("Restaurant Rating")
plt.ylabel("Customer Votes")
plt.show()

#avg rating for each rest
avg_rating=df.groupby("Listed_In(Type)")['Rate'].mean()
print(avg_rating)
plt.bar(avg_rating.index,avg_rating.values)
plt.title("Average ratings for each restaurant type")
plt.xlabel("Restaurant type")
plt.ylabel("Ratings")
plt.show()

#type of restaurant do the majority of customers order from
online_order=df['Listed_In(Type)'].value_counts()
print(pd.DataFrame(online_order))

#ratings restaurants most commonly receive
common_rate=df['Rate'].value_counts()
print(pd.DataFrame(common_rate).head(5))
plt.bar(common_rate.index,common_rate.values)
plt.show()



exp_rest=df['Approx_Cost(For Two People)'].max()
print(exp_rest)
"""
# restaurant types that have more records without online ordering
pivot_table=df.pivot_table( index="Listed_In(Type)", 
    columns="Online_Order", 
    aggfunc="size", 
    fill_value=0 )
print(pivot_table)
sns.heatmap(pivot_table,annot=True)
plt.title("Without online booking")
plt.show()