import csv

K = 1
while K != 0:
    names = input()
    if names == "stop":
        break
    else:
        with open("history_mirror.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                if names in row["username"]:
                    print(f"Предсказание для {row["username"]} - {row["verdict"]}")
                    break
                else:
                    print("Вас не нашлось в записях")
                    break


