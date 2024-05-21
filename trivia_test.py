import time

msg = "Enter the date for which you want trivia, or enter \"exit\" to exit: "
dot = "."
print(msg)
while True:
    date = input()
    if date == "exit": break

    print("Please wait while the trivia is generated", end='')

    with open("trivia-service.txt", "wt", encoding="utf8") as f:
        f.write("D" + date)
    f.close()

    for i in range(3):
        time.sleep(1.5)
        print(dot, end='')
    print("\n", end='')

    with open("trivia-service.txt", "rt", encoding="utf8") as f:
        quote = f.read()
        quote = quote[1:]
    f.close()

    print("Your quote for the day is:")
    print(quote)

    print(msg)
