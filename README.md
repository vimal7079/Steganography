# Image Steganography in Python

This project demonstrates a simple image steganography technique using Python and OpenCV. It allows you to hide a secret message within an image.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)

## Introduction

Steganography is the practice of hiding a secret message within a larger one in such a way that someone cannot know the presence or contents of the hidden message. This project hides a binary message within the pixel values of an image.

## Features

- Read and display images using OpenCV.
- Convert a secret message into its binary representation.
- Embed the binary message into the least significant bits of the image pixels.
- Save the modified image with the hidden message.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/image-steganography.git
    cd image-steganography
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Place the image you want to use in the project directory and name it `image.jpeg`.

2. Run the script:
    ```sh
    python steganography.py
    ```

3. Enter the message you want to hide when prompted.

4. The script will create a new image file named `image_with_hidden_message.png` with the hidden message embedded in it.

## How it Works

### Embedding the Message

1. **Reading the Image**: The script reads an image file using OpenCV.
    ```python
    image = cv2.imread('image.jpeg')
    ```

2. **Converting the Message to Binary**: The input message is converted into a binary string.
    ```python
    binary = ''
    for char in hidden_msg:
        binary += format(ord(char), '08b')
    ```

3. **Embedding the Message**: The binary message is embedded into the least significant bits of the image's pixel values.
    ```python
    for row in range(height):
        for col in range(width):
            for channel in range(channels):
                if len(temp_msg) == 0:
                    break
                pixel_value = image[row][col][channel]
                pixel_value_binary = format(pixel_value, '08b')
                new_pixel_value = pixel_value_binary[:-2] + temp_msg[:2]
                temp_msg = temp_msg[2:]
                image[row][col][channel] = int(new_pixel_value, 2)
    ```

4. **Saving the Modified Image**: The modified image with the hidden message is saved as a new file.
    ```python
    cv2.imwrite('image_with_hidden_message.png', image)
    ```
### Extracting a Message

1. **Reading the Image**: The script reads the image file containing the hidden message.
    ```python
    image = cv2.imread("new_image.png")
    ```

2. **Extracting the Binary Message**: The script extracts the binary message from the least significant bits of the image's pixel values.
    ```python
    binary_msg += bin(image[row][col][channel])[-2:]
    if len(binary_msg) == 8:
        temp = chr(int(binary_msg, 2))
        hidden_msg += temp
        binary_msg = ''
        if '**' in hidden_msg:
            break
    ```

3. **Printing the Hidden Message**: The hidden message is printed to the console.
    ```python
    print("Hidden Message:", hidden_msg[:-2])
    ```
