import model
import view
import zoo

def start():
    try:
        num = view.menu()
        if num == "1":
            addAnimal()
        elif num == "2":
            deleteAnimal()
        elif num == "3":
            infoAnimal()
        elif num == "4":
            sayAnimal()    
        elif num == "5":
            model.showAll()
            start()
        elif num == "6":
            model.sayAll()
            start()
        elif num == "7":
            return
        else:
            print("\n!! Введён некоректный пункт меню !! \n* Попробуйте снова *")
            start()
    except:
        print("\n!! Животное не найдено !!")
        start()

def addAnimal():
    num = view.addAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        start()
    else:
        model.addAnimal(num)
        start()

def deleteAnimal():
    model.showAll()
    num = view.deleteAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        start()
    else:
        model.deleteAnimal(num)
        start()

def sayAnimal():
    model.showAll()
    num = view.sayAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        start()
    else:
        model.sayAnimal(num)
        start()

def infoAnimal():
    model.showAll()
    num = view.showAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        start()
    else:
        model.showInfo(num)
        start() 