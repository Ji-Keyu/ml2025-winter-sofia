def is_number(input_string):
    try:
        float(input_string)
        return True
    except Exception:
        return False


def main():
    while True:
        try:
            user_input_N = input("Enter a positive integer: ")
            user_input_N = int(user_input_N)
            assert user_input_N > 0
            break
        except Exception:
            print("That did not work")
    user_input_record = []
    for i in range(user_input_N):
        while True:
            user_input = input(f"Enter a number, need {user_input_N-i} more: ")
            if is_number(user_input):
                user_input_record.append(user_input)
                break
            else:
                print("That did not work")
    while True:
        try:
            user_input_X = input("Finally, enter an integer: ")
            int(user_input_X)
            break
        except ValueError:
            print("That did not work")
    if user_input_X in user_input_record:
        print(str(user_input_record.index(user_input_X)+1))
    else:
        print("-1")


if __name__ == "__main__":
    main()
