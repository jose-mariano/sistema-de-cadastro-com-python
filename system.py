import interface as frames
from manipulationData import database as db

database = db.Database('register.db')

pages = (frames.StartPage, frames.SeeRegisteredPeople, frames.RegistrationPage)

system = frames.FrameManipulation(pages=pages, database=database)
system.mainloop()
