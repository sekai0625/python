# ここにプログラムを記入してください
class Student:
	# ここに Student クラスのメソッドを定義してください
	def __init__(self, idnum, name):
		self.idnum = idnum
		self.name = name
		self.scores_avg = 0
		self.scores = list()
		self.gpa = 0

	def add_score(self, score):
		if len(score) != 0:
			self.scores = list(map(int, score))
		else:
			self.scores.append(0)
		
	def scores_avg(self):
		return sum(self.scores) / len(self.scores)

	def GPA(self):
		gp = 0
		for x in self.scores:
			if x >= 90 and x <= 100:
				gp += 4
			elif x >= 80 and x < 90:
				gp += 3
			elif x >= 70 and x < 80:
				gp += 2
			elif x >= 60 and x < 70:
				gp += 1
			elif x >= 0 and x < 60:
				gp += 0
		
		self.gpa = gp / len(self.scores)

		return self.gpa

	def __str__(self):
		return "{}({}):{}".format(self.name, self.idnum, self.gpa)

	def idnumber(self):
		return self.idnum
	
	def __lt__(self, other):
		return self.idnum < other.idnum

# ここに Student クラスを利用するプログラムを書き写してください
n = int(input())
i = 0
object_list = []
while i < n:
	s = input()
	s_list = s.split(",")
	object_list.append(Student(s_list[0], s_list[1]))
	object_list[i].add_score(s_list[2:])
	i += 1

object_list.sort()
#object_list.sort(key = Student.GPA)
for x in object_list:
	print(x)

# 	print(x)