def sum(x,y):
    return x + y

def is_greater_than(x,y):
    return x > y

def login(user, password):
    if user == "admin" and password == "secret":
        return True
    return False