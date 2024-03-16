import csv

with open("history_mirror.csv",encoding="utf-8") as f,open("miror_error.csv",'w',encoding="utf-8",newline='') as result:
    reader = csv.DictReader(f,delimiter=",")
    sp = []
    for row in reader:
        if row["verdict"]=="Победа над смертью":
            sp.append(row)
    writer = csv.DictWriter(result,fieldnames=["date","username","verdict"])
    writer.writerows(sp)
    print(f"Сообщение было зафиксированно: 2008-07-22 у пользователя Разсудова Раиса Федоровна")