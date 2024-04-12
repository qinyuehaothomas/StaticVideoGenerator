from PIL import Image,ImageEnhance
import tkinter as tk
from tkinter import filedialog
import moviepy.editor
import os,random
from tqdm import tqdm
import imageio
import numpy as np
def generate_noise(width, height):
    # Create a new black image
    noise_image = Image.new('L', (width, height))

    # Access the pixel data of the image
    pixels = noise_image.load()
    for x in range(width):
        for y in range(height):
            pixels[x,y]=random.choice([0,255])
    return noise_image
"""
def floyd_steinberg_dithering(img,prev): # CHATGPT!!!!!!!

    img = img.convert('L')

    # Get the dimensions of the image
    width, height = img.size

    pix=img.load()
    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            old_pixel = pix[x,y]
            new_pixel = 255 if old_pixel > 128 else 0
            # img.putpixel((x, y), new_pixel)
            # pix[x,y]=new_pixel

            # Calculate error
            error = old_pixel - new_pixel

            # Diffuse error to neighboring pixels
            if x < width - 1:
                pix[x+1,y]+=error * 7 // 16
                # img.putpixel((x + 1, y), )
            if x > 0 and y < height - 1:
                pix[x-1,y+1]+=error * 3 // 16
            if y < height - 1:
                pix[x,y+1]+=error * 5 // 16
            if x < width - 1 and y < height - 1:
                pix[x+1,y+1]+=error * 1 // 16
            
            prev_pix=prev.getpixel((x,y))
            if(new_pixel==0):# white change
                pix[x,y]= 0 if prev_pix ==255 else 255
            else:
                pix[x,y]=prev_pix


    return img
"""
def grayscale(img,prev):
    fil=ImageEnhance.Contrast(img)
    img = fil.enhance(5).convert('1')
    # img=fil.enhance(10)


    # Get the dimensions of the image
    width, height = img.size

    pix=img.load()
    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            new_pixel = 255 if pix[x,y] > THRESHOLD else 0
            prev_pix=prev.getpixel((x,y))
            if(new_pixel==255):# white change
                pix[x,y]= 0 if prev_pix ==255 else 255
            else:
                pix[x,y]=prev_pix

    return img.convert("L")



# selectb input file

file_path =r"D:\Projects\StaticVideoGenerator\StaticVideoGenerator\byebye.mp4"
folder_name = os.path.dirname(file_path)

# file_path = filedialog.askopenfilename()
# folder_name = os.path.dirname(file_path)
# print("Selected file:", file_path)
# print("Folder:", folder_name)


VidFile = moviepy.editor.VideoFileClip(file_path)
Vid=[]
fps=VidFile.fps
w,h=VidFile.size
THRESHOLD=128
for frame in tqdm(VidFile.iter_frames(),desc="Loading video"):
    Vid.append(Image.fromarray(frame))

# ImageEnhance.Contrast(Vid[10]).enhance(10).show()


# Close the video clip
VidFile.close()
print("done loading")

Vid.insert(0,generate_noise(w,h))
for i in tqdm(range(1,len(Vid)),desc="Processing"):
    # Vid[i]=floyd_steinberg_dithering(Vid[i],Vid[i-1])
    Vid[i]=grayscale(Vid[i],Vid[i-1])

with imageio.get_writer(os.path.join(folder_name,'TrumpMew.mp4'), fps=fps) as video:
    for i in tqdm(range(len(Vid)),desc="exporting"):
        video.append_data(np.array(Vid[i]))
