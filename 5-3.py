# ここにプログラムを記入してください
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ['Sunday', 'Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday']
default_year = 1981
default_date = 101 #0101

# 閏年の判定
def leap_year(year):
	flag = 0
	if year % 400 == 0:
		flag = 1
	elif year % 100 != 0 and year % 4 == 0:
		flag = 1
	elif year % 4 == 0:
		flag = 1
		
	return flag

# その年の1/1~当日までの合計日数
def calc_daycount(input_year, input_date):
	month = input_date  // 100
	date = input_date % 100
	total = 0
	
	if leap_year(input_year):
		dates[1] = 29
	else:
		dates[1] = 28

	for i in range(month - 1):
		total += dates[i]
	total += date

	return total

def calc_daycount_and_dayofweek(input_date):
	result = {'daycount':0, 'dayofweek':'None'}
	year = input_date // 10000
	date = input_date % 10000
	daycount = 0
	for y in range(default_year, year):
		if leap_year(y):
			dates[1] = 29
		else:
			dates[1] = 28

		daycount += sum(dates)

	total = calc_daycount(year, date)
	daycount += total

	result['daycount'] = daycount
	day_num = (result['daycount'] + 3) % 7
	result['dayofweek'] = d[day_num]

	return result


target_date = int(input())
today = int(input())
Target = calc_daycount_and_dayofweek(target_date)
Today = calc_daycount_and_dayofweek(today)


print('Target {}'.format(Target['dayofweek']))
print('Today {}'.format(Today['dayofweek']))
print('Delta is {} day(s)'.format(Today['daycount'] - Target['daycount']))


print("")