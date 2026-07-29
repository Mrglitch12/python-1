def check_vowel(check):
    if check in vowels:
        print(check, "is a vowel sound")
    else:
        print(check, "is not a vowel sound")

vowels = "aeiouAEIOU"
check = input("Enter a letter: ")
check_vowel(check)