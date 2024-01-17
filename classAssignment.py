class Patient:
    """Encapsulation Assignment"""
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__ssn = 0

    def setData(self,id,name,ssn):
        self.__id = id
        self.__name = name
        self.__ssn = ssn

    def getData(self):
        return {"id":self.__id,"name":self.__name, "ssn":self.__ssn}
    
p1 = Patient()
p1.setData(1001, 'Jone', 2122)
print("\n\n")
print(p1.__doc__ )
# patientData = " ".join(p1.getData())
patientData = p1.getData()
print("Patient 1")
for x in patientData.keys():
    print(x,":",patientData[x])

from abc import ABC, abstractmethod
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        print("12929")

class HP(TouchScreenLaptop):
    def scroll(self):
        pass
    
class DELL(TouchScreenLaptop):
    def scroll(self):
        pass

class HpNoteBook(HP):
    """Abstraction Assignment"""
    def click(self):
        super().click()
        print("click on HP")

class DellNoteBook(DELL):
    def click(self):
        print("click on Dell")
        pass

HPNoteBook1 = HpNoteBook()
DELLPNoteBook1 = DellNoteBook()
print("\n\n")
print(HPNoteBook1.__doc__ )
HPNoteBook1.click()
DELLPNoteBook1.click()