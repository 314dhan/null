def find_middle(arr):
    middle_index = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[middle_index - 1] + arr[middle_index]) / 2.0
    else:
        return arr[middle_index]

find_middle([102030])