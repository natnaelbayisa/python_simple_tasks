file = open("./text.txt", "w")

for i in range(1000):
    file.write(f"{i+1}. \n")
file.close()