import random
class math_operations:
    def __init__(self):
        self.__operations = {
            "15 + 27": 42,
            "89 - 34": 55,
            "12 * 6": 72,
            "81 // 9": 9,
            "45 + 33": 78,
            "67 - 19": 48,
            "8 * 7": 56,
            "100 // 10": 10,
            "23 + 58": 81,
            "94 - 45": 49,
            "13 * 4": 52,
            "64 // 8": 8,
            "77 + 12": 89,
            "56 - 23": 33,
            "9 * 9": 81,
            "50 // 5": 10,
            "38 + 47": 85,
            "72 - 36": 36,
            "15 * 3": 45,
            "90 // 9": 10,
            "99 - 45": 54,
            "18 * 5": 90,
            "120 // 12": 10,
            "63 + 28": 91,
            "77 - 55": 22,
            "20 * 4": 80,
            "144 // 12": 12,
            "81 + 19": 100,
            "100 - 67": 33,
            "25 * 4": 100
            }
        
    def get_random_primer(self):
        self.primer = random.choice(self.__operations)
        return self.primer
    
    def get_operations(self):
        return self.__operations
    
class Player:
    def __init__(self):
        with open("info.txt","r",encoding="utf-8") as file:
            content = file.read()
            content = content.split(",")
        content[1],content[2],content[3]=int(content[1]),int(content[2]),int(content[3])
        self.__name = content[0]
        self.__true_primers = content[1]
        self.__false_primers = content[2]
        self.__money = content[3]
    
    def get_info(self):
        return list(self.__true_primers,self.__false_primers,self.__money,self.__name)

    def change_name(self,name_input):
        self.__name = name_input
    
class Game:
    def __init__(self):
        print("Привет как тебя зовут?")
        