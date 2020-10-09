def hour_glass_sum(array):
    answer = -64
    # or
    # answer = None

    for row in range(0, 4):
        for column in range(0, 4):
            total = array[row][column] + array[row][column + 1] + array[row][column + 2] + \
                    array[row + 1][column + 1] + \
                    array[row + 2][column] + array[row + 2][column + 1] + array[row + 2][column + 2]
            if answer is None or total > answer:
                answer = total

    return answer

print(hour_glass_sum([[1, 1, 1, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0],
                      [1, 1, 1, 0, 0, 0],
                      [0, 0, 2, 4, 4, 0],
                      [0, 0, 0, 2, 0, 0],
                      [0, 0, 1, 2, 4, 0]]))