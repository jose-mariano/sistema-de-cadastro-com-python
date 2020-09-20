import tkinter as tk
from tkinter import ttk
import manipulationData as data

class FrameManipulation(tk.Tk):
	def __init__(self, pages, database, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.database = database

		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in pages:
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.showFrame(pages[0])

	def showFrame(self, context):
		frame = self.frames[context]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		controller.title('Pagina')

		container = tk.Frame(self)
		container.grid(row=0, column=0)
		
		title = tk.Label(container, text='Página inicial', font=('Arial', '20', 'bold'))
		title.grid(row=0, column=0, pady=20)
		description = tk.Label(container, bg='white', highlightbackground='black',
			highlightthickness=1)
		description['text'] = """Esse sistema foi desenvolvido com o intuito de cadastrar novas\n pessoas e ver as pessoas cadastradas"""
		description.grid(row=1, column=0, sticky='we', ipadx=89, ipady=25)
		
		buttonSeeRegisteredPeople = tk.Button(container, text='Ver pessoas cadastradas', width=20)
		buttonSeeRegisteredPeople['command'] = lambda : (controller.frames[SeeRegisteredPeople].updateTable(), controller.showFrame(SeeRegisteredPeople))
		buttonSeeRegisteredPeople.grid(row=2, column=0, pady=(60, 0))
		
		buttonRegistrationPage = tk.Button(container, text='Cadastrar nova pessoa', width=20, command=lambda : controller.showFrame(RegistrationPage))
		buttonRegistrationPage.grid(row=3, column=0)
		
		buttonExit = tk.Button(container, text='Sair', width=20, command=container.quit)
		buttonExit.grid(row=4, column=0, pady=(0,60))

		development = tk.Label(container, text='Desenvolvido por José Mariano da Silva', font=('Arial', '8'))
		development.grid(row=5, column=0)


class SeeRegisteredPeople(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.database = controller.database
		self.showPeople = 0

		buttonHomePage = tk.Button(self, text='voltar', font=('Arial', '7'))
		buttonHomePage['command'] = lambda : controller.showFrame(StartPage)
		buttonHomePage.grid(row=0, column=0, sticky='w')

		title = tk.Label(self, text='Pessoas cadastradas', font=('Arial', '15', 'bold'))
		title.grid(row=1, column=0, columnspan=2)

		columns = ('id', 'name', 'dateOfBirth', 'gender', 'maritalStatus')
		portugueseColumns = ('Id', 'Nome', 'Nascimento', 'Sexo', 'Estado Civil')
		self.table = ttk.Treeview(self, columns=columns, show='headings', height=16)
		self.table.grid(row=2, column=0, padx=(8, 0))
		scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.table.yview)
		scrollbar.grid(row=2, column=1, sticky='ns')
		self.table.config(yscrollcommand=scrollbar.set)
		self.table.column('id', minwidth=30, width=30)
		self.table.column('name', minwidth=200, width=240)
		self.table.column('dateOfBirth', minwidth=100, width=100)
		self.table.column('gender', minwidth=100, width=100)
		self.table.column('maritalStatus', minwidth=100, width=100)

		for index, item in enumerate(columns):
			self.table.heading(item, text=portugueseColumns[index])

	def updateTable(self):
		people = self.database.select("SELECT * FROM tbl_people WHERE id > {}".format(self.showPeople))
		for person in people:
			person = (person[0], person[1], data.modifyDate(person[2]), person[3], person[4])
			self.table.insert('', 'end', values=person)
			self.showPeople += 1


class RegistrationPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.database = controller.database
		self.textFont = ('Arial', '12')
		self.errorFont = ('Arial', '8')

		containerButtonHomePage = tk.Frame(self)
		containerButtonHomePage.grid(row=0, column=0, columnspan=2, stick='w')
		buttonHomePage = tk.Button(containerButtonHomePage, text='Voltar', font=('Arial', '7'))
		buttonHomePage['command'] = lambda : controller.showFrame(StartPage)
		buttonHomePage.grid(row=0, column=0)

		containerTitle = tk.Frame(self)
		containerTitle.grid(row=1, column=0, columnspan=2, pady=30, padx=140)
		title = tk.Label(containerTitle, text='Preencha as informações abaixo', font=('Arial', '15', 'bold'))
		title.grid(row=0, column=0, columnspan=2)

		containerInputName = tk.Frame(self)
		containerInputName.grid(row=2, column=0, columnspan=2, padx=50, pady=10)
		textName = tk.Label(containerInputName, text='Nome: ', font=self.textFont)
		textName.grid(row=0, column=0)
		self.inputName = tk.Entry(containerInputName, width=50)
		self.inputName.grid(row=0, column=1)
		errorName = tk.Label(containerInputName, font=self.errorFont, fg='red')
		errorName.grid(row=1, column=0, columnspan=2)

		containerDateBirth = tk.Frame(self)
		containerDateBirth.grid(row=3, column=0, stick='w', padx=(65,0), pady=10)
		textDateBirth = tk.Label(containerDateBirth, text='Data de nascimento: ', font=self.textFont)
		textDateBirth.grid(row=0, column=0)
		self.inputBirthday = tk.Entry(containerDateBirth, width=2)
		self.inputBirthday.grid(row=0, column=1)
		separator1 = tk.Label(containerDateBirth, text='/', font=('Arial', '13', 'bold'))
		separator1.grid(row=0, column=2)
		self.inputBirthMonth = tk.Entry(containerDateBirth, width=2)
		self.inputBirthMonth.grid(row=0, column=3)
		separator2 = tk.Label(containerDateBirth, text='/', font=('Arial', '13', 'bold'))
		separator2.grid(row=0, column=4)
		self.inputBirthYear = tk.Entry(containerDateBirth, width=4)
		self.inputBirthYear.grid(row=0, column=5)
		errorDateOfBirth = tk.Label(containerDateBirth, font=self.errorFont, fg='red')
		errorDateOfBirth.grid(row=1, column=0, columnspan=6)

		containerGender = tk.Frame(self)
		containerGender.grid(row=3, column=1, stick='e', padx=(0,65), pady=10)
		textGender = tk.Label(containerGender, text='Sexo: ', font=self.textFont)
		textGender.grid(row=0, column=0)
		optionsGender = ('', 'Feminino', 'Masculino')
		self.selectGender = ttk.Combobox(containerGender, values=optionsGender, state='readonly', width=10)
		self.selectGender.grid(row=0, column=1)
		errorGender = tk.Label(containerGender, font=self.errorFont, fg='red')
		errorGender.grid(row=1, column=0, columnspan=2)

		containerMaritalStatus = tk.Frame(self)
		containerMaritalStatus.grid(row=4, column=0, columnspan=2, stick='w', padx=65, pady=10)
		textMaritalStatus = tk.Label(containerMaritalStatus, text='Estado civil: ', font=self.textFont)
		textMaritalStatus.grid(row=0, column=0)
		optionsMaritalStatus = ('', 'Solteiro', 'Namorando', 'Casado', 'Divorciado')
		self.selectMaritalStatus = ttk.Combobox(containerMaritalStatus, values=optionsMaritalStatus, state='readonly')
		self.selectMaritalStatus.grid(row=0, column=1)
		errorMaritalStatus = tk.Label(containerMaritalStatus, font=self.errorFont, fg='red')
		errorMaritalStatus.grid(row=1, column=0, columnspan=2)

		containerButton = tk.Frame(self)
		containerButton.grid(row=5, column=0, columnspan=2, pady=(20,50))
		buttonRegister = tk.Button(containerButton, text='Cadastrar', command=self.registerPerson)
		buttonRegister.grid(row=0, column=0)

		self.labelErrors = (errorName, errorDateOfBirth, errorGender, errorMaritalStatus)

	def registerPerson(self):
		self.showError()

		personData = data.treatData(self.getAttributes())
		dataError = data.errors(personData)

		if dataError == None:
			self.database.insertInto(personData[0], personData[1], personData[2], personData[3])
			self.cleanInputItems()
		else:
			self.showError(dataError)

	def getAttributes(self):
		name = str(self.inputName.get())
		birthday = str(self.inputBirthday.get())
		birthMonth = str(self.inputBirthMonth.get())
		birthYear = str(self.inputBirthYear.get())
		gender = str(self.selectGender.get())
		maritalStatus = str(self.selectMaritalStatus.get())

		return {
			'name': name,
			'birthYear': birthYear,
			'birthMonth': birthMonth,
			'birthday': birthday,
			'gender': gender,
			'maritalStatus': maritalStatus
		}

	def showError(self, error=None):
		dictLabelErrors = {
			'name': (self.labelErrors[0], '*Nome inválido*'),
			'dateOfBirth': (self.labelErrors[1], '*Data inválida*'),
			'gender': (self.labelErrors[2], '*Selecione seu sexo*'),
			'maritalStatus': (self.labelErrors[3], '*Selecione seu estado civil*')
		}
		if error in dictLabelErrors:
			dictLabelErrors[error][0]['text'] = dictLabelErrors[error][1]
		else:
			for item in dictLabelErrors.values():
				item[0]['text'] = ''

	def cleanInputItems(self):
		dictItems = {
			'Entry': (self.inputName, self.inputBirthday, self.inputBirthMonth, self.inputBirthYear),
			'Combobox': (self.selectGender, self.selectMaritalStatus)
		}
		for typeItem in dictItems.keys():
			for item in dictItems[typeItem]:
				if typeItem == 'Entry':
					item.delete(0, tk.END)
				else:
					item.current(0)

