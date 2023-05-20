#Certainly! Here's an example of Python code for an Image Processing Tool using the OpenCV library:

```python
import cv2

def apply_filter(image, filter_type):
    if filter_type == 'blur':
        return cv2.blur(image, (5, 5))
    elif filter_type == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)
    elif filter_type == 'edge_detection':
        return cv2.Canny(image, 100, 200)
    else:
        raise ValueError('Invalid filter type.')

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (cols, rows))

def crop_image(image, x, y, width, height):
    return image[y:y+height, x:x+width]

def adjust_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    updated_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(updated_hsv, cv2.COLOR_HSV2BGR)

def convert_image(image, output_path, format):
    cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, 90])

# Example usage
input_path = 'input.jpg'
output_path = 'output.jpg'

# Read input image
image = cv2.imread(input_path)

# Apply filters
filtered_image = apply_filter(image, 'blur')

# Resize image
resized_image = resize_image(image, 800, 600)

# Rotate image
rotated_image = rotate_image(image, 90)

# Crop image
cropped_image = crop_image(image, 100, 100, 300, 200)

# Adjust brightness
brightened_image = adjust_brightness(image, 50)

# Convert image format
convert_image(image, output_path, 'JPEG')
```

#This code demonstrates some common image processing operations such as applying filters, resizing, rotating, cropping, adjusting brightness, and converting image formats. Feel free to customize and enhance the code according to your specific requirements and additional functionalities.
