def get_description():
    """Return random veather. Just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog',
                     'sun', 'who knows']
    return choice(possibilities)