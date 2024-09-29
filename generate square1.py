def generate_squares(n):
    squares = [i ** 2 for i in range(1, n + 1)]
    print(squares)

num = int(input("Enter a number: "))
generate_squares(num)