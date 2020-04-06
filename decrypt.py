from generateTable import table


# we know that each key has one unique value
# so we can retrieve the key (initial character)
# just by knowing its value (encoded number)
def get_key(dic, val):
    for k, v in dic.items():
        if v == val:
            return k


with open("files/encrypted.txt") as file:
    numbers = file.readline().strip()

numbers = numbers.split(" ")

with open("files/decrypted.txt", "w", encoding="utf-8") as file:
    for n in numbers:
        file.write(get_key(table, int(n)))
