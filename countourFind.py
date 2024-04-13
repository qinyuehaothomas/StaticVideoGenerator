# test scripts

from PIL import Image, ImageDraw
from skimage import measure
import numpy as np

def find_and_draw_boundary(image):
    # Convert PIL Image to numpy array
    image_array = np.array(image.convert("L"))
    # print(image_array)
    # Find contours
    contours = measure.find_contours(image_array,level=150)
    print(contours)

    # Create a new blank image with the same size as the input image
    boundary_image = Image.new("L", image.size, color=255)
    draw = ImageDraw.Draw(boundary_image)

    # Draw contours on the blank image with black color
    
    for contour in contours:
        contour = np.array(contour, dtype=np.int32)
        contour = [tuple(l[::-1]) for l in contour.tolist()]
        draw.line(contour,width=1)

    return boundary_image

# Example usage
input_image = Image.open(r"D:\Projects\StaticVideoGenerator\StaticVideoGenerator\byebye.jpg")
boundary_image = find_and_draw_boundary(input_image)
boundary_image.show()
