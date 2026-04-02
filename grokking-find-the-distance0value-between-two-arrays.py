def find_the_distance_value(arr1, arr2, d):
    count = 0

    for num1 in arr1:
        valid = True

        for num2 in arr2:
            if abs(num1 - num2) <= d:
                valid = False
                break

        if valid:
            count += 1

    return count
