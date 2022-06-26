import sys
script, input_encoding, error = sys.argv

def main(language_file, org_file, encoding, errors):
    line = language_file.readline().encode('raw_unicode_escape')
    org_line = org_file.readline()

    if line:
        print_line(line, org_line, encoding, errors)
        return main(language_file, org_file, encoding, errors)

def print_line(line, org_line, encoding, errors):
    next_lang = line.strip()
    string = next_lang.decode(encoding, errors)
    bytes = string.encode(encoding, errors)
    
    print(org_line, "<===>", bytes)


languages = open("languages.txt", 'r', encoding='unicode_escape')
original_file = open("languages.txt", 'r')

main(languages, original_file, input_encoding, error)

languages.close()