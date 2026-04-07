# ===== WRITING =====
file = open("Hanni.txt","w")
file.write("Hanniel Rei L. Maningas\n")
file.write("Franz Gerald L. Roque\n")
file.close()
print("Sacesspul")


# ===== READING ====== (new file)
file = open("Hanni.txt", "r")
content = file.read()
file.close()
print(content)


# ===== APPENDING ===== (new file)
file = open("Hanni.txt", "a")
file.write("rawr")
file.close()


# ===== CHECKING IF FILE EXISTS ===== (new file)
import os

current = os.getcwd()
print(current)

# file_dir = os.path.join(file name)
file_dir = os.path.join(current, 'Hanni.txt')

if os.path.exists(file_dir):
    file = open("Hanni.txt","r")
    content = file.read()
    print(content)
else:
    print('file does not exists')