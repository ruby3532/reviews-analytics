data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0: # % 是用來求餘數
			print(len(data))  # 了解讀取進度
print('檔案讀取完了，總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為' , sum_len/ len(data))

	# print('平均長度為' , float(sum_len[-1]) / 1000)
	# print(sum_len)


#print(data[0]) # 印第一筆
#print(-------------------)
#print(data[1])
