class Cookie:
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
cookie_one = Cookie("green")
print(cookie_one.getColor())


duplicates = set()
duplicates.add(1)
duplicates