from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.int16)  # Convert to int16 to avoid overflow
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    
    # Convert back to uint8 and save the image
    encrypted_array = encrypted_array.astype(np.uint8)
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save('C:/Users/PRITHUL/Desktop/codes/IMAGES/encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png' in the IMAGES folder.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image, dtype=np.int16)  # Convert to int16 to avoid underflow
    
    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (encrypted_array - key) % 256
    
    # Convert back to uint8 and save the image
    decrypted_array = decrypted_array.astype(np.uint8)
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save('C:/Users/PRITHUL/Desktop/codes/IMAGES/decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png' in the IMAGES folder.")

# Example usage
key = 50  # Change this key to anything you like
encrypt_image('C:/Users/PRITHUL/Desktop/codes/IMAGES/input_image.png', key)
decrypt_image('C:/Users/PRITHUL/Desktop/codes/IMAGES/encrypted_image.png', key)
