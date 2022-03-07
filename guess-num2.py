# 讓使用者輸入隨機整數的範圍
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“終於猜對了！”
# 猜錯的話 要告訴他 比答案大/小
# 印出猜了幾次


import random
start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)

count = 0
r = random.randint(start, end)
while True:
	count += 1
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