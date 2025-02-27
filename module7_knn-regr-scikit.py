import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor


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

    # Get k
    while True:
        try:
            user_input_k = int(input("Enter another positive integer as k: "))
            assert user_input_k > 0
            break
        except Exception:
            print("That did not work")

    print(f"Next, provide {user_input_N} pairs of numbers")

    x_values = np.zeros(user_input_N)
    y_values = np.zeros(user_input_N)

    # Get x,y pairs
    for i in range(user_input_N):
        while True:
            user_input = input(
                f"Enter a number as the first value, need {user_input_N-i} more pairs: ")
            if is_number(user_input):
                x_values[i] = float(user_input)
                break
            else:
                print("That did not work")

        while True:
            user_input = input(
                f"Enter a number as the second value, need {user_input_N-i} more pairs: ")
            if is_number(user_input):
                y_values[i] = float(user_input)
                break
            else:
                print("That did not work")

    user_input_x = np.array(x_values)
    user_input_y = np.array(y_values)

    # Get X input
    while True:
        try:
            user_input_X = float(input("Finally, enter a number: "))
            break
        except ValueError:
            print("That did not work")

    if user_input_k <= user_input_N:
        X = user_input_x.reshape(-1, 1)
        knn = KNeighborsRegressor(n_neighbors=user_input_k)
        knn.fit(X, user_input_y)
        prediction = knn.predict([[user_input_X]])
        print(f"Predicted value: {prediction[0]}")
    else:
        print("Error: k must be less than or equal to N")

    scaler = StandardScaler()
    y_reshaped = user_input_y.reshape(-1, 1)
    scaler.fit(y_reshaped)
    print(f"Variance of labels in the training dataset is: {scaler.var_[0]}")


if __name__ == "__main__":
    main()
