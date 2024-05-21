import time

with open("trivia.txt", "rt", encoding="utf8") as f:
    trivia_lines = f.read()
f.close()
trivia_lines = trivia_lines.splitlines(0)

while True:
    time.sleep(1)
    with open("trivia-service.txt", "rt", encoding="utf8") as f:
        trivia_service = f.read()
    f.close()

    if trivia_service:
        if trivia_service[0] == "D":
            date = trivia_service[1:]
            for line in trivia_lines:
                if line[:5] == date:
                    quote = line[5:]
                    with open("trivia-service.txt", "wt", encoding="utf8") as f:
                        f.write(quote)
                    f.close()
