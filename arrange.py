import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame(pd.read_csv("data.csv"))
data.sort_values(by = ["customer_id"], axis = 0, ascending = True, inplace = True)
new_data = pd.DataFrame(columns = ["customer_id","gender","most_recent_order_date","order_count"])
unique_numb = data["customer_id"].unique()
for val in unique_numb:
	temp_frame = data[data["customer_id"] == val]
	count = len(temp_frame.index)
	gend = temp_frame["gender"].iloc[0]
	date = temp_frame["date"].iloc[count-1]
	temp_data = pd.Series({"customer_id":val,"gender":gend,"most_recent_order_date":date,"order_count":count},name = "")
	new_data  = new_data.append(temp_data,ignore_index = False)
new_data.to_csv("new_data.csv",index = False)

#plot
gender_0 = []
gender_1 = []
count_order = []
rang = pd.date_range('2017-01-01','2018-01-01',freq = "W")
new_data["most_recent_order_date"] = pd.to_datetime(new_data["most_recent_order_date"])
rang_numb = len(rang)
x = []
for i in range(0,rang_numb):
        x.append(1+i)
        count_order.append(new_data[(new_data["most_recent_order_date"] < rang[i]) & (new_data["most_recent_order_date"] > rang[i-1]) ]["order_count"].sum())
	gender_0.append(new_data[(new_data["most_recent_order_date"] < rang[i]) & (new_data["most_recent_order_date"] > rang[i-1]) & (new_data["gender"] == 0)]["order_count"].sum())
	gender_1.append(new_data[(new_data["most_recent_order_date"] < rang[i]) & (new_data["most_recent_order_date"] > rang[i-1]) & (new_data["gender"] == 1)]["order_count"].sum())
	
mean_0 = np.mean(gender_0)
mean_1 = np.mean(gender_1)
print ("%s: %lf"%("mean order value for gender 0",mean_0))
print("%s: %lf"%("mean order value for gender 1",mean_1))
plt.plot(x,count_order,linewidth = 1.0)
plt.xlabel("week")
plt.ylabel("count of orders")
plt.show()
