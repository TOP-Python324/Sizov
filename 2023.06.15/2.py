def deck() -> tuple[int, str]:
    """Создаёт упорядоченную колоду карт"""
    
    suits = ['черви', 'бубны', 'пики', 'трефы']
    
    for suit in suits: 
        for nominal in range(2, 15): 
            yield (nominal, suit)
        

# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
