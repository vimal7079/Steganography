import cv2

# To Read the image (remove the 0 to read it as a color image)
image = cv2.imread('image.jpeg')

# To View the image
cv2.imshow("vimal", image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

hidden_msg = input("Enter your message to hide: ") + '**'

binary = ''
for char in hidden_msg:
    binary += format(ord(char), '08b')

print('Binary Message: ', binary)

# Get the dimensions of the image
height, width, channels = image.shape

print('Height:', height, 'Width:', width, 'Channels:', channels)

# To hide the message into an image
temp_msg = binary
for row in range(height):
    for col in range(width):
        for channel in range(channels):
            if len(temp_msg) == 0:
                break
            print(image[row][col][channel])
            pixel_value = image[row][col][channel]
            pixel_value_binary = format(pixel_value, '08b')
            new_pixel_value = pixel_value_binary[:-2] + temp_msg[:2]
            temp_msg = temp_msg[2:]
            image[row][col][channel] = int(new_pixel_value, 2)
        if len(temp_msg) == 0:
            break
    if len(temp_msg) == 0:
        break

# Save the image with the hidden message
cv2.imwrite('image_with_hidden_message.png', image)

# To View the modified image
cv2.imshow("Modified Image", image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
