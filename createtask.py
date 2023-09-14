signs = {"Pig": 1957, "Dog": 1958, "Rooster": 1959, "Monkey": 1960, "Sheep": 1961, "Horse": 1962, "Snake": 1963, "Dragon": 1964, "Rabbit": 1965, "Tiger": 1966, "Ox": 1967, "Rat": 1968}
birth_year = input("What year were you born?")
birth_year = int(birth_year)

def check_animals(birth_year,animal):
    while birth_year >= signs[animal]:
        birth_year = birth_year - 12
        if birth_year == signs[animal]:
            return True   
    return False     

        

for animal in signs:
    if check_animals(birth_year, animal):
        print(animal)