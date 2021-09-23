''' THis is all what i've learned till the momment about python '''

###########################CH1 Gettin started##################################
print('Mhammed Merabet')

##########################CH2 Variables########################################
something = "This is a variable"

string = "Text"
number = 568
float = 3.1445673
boolen = True, False
print(type(string))

##############################CH3 Intro to lists###############################
list = ['hey','idk','python always start counting with 0']
lenghtOfList = len(list)
list[1] = 7
toAddAtTheEnd = list.append('The thing you wanna add')
toAddAtSertnPosition = list.insert(3,"what you like")
del list[0]
poppedFromList = list.pop()
#list.remove('The thing you wanna add')
#list.sort() #To sort just for once
#list.sorted() #To make it sorted forever

##################CH4 Working with lists#######################################
"""
for thing in list:
    print(thing)
numbersList = list(range(1,6))
for num in range(1,5):
    print(num)
print(list[-3:])
"""
##################CH5 If statements############################################
names = ['Moha']
x = 3
if x == 3:
    print("It is")
else:
    print("it's not")
if "Omar" not in names:
    print('Down')
else:
    print("Up")

#########################CH6 Dictionaries######################################
dicts = {
    'name' : 'Mhammed',
    'familly' : 'Merabet',
}
dicts['newKey'] = 'newValue'
for key,value in dicts.items():
    print(key)
for key in dicts.keys():
    print(key)
for shiit in dicts.values():
    print(shiit)

#############################CH7 User input and while loops##################
userInput = input("type something here: ")
userNum = input("Type a number here: ")
userNum = int(userNum)
while True:
    if userInput != "Fuck You":
        i =+ 1
        msg = userInput
    else:
        print(msg)
    if userNum == 5:
        break

#######################CH8 Functins##########################################
def great(user):
    print("Hey "+user.title())
def sum(num01,num02):
    summes = num01 + num02
    return summes

############################CH9 Classes#####################################
class car():
    def __init__(self,make,year,model):
        self.make = make
        self.model = model
        self.year = year
    def presentation(self):
        print("This is a "+ self.model+ " made by "+self.make+" in "+str(self.year))
myCar = car('audi',2015,'rs6')
myCar.presentation()
class ElictricCar(car):
    def __init__(self, make, year, model):
        super().__init__(make, year, model)
        self.battery = 70
    def showBattery(self):
        print("This car has "+str(self.battery)+'-Kw battery.')
myElictric = ElictricCar("Tesla",2020,"Model X")
myElictric.presentation()
myElictric.showBattery()
from collections import OrderedDict #And you can do it from local files for classes
###############################CH10 Files and Exceptions####################


#CH11

