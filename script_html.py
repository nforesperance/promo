from bs4 import BeautifulSoup

with open("account_suspended.html", "r") as file:
	soup = BeautifulSoup(file, "html.parser")
#print html string
print(str(soup))