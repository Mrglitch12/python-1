def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

n = int(input("Enter a number: "))
check_even_odd(n)