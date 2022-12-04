from random import *
class University:
	def __init__(self, title, faculty):
		self.title = title
		self.faculty = faculty
		self.budjet = False
	def studying(self, name):
		print(name, 'is studying')
	def isbudget(self):
		if self.budjet == True:
			print('Congrats! You are on budget')
		else:
			print('Pay money and study!')

class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.money = 500
    self.alive = True
  def ask_budget(self):
    if self.progress >= 20:
      print('You are good enough!')
      univer.budjet = True
    else:
      print('You are not good enough!')
  def payforstudying(self):
    if univer.budjet == False:
      print('Pay to study!')
      self.money -= 250
    if self.money < 250:
      print('You have not enough money to study!')
      self.alive = False
    if self.progress >= 20:
      print('You are on budjet!')
  def work(self):
    print('You are working well!')
    self.gladness -= 10
    self.progress -= 5
    self.money += 500
  def session(self):
    print('You are studying some etra lessons')
    self.money -= 250
    self.progress += 20
    self.gladness -= 15
  def say_hello(self):
    print('Hello!')
  def to_study(self):
    print('Time to study')
    self.progress += 10
    self.gladness -= 10
  def to_sleep(self):
    print('Sleep time')
    self.gladness += 5
  def to_chill(self):
    print('Chill time')
    self.gladness += 15
    self.progress -= 5
  def is_alive(self):
    if self.progress < -40:
      print('You are bad student')
      self.alive = False
    elif self.gladness < 15:
      print('Depression...')
      self.alive = False
    elif self.progress > 100:
      print('Amazing!')
      self.alive = False
  def statistics(self):
    print('Gladness = ', self.gladness, ' Progress = ', self.progress)
    print('Budget = ', univer.budjet,' Money = ',self.money)
  def live(self, day):
    day = 'Day ' + str(day) + ' of ' + self.name + ' life'
    print(day) 
    if self.money <=500:
      live_cube = randint(1,5)
      if live_cube == 1:
        self.ask_budget()
        self.to_study()
        univer.studying(self.name)
      elif live_cube == 2:
        self.to_sleep()
      elif live_cube == 3:
        self.to_chill()
      elif live_cube == 4:
        self.say_hello()
      elif live_cube == 5:
        self.work()
    else:
      live_cube2 = randint(1,6)
      if live_cube2 == 1:
        self.to_study()
        univer.studying(self.name)
      elif live_cube2 == 2:
        self.to_sleep()
      elif live_cube2 == 3:
        self.to_chill()
      elif live_cube2 == 4:
        self.say_hello()
      elif live_cube2 == 5:
        self.work()
      elif live_cube2 == 6:
        self.session()
    if univer.budjet == False:
      self.ask_budget()
    self.payforstudying()
    self.statistics()
    self.is_alive()

univer = University('Step', 'Computer Science')
human = Student('Anton')
for day in range(10):
	if human.alive == False:
		break
	human.live(day)