def palindrome_check(a):
    b = str(a)
    end = len(b) - 1
    d = ""
    for i in range(len(b)):
        d += b[end]
        end -= 1
    d = int(d)
    if a == d:
        return f"this is palindrome number {a}."
    else:
        return f"this is not palindrome number {a}."

a = int(input("Enter your number:- "))
print(palindrome_check(a))
