x = [ [5,2,3], [10,8,9] ] 
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]['first_name']='Bryant'
print(students)

sports_directory['soccer'][0]='Andres'
print(sports_directory)

z[0]['y']= 30
print(z)





students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
  for i in range (len(some_list)):
    key = some_list[i]
    for value in key:
      print(f"{value}:{key[value]},", end="")

iterateDictionary(students)



print("**"*20)



def iterateDictionary2(key_name, some_list):
  for i in range (len(some_list)):
    print(some_list[i][key_name])

iterateDictionary2('first_name',students)

print("**"*20)

iterateDictionary2('last_name',students)



dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for i in range(len(some_dict)):
    dojo=some_dict[i]
    



printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
