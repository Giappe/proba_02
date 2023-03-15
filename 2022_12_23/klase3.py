from abc import *

class Kartica(ABC):
    def __init__(self, broj, stanje):
        self.broj = broj
        self.stanje = stanje
    @abstractmethod
    def plati(self, suma):
        pass

# k = Kartica() OVO NE MOZE

class Visa(Kartica):
    def plati(self, suma):
        self.stanje -= suma *1.05

visa = Visa("111", 500)
print(visa())