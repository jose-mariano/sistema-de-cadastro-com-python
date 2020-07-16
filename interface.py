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

		self.containerPassword = tk.Frame(self.containerMain, padx=20, pady=10, bg=self.backgroundColor)
		self.containerPassword.pack()
		self.messagePassword = tk.Label(self.containerPassword, text='Password', padx=10, pady=10, bg=self.backgroundColor)
		self.messagePassword.pack(anchor='w')
		self.getPassword = tk.Entry(self.containerPassword, width=30, bg=self.backgroundColor)
		self.getPassword.config(highlightbackground='black')
		self.getPassword.pack()

		self.containerConfirmPassword = tk.Frame(self.containerMain, padx=20, pady=10, bg=self.backgroundColor)
		self.containerConfirmPassword.pack()
		self.messageConfirmPassword = tk.Label(self.containerConfirmPassword, text='Confirm Password', padx=10, pady=10, bg=self.backgroundColor)
		self.messageConfirmPassword.pack(anchor='w')
		self.getConfirmPassword = tk.Entry(self.containerConfirmPassword, width=30, bg=self.backgroundColor)
		self.getConfirmPassword.config(highlightbackground='black')
		self.getConfirmPassword.pack()

		self.containerButton = tk.Frame(self.containerMain, padx=20, pady=20, bg=self.backgroundColor)
		self.containerButton.pack()
		self.buttonCreateAccount = tk.Button(self.containerButton, text='Create Account')
		self.buttonCreateAccount.pack()



window = tk.Tk()
window['pady'] = 40
window.title('Creating a new account')
window.geometry('400x400')
Application(window)
window.mainloop()