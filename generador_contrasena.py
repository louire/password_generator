import random
def generate_password():
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 
        'T', 'U', 'V', 'X', 'Y', 'Z']
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 
        't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', 
        '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', 
        '°', '^', '&', '$', '#', '"']
    
    characters = UPPER + LOWER + NUMS + CHARS
    
    password = []
    
    for i in range(10):
        characters_random = random.choice(characters)
        password.append(characters_random)
    
    password = "".join(password)
    return password
        
    
def main():
    password = generate_password()
    print("Your new password is: " + password)

#Comentariooooo UwU
if __name__ == "__main__":
    main()
