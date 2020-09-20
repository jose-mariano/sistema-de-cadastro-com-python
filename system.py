import interface as frames
from manipulationData import database as db

database = db.Database('register.db')

pages = (frames.StartPage, frames.SeeRegisteredPeople, frames.RegistrationPage)

system = frames.FrameManipulation(pages=pages, database=database)
system.title('Sistema de Cadastro')
system.geometry('600x400+100+50')
system.resizable(False, False)
system.mainloop()
