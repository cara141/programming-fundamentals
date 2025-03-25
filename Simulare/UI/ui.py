from Controller.controller import SpeciesController

class UI:
    def __init__(self, file_name):
        self.controller = SpeciesController(file_name)

    def run(self):
        while True:
            command = input(">>>")
            if command == "1":
                date = input()
                result = self.controller.get_earlier_than(date)
                for animal in result:
                    print(animal.__str__())
                    print("\n")
            elif command == "2":
                statistics = self.controller.get_statistics()
                for result in statistics:
                    print(result[0] + ": " + result[1] + ", " + str(result[2]))
            else:
                print("Input invalid!")