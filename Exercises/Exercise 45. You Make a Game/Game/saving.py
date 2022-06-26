class save(object):

    def GetLine(self, name, string, dict):
        with open(name, 'r') as saving:
            for line in saving:
                if string in line:
                    for word in line:

                        list = line.split(" ")
                        position_key = 0
                        position_value = 1

                        for i in range(1):
                            dict[list[position_key]] = list[position_value]
                            position_key += 1
                            position_value += 1

                    return line
    

    def AddLine(self, name, variable, value):
        with open(name, 'a') as saving:
            saving.write(f"\n{variable} = {value}")
    

    def Switch(self, name, line, information):
        with open(name, 'r') as saving:
            all_file = saving.read()
            with open(name, 'r') as saving:
                string = saving.readlines()
                with open(name, 'w') as saving:
                    old = string[line-1].split()[2:]

                    # Will make changes if items was more than two
                    old = ' '.join(old)
                    new = information
                    edited_string = string[line-1].replace(old, new)
                    saving.write(all_file.replace(string[line-1], edited_string))