# 99DaysWithCPC

# Opening .txt files for this program

# Open the file in read mode
# Open the file with a relative path
# Open the file with the absolute path

from config import TEST_FILE_PATH

# with open(TEST_FILE_PATH, "r") as file:
#     for line in list(file):
#         print(line)


# Write some file

with open(TEST_FILE_PATH, "a") as file:
    file.write("\nAdding more text into void3")
