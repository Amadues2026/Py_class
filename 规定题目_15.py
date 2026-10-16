import csv
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['日期', '销量'])
    date = datetime.date(2022, 1, 1)
    for i in range(365):
        writer.writerow([date, 300 + i * 5 + random.randrange(100)])
        date += datetime.timedelta(days=1)

data = pd.read_csv('data.csv', parse_dates=['日期'])
print(data)
print(data.shape)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 5))
plt.plot(data['日期'], data['销量'])
plt.title('每天营业额')
plt.xlabel('日期')
plt.ylabel('营业额')
plt.tight_layout()
plt.savefig('first.jpg')
plt.close()

month = data.groupby(data['日期'].dt.month)['销量'].sum()
plt.figure(figsize=(10, 5))
plt.bar(month.index, month.values)
plt.xticks(range(1, 13))
plt.title('每月营业额')
plt.xlabel('月份')
plt.ylabel('营业额')
plt.tight_layout()
plt.savefig('second.jpg')
plt.close()

growth = month.pct_change()
with open('maxMonth.txt', 'w', encoding='utf-8') as f:
    f.write(str(growth.idxmax()) + '月')

quarter = data[data['日期'].dt.year == 2022].groupby(data['日期'].dt.quarter)['销量'].sum()
plt.figure(figsize=(7, 7))
plt.pie(quarter.values, labels=['第一季度', '第二季度', '第三季度', '第四季度'], autopct='%1.1f%%')
plt.title('2022年各季度营业额')
plt.tight_layout()
plt.savefig('third.jpg')
plt.close()
