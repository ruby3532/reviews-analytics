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

new = []
# for loop 的意思是把清單中的東西一個一個拿出來。每個拿出來的留言就稱作 d。
for d in data:
	if len(d) < 100:
		new.append(d) # 裝進新的清單
print('一共有' , len(new) , '筆留言長度小於100') # 因為他不需要一直印，所以不會在 for loop 中
print(new[0])


	# print('平均長度為' , float(sum_len[-1]) / 1000)
	# print(sum_len)


#print(data[0]) # 印第一筆
#print(-------------------)
#print(data[1])
