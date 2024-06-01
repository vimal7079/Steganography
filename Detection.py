import cv2

# Read the image
image = cv2.imread("new_image.png")

# Display the image
cv2.imshow('vimal', image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

height, width, channels = image.shape

hidden_msg = ''
binary_msg = ''

for row in range(height):
    flag = False
    for col in range(width):
        for channel in range(channels):
            binary_msg += bin(image[row][col][channel])[-2:]
            if len(binary_msg) == 8:
                temp = chr(int(binary_msg, 2))
                hidden_msg += temp
                binary_msg = ''
                if '**' in hidden_msg:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

print("Hidden Message:", hidden_msg[:-2])
