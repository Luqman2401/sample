import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to a byte array
    image_bytes = image.tobytes()

    # Create an AES cipher object with the given key
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad the image bytes to a multiple of the block size
    padded_bytes = pad(image_bytes, AES.block_size)

    # Encrypt the padded bytes
    encrypted_bytes = cipher.encrypt(padded_bytes)

    # Save the encrypted bytes to a file
    with open(output_path, 'wb') as f:
        f.write(encrypted_bytes)

def decrypt_image(encrypted_path, key, output_path):
    # Read the encrypted bytes from the file
    with open(encrypted_path, 'rb') as f:
        encrypted_bytes = f.read()

    # Create an AES cipher object with the given key
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the encrypted bytes
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Unpad the decrypted bytes
    unpadded_bytes = unpad(decrypted_bytes, AES.block_size)

    # Convert the decrypted bytes back to an image
    image = np.frombuffer(unpadded_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Save the decrypted image to a file
    cv2.imwrite(output_path, image)

if __name__ == '__main__':
    # Set the path to the input image
    image_path = 'input_image.jpg'

    # Set the encryption key
    key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15'

    # Set the path to the output file
    output_path = 'encrypted_image.bin'

    # Encrypt the image
    encrypt_image(image_path, key, output_path)
    
def encrypt_image(image_path, key, output_path):
    try:
        # Open the image using PIL
        image = Image.open(image_path)
        image_bytes = image.tobytes()
        # ... rest of your encryption code ...
    except FileNotFoundError:
        print(f"Error: Image not found at '{image_path}'")
    except IOError:
        print(f"Error: Could not open image '{image_path}'")
    except Exception as e:
        print(f"Error: An error occurred while processing image: {e}")

    # Set the path to the encrypted file
    encrypted_path = output_path

    # Set the path to the decrypted image
    decrypted_path = 'decrypted_image.jpg'

    # Decrypt the image
    decrypt_image(encrypted_path, key, decrypted_path)
