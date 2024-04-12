# StaticVideoGenerator

If you pause the video, you see nothing, but if you play the video you see something
Inspired by [this video](https://www.youtube.com/watch?v=TdTMeNXCnTs)
Floyd-Steinburg Transformation written by ChatGPT

## How?

It use **persistence of vision (POV)** effect (I guess)

1. Original(last frame) is just random static(black and white)
1. turn image you want to display to black and white
This is the "mask"
1. flip the color of Orginal pixel for black pixel in mask,keep for white in mask

## How to Use

1. run code, select video you want to convert, wait, done
1. output will be saved in same folder as input.

## Process
At first i though of Flyod-Steinburg Dithering , but result was poor
Then i simply turn super high contrast , it was better
I want this type of detailed, but dunno the algrithm
![Stalin](https://i.pinimg.com/564x/be/16/b3/be16b32d9b18b01aca0ffe0bf2fcc84a.jpg)

## Requiste

pip install opencv-python
pip install moviepy
pip instal tqdm (a progress bar)