import random
import string

url_db = {}

def shorten_url(long_url):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[short] = long_url
    return short

def get_original(short):
    return url_db.get(short, "Not found")


long_url = input("Enter URL: ")
short = shorten_url(long_url)

print("Short URL:", short)
print("Original URL:", get_original(short))