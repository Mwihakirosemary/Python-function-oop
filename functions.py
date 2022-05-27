from unicodedata import name


def hello(name,age):
    year = 2022 - age
    print(f"Hello {name},you were born in {year}")
    print(f"Hello {name}")
    # templete

def hello(name,age):
    year = 2022 - age
    # print(f"Hello welcome to Akirachix")
    # return
    return f"Hello {name},you were born in {year}"

def my_country(country = "Uganda",student = "Susan"):
    return f"Hello {student}you are from {country}"

def my_country (country = "Rwanda",student = "Verite"):
    return f"Hello {student} you are from {country}"


# converts to a tuple
def greet_multiple(*names):
    for name in names:
        print(f"Hello {name}")
# converts to dict
def greet_multiple(**kwargs):   
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

def greet_multiple(**kwargs):
    keys = kwargs.keys()
    if "contry" in keys:
        print(f"Hello {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in keys:
        year = 2022 - kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif not kwargs:
        print(f"Hello anonymous")

def sum_and_greet(*args,**kwargs):
    sum = 0
    for num in args:
        sum+=num
    keys = kwargs.keys()
    if "name" in keys:
        print(f"Hello {kwargs['name']} the answer is {sum}")
    elif "country" in keys:
        print(f"Hello {kwargs['country']} the answer is {sum}")
    elif not kwargs:
        print(f"Hello the anwer is {sum}")

def sum(*nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum

def multiply(*nums):
    ans = 1
    for num in nums:
        ans*=num
    return ans
