import sys


def cow_say_text():


	text = sys.argv[1:]

	string = ""
	words = " ".join(text)
	for i in range(0, len(words)):
		string += "_"

	print(string)
	print(words)
	print(string)


	print("""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    	 """) 


if __name__ == "__main__":
	cow_say_text()