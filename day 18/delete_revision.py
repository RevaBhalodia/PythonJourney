#Check if a file named old.txt exists.If it exists, delete it.
#Write a program that prints:"File deleted" if deleted,"File not found" if it doesn’t exist
import os

if os.path.exists("old.txt"):
    os.remove("old.txt")
    print("file deleted")
else:
    print("file not found")

