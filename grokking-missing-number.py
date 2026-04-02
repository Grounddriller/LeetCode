def first_k_missing_numbers(arr, k):
    i = 0

    while i < len(arr):
        correct = arr[i] - 1
        if 1 <= arr[i] <= len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()

    for i in range(len(arr)):
        if len(missing_numbers) < k and arr[i] != i + 1:
            missing_numbers.append(i + 1)
            extra_numbers.add(arr[i])

    next_number = len(arr) + 1
    while len(missing_numbers) < k:
        if next_number not in extra_numbers:
            missing_numbers.append(next_number)
        next_number += 1

    return missing_numbers
