Arab_Countries = {

    'Bahrain': 'Manama',
    'Suadi Arabia': 'Ryadh',
    'Jordan': 'Amman',
    'Lybia': 'Tripoli',
    'Kuwait': 'Kuwait City',
    'Egypt': 'Cairo',
    'Morocco': 'Rabat',
    'Qatar': 'Doha',
    'Yemen': 'Sana\'a',
    'UAE': 'Abu Dhabi',
    'Tunisia': 'Tunis',
    'Sudan': 'Khartoum',
    'Oman': 'Muscat',
    'Syria': 'Damascus',
    'Algeria': 'Algiers',
    'Iraq': 'Baghdad',
    'Djibouti': 'Djibouti',
    'Mauritania': 'Nouakchott',
    'Somalia': 'Mogadishu',
    'Palestine': 'Alquds',
    'Lebanon': 'Beirut',
    'Comoros': 'Moroni'
}

Arab_Countries_Size = {

    'Manama': f"{30}",
    'Ryadh': f"{404240}",
    'Amman': f"{1680}",
    'Tripoli': f"{14}",
    'Kuwait City': f"{8}",
    'Cairo': f"{3084.676}",
    'Rabat': f"{118}",
    'Doha': f"{260}",
    'Sana\'a': f"{5552}",
    'Abu Dhabi': f"{67.34}",
    'Tunis': f"{212.63}",
    'Khartoum': f"{1683.5}",
    'Muscat': f"{3.5}",
    'Damascus': f"{105}",
    'Algiers': f"{363}",
    'Baghdad': f"{2042}",
    'Djibouti City': f"{23.2}",
    'Nouakchott': f"{1036}",
    'Mogadishu': f"{104}",
    'Alquds': f"{125156}",
    'Beirut': f"{198}",
    'Moroni': f"{1862}"
    
}

capital_counter = 0
for country, capital in list(Arab_Countries.items()):
    print("The capital city of {0} is {1}".format(country, capital))
    Mylist = list(Arab_Countries_Size.items())
    current_list = Mylist[capital_counter]; capital_counter += 1
    print(f"The total geographical area of {capital} is {current_list[1]}Km²\n")


number = 0
target = 1

total = len(Arab_Countries)
total_kms = 0

for _ in range(total):

    Mylist = list(Arab_Countries_Size.items())
    current_list = Mylist[number]; number += 1
    total_kms += float(current_list[target]) // 1

print(f"The total geographical area for capitals is {int(total_kms)}Km²\n")
print("The total of arabic countries is {0}\n".format(total))
