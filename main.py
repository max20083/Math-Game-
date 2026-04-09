import random
class math_operations:
    def __init__(self):
       self.__operations = {}
       for _ in range(1000):
            # Выбираем случайную операцию
            op_type = random.choice(['+', '-', '*', '//'])
        
            if op_type == '+':
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                primer = f"{a} + {b}"
                answer = a + b
            
            elif op_type == '-':
                a = random.randint(1, 100)
                b = random.randint(1, a)  # чтобы результат не был отрицательным
                primer = f"{a} - {b}"
                answer = a - b
            
            elif op_type == '*':
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                primer = f"{a} * {b}"
                answer = a * b
            
            elif op_type == '//':
                b = random.randint(2, 20)
                answer = random.randint(1, 20)
                a = b * answer
                if a > 200:  # ограничиваем максимальное число
                    a = b * random.randint(1, 10)
                    answer = a // b
                primer = f"{a} // {b}"
        
            self.__operations[primer] = answer

        
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
        self.__rank = self.get_rank(content[1])
    
    def get_info(self):
        return [self.__name,self.__true_primers,self.__false_primers,self.__money,self.__rank]

    def change_name(self,name_input):
        if name_input != "" and name_input != "Unknown" and name_input != self.__name and "," not in name_input and "/" not in name_input:
            self.__name = name_input
            return 200
        elif self.__name == name_input:
            return 401
        elif name_input == "/stop":
            return 402
        else:
            return 400
    def up_true_primers(self):
        self.__true_primers += 1

    def up_false_primers(self):
        self.__false_primers += 1

    def get_rank(self,true_primers):
        if 0 <= true_primers  <= 50:
            return "Новичек"
        elif  51 <= true_primers <= 100:
            return "Крут"
        elif 101 <= true_primers <= 150 :
            return "Невероятно крут"
        elif 151 <= true_primers <= 250:
            return "Босс матана"
        elif  true_primers >= 251:
            return "легенда"
    
    def download_new_info(self,new_name,new_true,new_false,new_money,new_rank):
        self.__name = new_name
        self.__true_primers = new_true
        self.__false_primers = new_false
        self.__money = new_money
        self.__rank = new_rank


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
        elif name == "Unknown" or "/" in name or "," in name:
            return 400   
    def start(self):
        status_name = self.verify_name()
        data_player = self.player_game.get_info()
        if status_name == 200:
             print(f"Привет {data_player[0]}")
             while True:
                print("выбери операцию что б начать 1 - решать примеры , 2 - узнать информацию по аккаунту , 3 - Изменить никнейм, 4 - выйти")       
                user_choise = input().strip()
                if user_choise == "1":
                    while True:
                        primers = self.math_c.get_operations()
                        primer = self.math_c.get_random_primer()[0]
                        print(f"Пример - {primer} (Выйти с игры - /stop)")
                        otvet = input().strip()
                        if otvet == "/stop":
                            break
                        try:
                            otvet = int(otvet)
                            if otvet == primers[primer]:
                                up_money = random.randint(40,100)
                                data_player[1] += 1
                                if self.player_game.get_rank(data_player[1]) != data_player[4]:
                                    print(f"Ранг повышен - {self.player_game.get_rank(data_player[1])}")
                                    data_player[4] = self.player_game.get_rank(data_player[1])
                                data_player[3] += up_money 
                                print(f"Ответ верный - баланс: {data_player[3]}(+{up_money})")
                            else:
                                del_money = random.randint(40,100)
                                data_player[2] += 1
                                if data_player[3] - del_money <= 0:
                                    data_player[3] = 0
                                    print(f"Ответ не верный - баланс: {data_player[3]}")
                                else:
                                    data_player[3] -= del_money
                                    print(f"Ответ не верный - баланс: {data_player[3]}(-{del_money})")
                        except:
                              del_money = random.randint(40,100)
                              data_player[2] += 1
                              if data_player[3] - del_money <= 0:
                                data_player[3] = 0
                                print(f"Ответ не верный - баланс: {data_player[3]}")
                              else:
                                data_player[3] -= del_money
                                print(f"Ответ не верный - баланс: {data_player[3]}(-{del_money})")
                elif user_choise == "2":
                    print(f"\nНикнейм - {data_player[0]}\nПравильно решенные примеры - {data_player[1]}\nНеправильно решенные примеры - {data_player[2]}\nБаланс - {data_player[3]}\nРанг - {data_player[4]}")
                elif user_choise == "3":
                    status_code = 0
                    while status_code != 200:
                        new_name = input("Введите желаемый никнейм (Выйти - /stop):").strip()
                        status_code = self.player_game.change_name(new_name)
                        if status_code == 401:
                            print("Никнейм не должен совпадать с предыдущим, Введите новый: (Выйти - /stop)")                            
                            status_code = self.player_game.change_name(new_name)
                            if new_name == "/stop":
                                break

                        elif status_code == 400:
                            print("Ошибка , введите корректный никнейм :  (Выйти - /stop)")
                            status_code = self.player_game.change_name(new_name)
                            if new_name == "/stop":
                                break
                        elif status_code == 402:
                            break
                    if status_code == 200:
                        print(f"Ник изменен на : {new_name}")
                        data_player[0] = new_name
                            
                elif user_choise == "4":
                    self.player_game.download_new_info(data_player[0],data_player[1],data_player[2],data_player[3],data_player[4])
                    response_write_data = self.player_game.get_info()
                    response_write_data[1],response_write_data[2],response_write_data[3] = str(response_write_data[1]), str(response_write_data[2]), str(response_write_data[3])
                    with open("info.txt","w",encoding="utf-8") as file_insert:
                        file_insert.write(",".join(response_write_data))
                    print(f"Возвращайтесь {data_player[0]}!!")
                    break
        elif status_name == 400:
                    while status_name != 200:
                        print("Введите ваш никнейм")
                        name = input()
                        name = name.strip()
                        status_name = self.player_game.change_name(name)
                        if status_name == 200:
                            data_player[0] = name
                            with open("info.txt","w",encoding="utf-8") as f:
                                data_player[1],data_player[2],data_player[3] = str(data_player[1]), str(data_player[2]), str(data_player[3])
                                data_player = ",".join(data_player)
                                f.write(data_player)
                            self.start()
                           
                        else : 
                            print("Недопустимое Имя")
            
if __name__ == "__main__":
    start_game = Game()         
    start_game.start()
            