# smally
Video compression with math, yay!
While mainting quality, good enough for humans. Lossy Compression.

## Current best: 16% of original size.

Wanted to compress your files with your notebook and pencil? Now you can!

Using the Singular Value Decomposition and picking out the nicest eigenvectors, as shown by [Professor Gilbert Strang](http://www-math.mit.edu/~gs/) in his brilliant book "Introduction to linear algebra"
Still working on obtaining the eigenvector bases for every frame, seems unlikely though.

### What's working?
1. The image compression (b/w)
2. The video compression (b/w and color)
Video compression works without using a new format to store the tensors because mp4 automatically compresses empty space (most likely)

### ToDo
- [x] Use multiprocessing to process color videos
- [ ] Store in new format (Not required as of now as mp4 handles it automatically)
- [ ] More coarse grained parallelism so that overhead is reduced

## Actual usage
Install everything:
```
pip install -r requirements.txt
```
Run
```
python compress.py [i|v] [input filename] [output filename]
# i is for image, result stored at result.png
# v is for video, only mp4, result stored at 1999.mp4
```
