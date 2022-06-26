import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()


	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
languages = b'\x00'

main(languages, input_encoding, error)

# error
#> python3.10 ex23.py utf-8 strict
# Traceback (most recent call last):
#   File "C:\Users\Nayef\OneDrive - Ministry of Education\Documents\Python\Learn Python 3 the Hard Way\Exercises\Exercise 23. Strings, Bytes, and Characters Encodings\Breaking it\BK1\ex23.py", line 22, in <module>
#     main(languages, input_encoding, error)
#   File "C:\Users\Nayef\OneDrive - Ministry of Education\Documents\Python\Learn Python 3 the Hard Way\Exercises\Exercise 23. Strings, Bytes, and Characters Encodings\Breaking it\BK1\ex23.py", line 5, in main
#     line = language_file.readline()
# AttributeError: 'bytes' object has no attribute 'readline'
# PS C:\Users\Nayef\OneDrive - Ministry of Education\Documents\Python\Learn Python 3 the Hard Way\Exercises\Exercise 23. Strings, Bytes, and Characters Encodings\Breaking it\BK1>