import sys


def cow_say_text():


	text = sys.argv[1:]

	string = " "
	string2 = " "
	words = " ".join(text)
	for i in range(0, len(words) + 2):
		string += "_"
		string2 += "-"

	print(string)
	print("< " + words + " >")
	print(string2)


	print("""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    	 """) 


if __name__ == "__main__":
	cow_say_text()