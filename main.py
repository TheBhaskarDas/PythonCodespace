from codesnips.fundamentals.var_lit import variable_literals
from codesnips.fundamentals.type_conversion import type_conv

def exmet(name):
    return f"Hello, {name}!"

def main():
    name = input("Enter Your Name: \n")
    message = exmet(name)
    print(message)

if __name__ == "__main__":
    main()

# https://chatgpt.com/share/766ee46f-1ff3-4508-8121-517b108deceb