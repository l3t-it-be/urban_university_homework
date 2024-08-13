my_dict = {
    'Professions needed': [
        'Project Manager',
        'Business Analyst',
        'DevOps',
        'Frontend Engineer',
        'Backend Engineer',
        'QA',
    ],
    'Frontend': ('HTML', 'CSS', 'JavaScript'),
    'Backend': ('Java', 'Python'),
    'Database': 'PostgreSQL',
}

print(my_dict)

print(my_dict.get('Backend'))
print(my_dict.get('Salary'))

my_dict['API'] = 'REST'
my_dict['Frameworks'] = ('Django', 'React', 'Vue')

database = my_dict.pop('Database')
print(database)

print(my_dict)

my_set = {'Kate', 2000, 5.5, 'Python', 5.5, 'Urban University', 'Kate', 1000}
print(my_set)

my_set.add('Awesome')
my_set.add(-3)
my_set.discard(1000)

print(my_set)
