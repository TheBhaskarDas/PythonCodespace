def exmet(name):
    return f"Hello, {name}!"

def main():
    name = input("Enter Your Name: \n")
    message = exmet(name)
    print(message)

if __name__ == "__main__":
    main()