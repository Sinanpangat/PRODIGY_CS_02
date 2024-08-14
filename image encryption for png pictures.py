from PIL import Image

def encryption_decryption():
    while True:
        try:
            key = int(input("Enter your key between 1-255 (inclusive):\n"))
            if not 1 <= key <= 255:
                print("Invalid key. Please enter a value between 1 and 255.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_img = Image.new(img.mode, img.size)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g , b , a = img.getpixel((x, y))
            new_pixel = (r ^ key, g ^ key, b ^ key,a ^ key)
            new_img.putpixel((x, y), new_pixel)
    save_path=input("enter image path to save :")
    new_img.save(save_path) # Replace with your desired file path
    
while True:

    try:
        print("enter your choise:")
        choice = input("\nEnter your choice:\n" 
                   "1. Encryption\n"
                   "2. Decryption\n"
                   "3. Exit\n\n")
        if choice=='1':
            image_path=input("enter image path:")
            img = Image.open(image_path)
            encrypt=encryption_decryption()
        elif choice=='2':        
            image_path=input("enter image path:")
            img = Image.open(image_path)
            decrypt=encryption_decryption()
        else:
            break   
    except FileNotFoundError:
            print("Error: Invalid image path provided.")

   

  
    