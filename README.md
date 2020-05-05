# smally
Video compression with math, yay!
While mainting quality, good enough for humans. Lossy Compression.

## Current best: 47% of original size.

Wanted to compress your files with your notebook and pencil? Now you can!

Using the Singular Value Decomposition and picking out the nicest eigenvectors, as shown by [Professor Gilbert Strang](http://www-math.mit.edu/~gs/) in his book "introduction to linear algebra", thank you for everything!  
Still working on obtaining the eigenvector bases for every frame, seems unlikely though.

### What's working?
1. The image compression
2. The video compression
... That's it? Haha no
As of now the output files also contain the redundant information which is meant to be discarded.
Although, the mp4 format somehow already does this when it receives the processed frames.

### What's left?
1. Actual compression, maybe with a new format. Need a fancy new decoder too. Can save network bandwidth 10/10.  
2. Parallelize? A lot of the operations can be parallelized, maybe with CPU threads, maybe with a GPU.  
3. Clean up the use of external libraries, try to maximise each one's functionality.

## Actual usage
Install everything:
```
pip install -r requirements.txt
```
Run
```
python rawed.py
```
Do as the script commands. ;)
