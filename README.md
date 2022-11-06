# Yatzy


# Installation

### Requirements
    - Python 3.10 +

### Install packeges
    - pip install -r requirements.txt

# Start app
    - python app.py

# Start test
    - python -m unittest test_app.py 


# Game info

### Player
```
 playerData = {
    'player_info': {
        'gender': 'M', 
        'firstname': 'John', 
        'lastname': 'Risnes', 
        'email': 'john.risnes@frisurf.no', 
        'phone': None, 
        'mobile': '46510490', 
        'dateOfBirth': '1988-01-19T00:00:00+01:00', 
        'age': 34 
    },
    'game_data': {
        'firstDice': '',
        'scoreBoard': {
            'only_one': '99',
            'only_two': '99',
            'only_three': '99',
            'only_four': '99',
            'only_five': '99',
            'only_six': '99',
            'one_pair': '99',
            'two_pair': '99',
            'three_of_kind': '99',
            'four_of_kind': '99',
            'full_house': '99',
            'small_straight': '99',
            'big_straight': '99',
            'yatzee': '99'
        },
        totalScore: 0
    }
}
```