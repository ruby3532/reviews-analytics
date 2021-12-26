import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		bar.update(count)
print('檔案讀取完了，總共有' , len(data) , '筆資料')

print(data[0])

# 文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split(' ') # d 是 一筆留言，data 是清單
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的 key 進 wc 字典

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))


while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過喔')

print('感謝使用此查詢功能！')