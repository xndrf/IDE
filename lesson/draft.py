from random import randint

def attack(char_name, char_class):
    if char_class == 'warrior':
        return (
            f'{char_name} нанес урон противнику равный {5 + randint (3, 5)}'
            )
    elif char_class == 'mage':
        return (f'{char_name} нанес урон противнику равный \
                {5 + randint (5, 10)}')
    return (f'{char_name} нанес урон противнику равный;'
            f'{5 + randint (-3, -1)}')
    
def defence (char_name, char_class):
    