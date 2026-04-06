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
        return random.choice(list(self.__operations.items()))
    
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
        return [self.__name,self.__true_primers,self.__false_primers,self.__money]

    def change_name(self,name_input):
        if name_input != "":
            self.__name = name_input
            return 200
        else:
            return 400
    def up_true_primers(self):
        self.__true_primers += 1

    def up_false_primers(self):
        self.__false_primers += 1



class Game:
    def __init__(self):
        self.math_c = math_operations()
        self.player_game = Player()
        self.__content = None

    def verify_name(self):
        with open('info.txt',"r",encoding="utf-8") as file:
            self.__content = file.read()
        self.__content = self.__content.split(",")
        name = self.__content[0]
        if name != "Unknown":
            return 200
        elif name == "Unknown":
            return 400   
    def start(self):
        status_name = self.verify_name()
        if status_name == 200:
             data_player = self.player_game.get_info()
             print(f"Привет {data_player[0]}")
             while True:
                print("выбери операцию что б начать 1 - решать примеры , 2 - узнать информацию по аккаунту , 3 - выйти")       
                user_choise = input()
                if user_choise == "1":
                    while True:
                        primers = self.math_c.get_operations()
                        primer = self.math_c.get_random_primer()[0]
                        print(f"Пример - {primer} (Выйти с игры - /stop)")
                        otvet = input()
                        if otvet == "/stop":
                            break
                        try:
                            otvet = int(otvet)
                            if otvet == primers[primer]:
                                up_money = random.randint(40,100)
                                data_player[1] += 1
                                data_player[3] += up_money 
                                print(f"Ответ верный - баланс: {data_player[3]}(+{up_money})")
                            else:
                                del_money = random.randint(40,100)
                                data_player[2] += 1
                                data_player[3] -= del_money
                                print(f"Ответ не верный - баланс: {data_player[3]}(-{del_money})")
                        except:
                              del_money = random.randint(40,100)
                              data_player[2] += 1
                              data_player[3] -= del_money
                              print(f"Ответ не верный - баланс: {data_player[3]}(-{del_money})")
                elif user_choise == "2":
                    print(f"Никнейм - {data_player[0]}, Правильно решенные примеры - {data_player[1]}, Неправильно решенные примеры - {data_player[2]}, Баланс - {data_player[3]}")
                elif user_choise == "3":
                    print(f"Возвращайтесь {data_player[0]}!!")
                    break
if __name__ == "__main__":
    start_game = Game()         
    start_game.start()
            