import string
import random
import datetime

def logo():
    print(""" 
    
    _______     _       ______    ______     ______  ________  ____  _____  
|_   __ \   / \    .' ____ \ .' ____ \  .' ___  ||_   __  ||_   \|_   _| 
  | |__) | / _ \   | (___ \_|| (___ \_|/ .'   \_|  | |_ \_|  |   \ | |   
  |  ___/ / ___ \   _.____`.  _.____`. | |   ____  |  _| _   | |\ \| |   
 _| |_  _/ /   \ \_| \____) || \____) |\ `.___]  |_| |__/ | _| |_\   |_  
|_____||____| |____|\______.' \______.' `._____.'|________||_____|\____| 
                            by:CoderSigma
    
    """)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(length)]
    return "".join(password)

def save_to_file(password, filename):
    with open(filename, "w") as file:
        file.write(password)

def main():
    length = int(input("Enter password length: "))
    
    password = generate_password(length)
    cleaned_password = password.replace(" ", "")
    
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d_%H%M%S")
    
    filename = f"{formatted_time}_password.txt"
    
    save_to_file(cleaned_password, filename)
    
    print(f"Generated password: {cleaned_password}")
    print(f"Password saved to {filename}")

if __name__ == "__main__":
    logo()
    main()
