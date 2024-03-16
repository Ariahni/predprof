import csv

def create_hash(s):
    hash_value = 0
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    d = {l: i for i, l in enumerate(alphabet, 1)}
    p = 67
    m = 10**9 + 9
    p_pow = 0
    for c in s:
        hash_value += (d[c]*p**p_pow)%m
        p_pow = p_pow+1
    return hash_value

with open("history_mirror.csv",encoding="utf-8") as f, open("users_with_hash.csv","w",encoding="utf-8") as res:
    reader = csv.DictReader(f, delimiter=",")
    writer = csv.DictWriter(res, fieldnames=["ID", "date", "username", "verdict"])
    with_hash = []
    for row in reader:
        row["ID"] = create_hash(row["username"])
        with_hash.append(row)
    writer.writerows(with_hash)
