# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“終於猜對了！”
# 猜錯的話 要告訴他 比答案大/小
# 印出猜了幾次

import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請輸入數字：')
	num = int(num)
	if num == r:
		print('終於猜對了！', '共猜了', count, '次')
		break
	elif num > r:
		print('答案比', num, '小')
	elif num < r:
		print('答案比', num, '大')
	print('共猜了', count, '次')
