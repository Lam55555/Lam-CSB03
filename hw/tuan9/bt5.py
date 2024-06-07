names = {
  'students': [
    {'firstName': 'Nikki', 'lastName': 'Roysden'},
    {'firstName': 'Mervin', 'lastName': 'Friedland'},
    {'firstName': 'Aron', 'lastName': 'Wilkins'}
  ],
  'teachers': [
    {'firstName': 'Amberly', 'lastName': 'Calico'},
    {'firstName': 'Regine', 'lastName': 'Agtarap'}
  ]
}

print('List of students:')
for x in names['students']:
    print(f"-{x['firstName']} {x['lastName']}")
print('List of teachers:')
for y in names['teachers']:
    print(f"-{y['firstName']} {y['lastName']}")
