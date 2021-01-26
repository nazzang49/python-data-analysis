# open file
data = open("../documents/00_Material(Uploaded)/00_data/text_data.txt", 'r', encoding="utf-8-sig")

# close file
data.close()

# with => auto close
with open("../documents/00_Material(Uploaded)/00_data/text_data.txt", 'r', encoding="utf-8-sig") as desc:
    print("auto close")

# read whole line => each line on list element
data = open("../documents/00_Material(Uploaded)/00_data/text_data.txt", 'r', encoding="utf-8-sig")
for line in data.readlines():
    print(line)

# read 1 line
data = open("../documents/00_Material(Uploaded)/00_data/text_data.txt", 'r', encoding="utf-8-sig")
print(data.readline())

# read whole text
data = open("../documents/00_Material(Uploaded)/00_data/text_data.txt", 'r', encoding="utf-8-sig")
print(data.read())

data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'w', encoding="utf-8-sig")
data.write("박진영\n")
data.write("박진수\n")

# add line on original file
data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'a', encoding="utf-8-sig")
data.write("추가 구문 by a 옵션")

data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'r', encoding="utf-8-sig")
print(data.read())

# remove element
data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'r', encoding="utf-8-sig")
list = data.readlines()
del list[1]
print(list)

# restore
data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'w', encoding="utf-8-sig")
for str in list:
    data.write(str)

data = open("../documents/00_Material(Uploaded)/00_data/text_data_write.txt", 'r', encoding="utf-8-sig")
print(data.read())