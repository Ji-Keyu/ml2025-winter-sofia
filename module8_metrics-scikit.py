import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import precision_score, recall_score


def is_number(input_string):
    try:
        float(input_string)
        return True
    except Exception:
        return False


def main():
    # Get N
    while True:
        try:
            user_input_N = int(input("Enter a positive integer as N: "))
            assert user_input_N > 0
            break
        except Exception:
            print("That did not work")

    print(f"Next, provide {user_input_N} pairs of bits")

    x_values = np.zeros(user_input_N)
    y_values = np.zeros(user_input_N)

    # Get x,y pairs
    for i in range(user_input_N):
        while True:
            user_input = input(
                f"Enter a number as the first value, need {user_input_N-i} more pairs: ")
            if user_input == "0" or user_input == "1":
                x_values[i] = int(user_input)
                break
            else:
                print("That did not work, please enter 0 or 1")

        while True:
            user_input = input(
                f"Enter a number as the second value, need {user_input_N-i} more pairs: ")
            if user_input == "0" or user_input == "1":
                y_values[i] = int(user_input)
                break
            else:
                print("That did not work, please enter 0 or 1")

    # X is the ground truth, Y is the prediction
    precision = precision_score(x_values, y_values)
    recall = recall_score(x_values, y_values)
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()
