def say_hi(name, age):
    if isinstance(name, str) and isinstance(age, int):
        return print(f"Hi. My name is {name} and I'm {age} years old")
    else:
        return print("Please, provide correct arguments")


say_hi("Sergii", 30)
