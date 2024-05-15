
import pandas as pd

# df = pd.read_excel("data-test.xlsx")

df = pd.read_csv("_user__202405151843.csv")

# # 计算一列数字的总和
total_sum = df['age'].sum()
total_count = df['age'].count()

print("The sum of the column is:", total_sum, total_count)

# print("\n(1)全部数据：") # user数据量太大，这里中间数据显示不出来
# print(df.iloc[:,:].values)

print("\n(2)第2行第3列的值：")
print(df.iloc[1,2])

# # # print("\n(3)第3行数据：")
# # # print(df.iloc[2].values)

# # # print("\n(4)第2列数据：")
# # # print(df.iloc[:,1].values)

# # # print("\n(5)第6行的姓名：")
# # # print(df.loc[5,"姓名"])

# # print("\n(6)第2至3行、第3至4列数据：")
# # print(df.iloc[1:3,2:4].values)



# ts.get_hist_data('600848')
# ts.get_today_all()
# df = ts.get_tick_data('600848',date='2014-01-09')
# df.head(10)

