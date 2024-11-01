f1 = open("text.txt", "r")

text = []

for line in f1.readlines():
    line = line.strip("\n")
    text.append(line)

del line
print(text)

for i in range(1, len(text)):
    values = text[i].split(" ")
    pos = 0
    for value in values:
        if value == "":
            value = text[i - 1].split(" ")[pos]
            values[pos] = value
            text[i] = ' '.join(values)
        pos += 1

print(text)
