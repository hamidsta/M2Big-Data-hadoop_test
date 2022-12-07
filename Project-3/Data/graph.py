import pandas as pd
import matplotlib.pyplot as plt

Description=pd.read_csv("D:/ROSALIND_problems/Mongo_db/Cause.csv",index_col=False,header=None)
Description=Description.dropna()
Description.rename(columns = {0:'Description' , 1:'Average_age'}, inplace = True)
Description = Description.loc[Description['Average_age'] <=22]
Description.sort_values('Average_age', ascending=True, inplace=True)
plt.plot(Description["Description"], Description["Average_age"])
plt.tick_params(axis='both', labelsize=18)
plt.rcParams["figure.figsize"] = (10,5.5)


locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()



#plt.savefig('age_description')

