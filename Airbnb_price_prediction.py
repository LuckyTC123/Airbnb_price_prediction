#step1
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

#step2 read the file
df=pd.read_csv("Airbnb.csv")
#step3
##print(df.head())
##print(df.columns)
#defining the problem
##print(df['city'].value_counts())
#implementing the one hot encoding to convert textual to numeric
df=pd.get_dummies(df)
print(df.columns)

#creating two bins 
y=df['price']
x=df[['id', 'bedrooms', 'bathrooms', 'accommodates', 'min_nights', 'reviews',
        'city_Bangalore', 'city_Delhi', 'city_Goa', 'city_Mumbai','room_type_Entire home', 'room_type_Private room','room_type_Shared room']]

x_train,x_test,y_train,y_test=train_test_split(x,y)

model=RandomForestRegressor()

##model=joblib.load("airbnb.pkl")
model.fit(x_train,y_train)
#joblib.dump(model,"airbnb.pkl")

pred=model.predict(x_test)

print(mean_absolute_percentage_error(y_test,pred))







