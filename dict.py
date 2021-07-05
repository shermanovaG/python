
lugat = {
	"book": "kitob",
	"friend": "do'st",
	"family": "oila",
	"city": "shahar"
}

soz = input("soz kirit").lower()

if soz in lugat:
	print(lugat[soz])
else:
	print("404 ERROR")