import argparse
import math
import os
import tkinter as tk
from functools import partial
from pathlib import Path

parser = argparse.ArgumentParser("image-sorter")
parser.add_argument("width", help="Width of window", type=int)
parser.add_argument("height", help="Height of window", type=int)
args = parser.parse_args()


win = tk.Tk()
win.title("image-sorter")
win.geometry(f"{args.width}x{args.height}")
index = tk.IntVar()

max_image_width = int(0.8 * args.width)
max_image_height = int(0.8 * args.height)

p = Path("./")
folders = [f for f in p.iterdir() if f.is_dir()]
images = []
for content_filename in os.listdir("./"):
    # check if the image ends with png or jpg
    if content_filename.endswith(".png") or content_filename.endswith(".jpg"):
        images.append(content_filename)

index.set(0)

photo = tk.PhotoImage(file=images[index.get()])

print(f"photo width: {photo.width()} photo height: {photo.height()}")

if photo.width() > max_image_width or photo.height() > max_image_height:
    ratio = math.ceil(
        max(photo.width() / max_image_width, photo.height() / max_image_height)
    )
    photo = photo.subsample(ratio, ratio)

image = tk.Label(win, image=photo)
image.pack()


def move_image(folder, images):
    print(f"Moving {images[index.get()]} to {folder}")
    os.rename(images[index.get()], f"{folder}/{images[index.get()]}")
    index.set(index.get() + 1)
    photo = tk.PhotoImage(file=images[index.get()])
    if photo.width() > max_image_width or photo.height() > max_image_height:
        ratio = math.ceil(
            max(photo.width() / max_image_width, photo.height() / max_image_height)
        )
        photo = photo.subsample(ratio, ratio)
    image.configure(image=photo)
    image.image = photo


def main():
    buttons = []
    for folder in folders:
        button = tk.Button(
            win,
            text=f"Click to move image to {folder}",
            command=partial(move_image, folder, images),
        )
        button.pack()
        buttons.append(button)

    win.mainloop()
