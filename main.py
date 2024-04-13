from PIL import Image,ImageEnhance,ImageDraw
import tkinter as tk
from tkinter import filedialog
import moviepy.editor
import os,random
from tqdm import tqdm
import imageio
import numpy as np
from skimage import measure
from tkinter import messagebox



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
def custom_grayscale(img):
    fil=ImageEnhance.Contrast(img)
    img = fil.enhance(5).convert('1')
    # img=fil.enhance(10)
    return img

def POV(img,prev,BFlip=True):# black then flip
    # Get the dimensions of the image
    width, height = img.size

    pix=img.load()
    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            new_pixel = 255 if pix[x,y] > THRESHOLD else 0
            prev_pix=prev.getpixel((x,y))
            if((new_pixel==255)==BFlip):# white change
                pix[x,y]= 0 if prev_pix ==255 else 255
            else:
                pix[x,y]=prev_pix

    return img.convert("L")


def boundary(image,stage=3):
    # Convert PIL Image to numpy array
    image_array = np.array(image.convert("L"))

    # Create a new blank image with the same size as the input image
    boundary_image = Image.new("L", image.size, color=255)
    draw = ImageDraw.Draw(boundary_image)
    for i in range(int(255/stage),255,int(255/stage)):
        contours =measure.find_contours(image_array,level=i)
        for contour in contours:
            contour = np.array(contour, dtype=np.int32)
            contour = [tuple(l[::-1]) for l in contour.tolist()]
            draw.line(contour,width=1)
            draw.polygon(contour, fill="black") if(i==int(255/stage)) else 0
    

    return boundary_image


# selectb input file

file_path = filedialog.askopenfilename()
folder_name = os.path.dirname(file_path)

MODE="B"
def func(s):
    MODE=s
    root.destroy()
root=tk.Tk()
tk.Button(root,text="Boundary",command=lambda:func("B")).pack()
tk.Button(root,text="Grayscale",command=lambda:func("G")).pack()
root.mainloop()


VidFile = moviepy.editor.VideoFileClip(file_path)
Vid=[]
fps=VidFile.fps
w,h=VidFile.size
THRESHOLD=128
for frame in tqdm(VidFile.iter_frames(),desc="Loading video"):
    Vid.append(Image.fromarray(frame))

VidFile.close()
print("done loading")

Vid.insert(0,generate_noise(w,h))
for i in tqdm(range(1,len(Vid)),desc="Processing"):
    if(MODE=='G'):
        Vid[i]=POV(custom_grayscale(Vid[i]),Vid[i-1],BFlip=True)
    else:
        Vid[i]=POV(boundary(Vid[i],stage=4),Vid[i-1],BFlip=False)

with imageio.get_writer(os.path.join(folder_name,'RickBoundary_.mp4'), fps=fps) as video:
    for i in tqdm(range(len(Vid)),desc="exporting"):
        video.append_data(np.array(Vid[i]))
