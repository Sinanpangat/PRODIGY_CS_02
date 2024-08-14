from PIL import Image

def encryption_decryption():
    key =100
    new_img = Image.new(img.mode, img.size)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g , b , a = img.getpixel((x, y))
            new_pixel = (r ^ key, g ^ key, b ^ key,a ^ key)
            new_img.putpixel((x, y), new_pixel)
    #save_path=input("enter image path to save :")
    new_img.save(image_path) # Replace with your desired file path
    
while True:
    print("enter your choise:")
    choice = input("\nEnter your choice:\n" 
                   "1. Encryption\n"
                   "2. Decryption\n"
                   "3. Exit\n\n") 
    if choice=='1':  
        image_path=input("enter image path:")
        img = Image.open(image_path) # Replace with your image file path
        encrypt=encryption_decryption()
    elif choice=='2':
        image_path=input("enter image path:")
        img = Image.open(image_path) # Replace with your image file path
        decrypt=encryption_decryption()
    else:
        break

  
    