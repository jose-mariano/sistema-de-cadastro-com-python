import tkinter as tk

class Application:
	def __init__(self, master=None):
		self.backgroundColor = 'white'

		self.containerMain = tk.Frame(master, bg=self.backgroundColor)
		self.containerMain.pack()

		self.containerUsername = tk.Frame(self.containerMain, padx=20, pady=10, bg=self.backgroundColor)
		self.containerUsername.pack()
		self.messageUsername = tk.Label(self.containerUsername, text='Username', padx=10, pady=10, bg=self.backgroundColor)
		self.messageUsername.pack(anchor='w')
		self.getUsername = tk.Entry(self.containerUsername, width=30, bg=self.backgroundColor)
		self.getUsername.config(highlightbackground='black')
		self.getUsername.pack()
		self.errorUsername = tk.Label(self.containerUsername, bg=self.backgroundColor)

		self.containerPassword = tk.Frame(self.containerMain, padx=20, pady=10, bg=self.backgroundColor)
		self.containerPassword.pack()
		self.messagePassword = tk.Label(self.containerPassword, text='Password', padx=10, pady=10, bg=self.backgroundColor)
		self.messagePassword.pack(anchor='w')
		self.getPassword = tk.Entry(self.containerPassword, width=30, bg=self.backgroundColor)
		self.getPassword['show'] = '*'
		self.getPassword.config(highlightbackground='black')
		self.getPassword.pack()
		self.errorPassword = tk.Label(self.containerPassword, bg=self.backgroundColor)

		self.containerConfirmPassword = tk.Frame(self.containerMain, padx=20, pady=10, bg=self.backgroundColor)
		self.containerConfirmPassword.pack()
		self.messageConfirmPassword = tk.Label(self.containerConfirmPassword, text='Confirm Password', padx=10, pady=10, bg=self.backgroundColor)
		self.messageConfirmPassword.pack(anchor='w')
		self.getConfirmPassword = tk.Entry(self.containerConfirmPassword, width=30, bg=self.backgroundColor)
		self.getConfirmPassword['show'] = '*'
		self.getConfirmPassword.config(highlightbackground='black')
		self.getConfirmPassword.pack()
		self.errorConfirmPassword = tk.Label(self.containerConfirmPassword, bg=self.backgroundColor)

		self.containerButton = tk.Frame(self.containerMain, padx=20, pady=20, bg=self.backgroundColor)
		self.containerButton.pack()
		self.buttonCreateAccount = tk.Button(self.containerButton, text='Create Account')
		self.buttonCreateAccount['command'] = self.checkData
		self.buttonCreateAccount.pack()
	

	def checkData(self):
		erros = False
		self.clearErrorMessages()
		self.getEntryValues()
		checkPasswords = self.passwordEqualsConfirmPassword()
		if checkPasswords == False:
			erros = True
			self.showError(self.errorConfirmPassword, '*the passwords are different*')
		if not self.username[0].isalpha():
			erros = True
			self.showError(self.errorUsername, '*the username must begin with a letter*')
		if not erros:
			print('Creating new account...')
			self.containerMain.quit()


	def getEntryValues(self):
		self.username = str(self.getUsername.get())
		self.password = str(self.getPassword.get())
		self.confirmPassword = str(self.getConfirmPassword.get())


	def passwordEqualsConfirmPassword(self):
		if self.password == self.confirmPassword:
			return True
		else:
			return False


	def showError(self, where, message):
		where['fg'] = 'red'
		where['font'] = ('arial', '8')
		where['text'] = message
		where.pack()


	def clearErrorMessages(self):
		errorLabels = (self.errorUsername, self.errorPassword, self.errorConfirmPassword)
		for label in errorLabels:
			label['text'] = ''
			label.forget()






window = tk.Tk()
window['pady'] = 40
window.title('Create a new account')
Application(window)
window.mainloop()