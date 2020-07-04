import shelve
db=shelve.open('class-shelve')
sue =db['sue']
sue.giveRaise(-.25)
db['sue']=sue
print(db['sue'].pay)

tom = db['tom']
tom.giveRaise(-.20)
db['tom']=tom
print(db['tom'].pay)
db.close()