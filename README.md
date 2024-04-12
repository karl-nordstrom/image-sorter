Hacky minimal python script for sorting images into folders with a GUI. Only works for `.png`, `.gif`, `.ppm`, `.pgm` formats. Usage:

```
pip install .
cd folder/with/images
image-sorter --width $WIDTH --height $HEIGHT
```

(You need to pass in the pixel width and height of the GUI window as integers.)

This will open a window displaying one image in the current directory at a time, and buttons for each of the folders in the directory. Pressing a button will move the image to that folder.
