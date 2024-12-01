name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
ball = int(input("Balingizni kiriting: "))

if age > 17 and ball > 50:
    print(f"{name} siz o'qishga kirdingiz")
else:
    print(f"{name} siz o'qishga kira olmadingiz")
    