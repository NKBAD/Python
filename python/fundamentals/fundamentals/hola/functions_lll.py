x = [ [5,2,3], [10,8,9] ] 

x [1] [0] = 15 
print(x)

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes [0] ["last_name"] = "bryant"
print(estudiantes)


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes ["fútbol"] [0] = "andres"
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]

z [0] ["y"] = 30 
print(z)



estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary (list):
    for i in range(0 , len(list)):
        output =" "
        for key, val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterateDictionary(estudiantes)


def iterate_dictionary2( key_name , list): 
    for i in range ( 0 , len(list)): 

        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2 ("first_name" , estudiantes)
iterate_dictionary2 ("last_name", estudiantes)


dojo = {
    "ubicaciones": ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    "instructores": ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
print_info(dojo)