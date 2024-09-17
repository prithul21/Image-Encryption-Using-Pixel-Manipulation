# Image-Encryption-Using-Pixel-Manipulation

This project showcases a basic image encryption and decryption technique using pixel manipulation. The encryption is done by modifying pixel values of an image with a Caesar Cipher approach, where each pixel is shifted by a key value. This project is part of **Prodigy Infotech Task 2**.

## Features:
- Encrypts an image by modifying its pixel values with a given key.
- Decrypts the encrypted image back to its original form using the same key.
- Simple and efficient, using Python libraries like `PIL` and `NumPy`.

## How It Works:
1. **Encryption**: The pixel values of the image are adjusted by adding the key value to each pixel. The result is taken modulo 256 to ensure pixel values remain in the valid range (0-255).
2. **Decryption**: The encrypted pixel values are adjusted by subtracting the key value, restoring the image to its original state.

## Requirements:
- Python 3.x
- `PIL` (Pillow)
- `NumPy`

You can install the dependencies using:
```bash
pip install pillow numpy
