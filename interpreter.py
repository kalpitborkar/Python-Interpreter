

class Interpreter:
    def __init__(self):
        self.stack = []
    
    def LOAD_VALUE(self, number):
        self.stack.append(number)
        
    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)
    
    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    
