# Validate data
def modifyDate(date):
	oldDate = date[:].split('-')
	return '{}/{}/{}'.format(oldDate[2], oldDate[1], oldDate[0])


def removeSpaces(string):
	return string.replace(' ', '')


def leapYear(year):
	year = int(year)
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 100 == 0 and year % 400 == 0:
		return True
	else:
		return False


def validateDateOfBirth(dateOfBirth):
	from datetime import date

	# date -> year/month/day
	dateOfBirth = dateOfBirth.split('-')
	if len(dateOfBirth) != 3:
		return False
	else:
		if len(removeSpaces(dateOfBirth[0])) == 0 or len(removeSpaces(dateOfBirth[1])) == 0 or len(removeSpaces(dateOfBirth[2])) == 0:
			return False 

	dateOfBirth = [int(item) for item in dateOfBirth]

	currentYear = date.today().year
	if dateOfBirth[0] > currentYear:
		return False
	elif dateOfBirth[1] < 1 or dateOfBirth[1] > 12:
		return False
	else:
		totalDaysOfTheMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if leapYear(dateOfBirth[0]):
			totalDaysOfTheMonth[1] = 29

		if dateOfBirth[2] < 1 or dateOfBirth[2] > totalDaysOfTheMonth[dateOfBirth[1] - 1]:
			return False

	return True


def validateName(name):
	nameWithoutSpaces = name[:].replace(' ', '')
	if name.strip() != '' and nameWithoutSpaces.isalpha() and len(nameWithoutSpaces) >= 3:
		return True
	else:
		return False


# Erros
def errors(data):
	if not validateName(data[0]):
		return 'name'
	elif not validateDateOfBirth(data[1]):
		return 'dateOfBirth'
	elif data[2] == '':
		return 'gender'
	elif data[3] == '':
		return 'maritalStatus'
	else:
		return None


# Treatment of data
def treatData(data):
	birthYear = removeSpaces(data['birthYear'])
	birthMonth = removeSpaces(data['birthMonth'])
	birthday = removeSpaces(data['birthday'])
	dateOfBirth = '{}-{}-{}'.format(birthYear, birthMonth, birthday)

	return (data['name'].strip(), dateOfBirth, data['gender'], data['maritalStatus'])
