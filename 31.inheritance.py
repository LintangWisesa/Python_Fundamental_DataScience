class Koki:
    def masakAppetizer(self):
        print('Koki pakar appetizer')
    def masakMainCourse(self):
        print('Koki pakar main course')
    def masakDessert(self):
        print('Koki pakar dessert')
    def masakSpesial(self):
        print('Koki pakar nasi tumpeng')

class Koki_Chinese(Koki):
    def masakSpesial(self):
        print('Koki pakar bebek Peking panggang')
    def masakKwetiau(self):
        print('Koki bisa masak kwetiau')

koki1 = Koki()
koki1.masakAppetizer()
koki1.masakSpesial()

koki2 = Koki_Chinese()
koki2.masakAppetizer()
koki2.masakSpesial()