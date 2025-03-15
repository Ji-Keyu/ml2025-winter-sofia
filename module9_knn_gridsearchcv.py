import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


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

    print(
        f"Next, provide {user_input_N} pairs of numbers as training data, the first value is a real number and the second value is a non-negative integer")

    training_x = np.zeros(user_input_N)
    training_y = np.zeros(user_input_N)

    # Get x,y pairs
    for i in range(user_input_N):
        while True:
            user_input = input(
                f"Enter a real number as the first value, need {user_input_N-i} more pairs: ")
            if is_number(user_input):
                training_x[i] = float(user_input)
                break
            else:
                print("That did not work")

        while True:
            user_input = input(
                f"Enter a non-negative integer as the second value, need {user_input_N-i} more pairs: ")
            try:
                assert int(user_input) >= 0
                training_y[i] = int(user_input)
                break
            except Exception:
                print("That did not work")

    # Get M
    while True:
        try:
            user_input_M = int(input("Enter a positive integer as M: "))
            assert user_input_M > 0
            break
        except Exception:
            print("That did not work")

    test_x = np.zeros(user_input_M)
    test_y = np.zeros(user_input_M)

    print(
        f"Next, provide {user_input_M} pairs of numbers as test data, the first value is a real number and the second value is a non-negative integer")

    # Get x,y pairs
    for i in range(user_input_M):
        while True:
            user_input = input(
                f"Enter a real number as the first value, need {user_input_M-i} more pairs: ")
            if is_number(user_input):
                test_x[i] = float(user_input)
                break
            else:
                print("That did not work")

        while True:
            user_input = input(
                f"Enter a non-negative integer as the second value, need {user_input_M-i} more pairs: ")
            try:
                assert int(user_input) >= 0
                test_y[i] = int(user_input)
                break
            except Exception:
                print("That did not work")

    gs_knn = GridSearchCV(
        KNeighborsClassifier(),
        param_grid={"n_neighbors": range(1, 11)},
        scoring="accuracy",
        cv=5
    )

    gs_knn.fit(training_x.reshape(-1, 1), training_y)
    print(f"Best k: {gs_knn.best_params_['n_neighbors']}")
    print(f"Best score: {gs_knn.best_score_}")

    best_model = gs_knn.best_estimator_
    predictions = best_model.predict(test_x.reshape(-1, 1))
    test_accuracy = best_model.score(test_x.reshape(-1, 1), test_y)
    print(f"Predictions: {predictions}")
    print(f"Actual: {test_y}")
    print(f"Test Accuracy: {test_accuracy}")


if __name__ == "__main__":
    main()
