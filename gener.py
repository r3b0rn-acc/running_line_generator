import numpy as np
from moviepy.editor import ImageSequenceClip
from PIL import Image, ImageDraw, ImageFont


class Colour:
    def __init__(self, colour):
        colour_text_to_typle = {'black': (0, 0, 0),
                               'white': (255, 255, 255),
                               'red': (255, 0, 0),
                               'green': (0, 255, 0),
                               'blue': (0, 0, 255)}
        if isinstance(colour, tuple):
            self.colour = colour
        elif isinstance(colour, str):
            self.colour = colour_text_to_typle.get(colour, (0, 0, 0))
        else:
            raise ValueError


def generate(text, text_colour='black', background_colour='white'):
    text_colour = Colour(text_colour).colour
    background_colour = Colour(background_colour).colour

    array = np.array([[background_colour for _ in range(100)] for _ in range(100)])
    seconds = 3
    fps = 24
    frames_num = fps * seconds

    font = ImageFont.truetype("arial.ttf", 100)
    text_size = ImageDraw.Draw(Image.fromarray(array.astype(np.uint8))).textsize(text, font=font)
    delta = text_size[0] // frames_num

    video = []
    for frame in range(frames_num):
        image = Image.fromarray(array.astype(np.uint8))
        drawer = ImageDraw.Draw(image)
        drawer.text((-1*frame*delta, 0), text, font=font, fill=text_colour)
        video.append(image)


    clip = ImageSequenceClip([np.array(frame) for frame in video], fps=fps)
    clip.write_videofile('video.mp4')
    clip.preview(fps=fps)


generate('hello world!')
