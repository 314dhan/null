def find_middle(arr):
    middle_index = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[middle_index - 1] + arr[middle_index]) / 2.0
    else:
        return arr[middle_index]

def fizzbuss(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    return n

# for i in range(1, 31):
#     print(fizzbuss(i))

print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,31)),sep='\n')