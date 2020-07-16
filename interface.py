import tkinter as tk

class Application:
	def __init__(self, master=None):
		self.containerMain = tk.Frame(master)
		self.containerMain.pack()

		self.containerUsername = tk.Frame(self.containerMain, padx=20, pady=10)
		self.containerUsername.pack()
		self.messageUsername = tk.Label(self.containerUsername, text='Username', padx=10, pady=10)
		self.messageUsername.pack(anchor='w')
		self.getUsername = tk.Entry(self.containerUsername, width=30)
		self.getUsername.pack()

		self.containerPassword = tk.Frame(self.containerMain, padx=20, pady=10)
		self.containerPassword.pack()
		self.messagePassword = tk.Label(self.containerPassword, text='Password', padx=10, pady=10)
		self.messagePassword.pack(anchor='w')
		self.getPassword = tk.Entry(self.containerPassword, width=30)
		self.getPassword.pack()

		self.containerConfirmPassword = tk.Frame(self.containerMain, padx=20, pady=10)
		self.containerConfirmPassword.pack()
		self.messageConfirmPassword = tk.Label(self.containerConfirmPassword, text='Confirm Password', padx=10, pady=10)
		self.messageConfirmPassword.pack(anchor='w')
		self.getConfirmPassword = tk.Entry(self.containerConfirmPassword, width=30)
		self.getConfirmPassword.pack()

		self.containerButton = tk.Frame(self.containerMain, padx=20, pady=20)
		self.containerButton.pack()
		self.buttonCreateAccount = tk.Button(self.containerButton, text='Create Account')
		self.buttonCreateAccount.pack()



window = tk.Tk()
window['pady'] = 40
window['bg'] = 'white'
window.title('Creating a new account')
window.geometry('400x400')
Application(window)
window.mainloop()