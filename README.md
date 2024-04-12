# StaticVideoGenerator

If you pause the video, you see nothing, but if you play the video you see something
Inspired by [this video](https://www.youtube.com/watch?v=TdTMeNXCnTs)
Floyd-Steinburg Transformation written by ChatGPT

## Result
<iframe width="952" height="536" src="https://www.youtube.com/embed/UJDuP1R9A4Y" title="Yea, Just Some Random Noise" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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

## Future Ideas

A better algrithm is **K mean clustering**
Maybe in the future ill add a **image function**, can **hide a static image behind moving noise**.
Another idea is use **ascii to do grayscale**, but tired....
## Requiste

pip install opencv-python
pip install moviepy
pip instal tqdm (a progress bar)