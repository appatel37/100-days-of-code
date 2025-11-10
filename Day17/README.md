# Day 17 - File Handling Practice

# 1 - Writing to a file
with open("data.txt", "w") as file:
    file.write("Day 17 - File Handling Practice\n")
    file.write("Learning how to read and write files\n")
    file.write("Python makes it easy!\n")

print("File written successfully!\n")

# 2 - Reading from the file
with open("data.txt", "r") as file:
    content = file.read()
    print("📄 File contents after writing:\n")
    print(content)

# 3 - Appending new data
with open("data.txt", "a") as file:
    file.write("Appended line successfully!\n")

print("\n➕ New line appended successfully!\n")

# 4 - Reading the updated file
with open("data.txt", "r") as file:
    updated_content = file.read()
    print("📄 Final file contents:\n")
    print(updated_content)