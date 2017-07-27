#!/usr/bin/python

from collections import Counter

NUM_BALLS = 5
NUM_POWERBALLS = 1
BALL_MIN = 1
BALL_MAX = 69
POWERBALL_MAX = 26
BALL_RANGE = range(BALL_MIN, BALL_MAX+1)
POWERBALL_RANGE = range(BALL_MIN, POWERBALL_MAX+1)

NOT_A_NUMBER_ERROR = '*** Input entered is not a number'
NOTHING_ENTERED_ERROR = '*** Nothing entered for input'
NOT_IN_BALL_RANGE = '*** Input entered is not between ' + str(BALL_MIN) + ' and ' + str(BALL_MAX) + ' or already entered'
NOT_IN_POWERBALL_RANGE = '*** Input entered is not between ' + str(BALL_MIN) + ' and ' + str(POWERBALL_MAX)


class Employee:
	def __init__(self):
		self.first_name = ''
		self.last_name = ''
		self.balls = []
		self.balls_left = BALL_RANGE
		self.powerball = None

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_name(self):
		return self.get_first_name() + ' ' + self.get_last_name()

	def set_first_name(self, first_name):
		self.first_name = first_name

	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_balls(self):
		return self.balls

	def get_balls_left(self):
		return self.balls_left

	def get_number_of_balls(self):
		return len(self.get_balls())

	def verify_ball(self, ball):
		ball_num = int(ball)
		if ball_num in self.get_balls_left():
			return True
		else:
			return False

	def add_ball(self, ball):
		if self.get_number_of_balls() is 0:
			self.balls_left = range(BALL_MIN, BALL_MAX)
		ball_num = int(ball)
		self.balls_left[ball_num-1] = None
		self.balls.append(ball)

	def reset_balls_left(self):
		self.balls_left = BALL_RANGE

	def get_powerball(self):
		return self.powerball

	def set_powerball(self, powerball):
		self.powerball = powerball

	def __str__(self):
		balls_str = " ".join(str(ball) for ball in self.balls)
		return self.get_name() + " | " + balls_str + " | Powerball: " + str(self.get_powerball())



def main():
	num_employees = None
	while type(num_employees) is not int:
		try:
			num_employees = input('Enter number of employees: ')
			if not num_employees:
				raise Exception(NOTHING_ENTERED_ERROR)
		except NameError:
			print NOT_A_NUMBER_ERROR, '\n'
			continue
		except Exception as e:
			print NOTHING_ENTERED_ERROR, '\n'
			continue

	employees = range(0, int(num_employees))
	for num in employees:
		first_name = ''
		last_name = ''
		while len(first_name) is 0:
			try:
				first_name = raw_input('Enter your first name: ')
				if not first_name:
					raise Exception(NOTHING_ENTERED_ERROR)
			except Exception as e:
				print e, '\n'
				continue

		while len(last_name) is 0:
			try:
				last_name = raw_input('Enter your last name: ')
				if not last_name:
					raise Exception(NOTHING_ENTERED_ERROR)
			except Exception as e:
				print e, '\n'
				continue

		employee = Employee()
		employee.reset_balls_left()
		employees[num] = employee
		current_employee = employees[num]
		current_employee.set_first_name(first_name)
		current_employee.set_last_name(last_name)
		while current_employee.get_number_of_balls() is not NUM_BALLS:
			ball_input = None
			try:
				ball_input = input('Enter Ball #' + str(employee.get_number_of_balls()+1) + ': ')
				if current_employee.verify_ball(ball_input):
					current_employee.add_ball(ball_input)
				else:
					raise Exception(NOT_IN_BALL_RANGE)
			except NameError:
				print NOT_A_NUMBER_ERROR, '\n'
			except Exception as e:
				print e, '\n'

		while current_employee.get_powerball() not in POWERBALL_RANGE:
			try:
				powerball_input = input('Enter Powerball: ')
				if not powerball_input:
					raise Exception(NOTHING_ENTERED_ERROR)
				if powerball_input not in POWERBALL_RANGE:
					raise Exception(NOT_IN_POWERBALL_RANGE)
				current_employee.set_powerball(powerball_input)
			except Exception as e:
				print e, '\n'
				continue

	for employee in employees:
		print employee
		ball_output = Counter(employee.get_balls()).most_common(employee.get_number_of_balls())
		powerball_output = Counter([employee.get_powerball()]).most_common(1)[0]
		print "Powerball winning numbers: \n"
		for o in ball_output:
			ball, count = o
			print ball,
		print " Powerball: ",
		powerball, count = powerball_output
		print powerball



if __name__ == '__main__':
    main()
