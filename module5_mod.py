class Guess:
    def __init__(self):
        self.user_input_N = 0
        self.user_input_record = []
        self.user_input_X = 0

    def is_number(self, input_string):
        try:
            float(input_string)
            return True
        except Exception:
            return False

    def get_user_input_N(self):
        while True:
            try:
                self.user_input_N = input("Enter a positive integer: ")
                self.user_input_N = int(self.user_input_N)
                assert self.user_input_N > 0
                break
            except Exception:
                print("That did not work")

    def get_user_input_record(self):
        for i in range(self.user_input_N):
            while True:
                user_input = input(f"Enter a number, need {
                                   self.user_input_N-i} more: ")
                if self.is_number(user_input):
                    self.user_input_record.append(user_input)
                    break
                else:
                    print("That did not work")

    def get_user_input_X(self):
        while True:
            try:
                self.user_input_X = input("Finally, enter an integer: ")
                int(self.user_input_X)
                break
            except ValueError:
                print("That did not work")
        if self.user_input_X in self.user_input_record:
            print(str(self.user_input_record.index(self.user_input_X)+1))
        else:
            print("-1")
