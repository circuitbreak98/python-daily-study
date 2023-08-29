import operator
PEOPLE = [{
    'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'
}, {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'
}, {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'
}, {'first':'Alan', 'last':'Putin',
    'email':'president@kremvax.ru'
}]

def alphabetize_names1():
    s = sorted(PEOPLE, key=operator.itemgetter('first'))
    return sorted(s, key=operator.itemgetter('last'))

def alphabetize_names2():
    people = sorted(PEOPLE, key=lambda x: [x['last'], x['first']])
    return people 
    '''for person in people:
        print(f'{person["last"]}, {person["first"]}, {person["email"]}')
    '''
def alphabetize_names():
    people = sorted(PEOPLE, key=operator.itemgetter('last', 'first'))
    return people 

print(alphabetize_names())
#alphbetize_names()

