db_list = [{'name': 'Lisa', 'age': 20}]

def db_print():
    sorted(db_list, key = lambda db:db['age'])
    for db in db_list:
        print ("{}'s age is {}".format(db['name'], db['age']))
    print '\n'

def db_insert (name, age):
    db_list.append({"name":name, "age":age})

def db_delete_name(name):
    for db in db_list:
        if db["name"] == name:
            db_list.remove(db)

def db_delete_age(age):
    for db in db_list:
        if db["age"] == age:
            db_list.remove(db)


db_print()
db_insert('Nana', '19')
db_insert('Emily', '10')
db_print()
db_delete_name('Lisa')
db_print()
db_delete_age('10')
db_print()
