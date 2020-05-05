from PIL import Image
import numpy as np
from scipy import linalg as LA
import cv2
import imageio

BEST_PERCENT = 0.2


def pixelate_image(image, percent):
    A = image
    m, n = A.shape
    U, S, V_t = LA.svd(A)
    best = np.array(sorted(enumerate(S), key=lambda x: x[1], reverse=True))
    x = list(best.shape)[0]
    reduced = int(x*percent)
    best = best[reduced:]
    sigma = np.zeros((m, n))
    sigma[:m, :m] = np.diag(S)
    for index, _ in best:
        index = int(index)
        sigma[index, index] = 0

    return U.dot(sigma.dot(V_t))  


"""
Initial testing with one image, works well in pixelating the images, 
TODO: need to work on saving only the necessary information
"""
# data = Image.open('plane.jpg').convert('L')
# print(type(data))
# data = np.matrix(data)

# result = pixelate_image(data, BEST_PERCENT)
# saver = Image.fromarray(result)
# saver = saver.convert("L")
# saver.save('result.png')

video_file_name = input("What's the name of the video you want to compress")

# Get specifics of video
cap_read = cv2.VideoCapture(video_file_name)
if cap_read.isOpened():
    height = int(cap_read.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap_read.get(cv2.CAP_PROP_FRAME_WIDTH))
    count = cap_read.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap_read.get(cv2.CAP_PROP_FPS)
print(f"height: {height}, width: {width}, count: {count}, fps: {fps}")
# codec = cv2.VideoWriter_fourcc(*'mp4v')
# cap_write = cv2.VideoWriter('1980.mp4', codec, fps, (int(cap_read.get(3)), int(cap_read.get(4))))
writer = imageio.get_writer('1999.mp4', fps=fps)
frame_count = 0
ret_bool = True
while cap_read.isOpened() and ret_bool:
    ret_bool, frame = cap_read.read()
    if ret_bool:
        frame_count += 1
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fixed_frame = pixelate_image(gray_frame, BEST_PERCENT).astype(np.uint8)
        writer.append_data(fixed_frame)
        print("Wrote frame", frame_count)
cap_read.release()
writer.close()
# cap_write.release()
cv2.destroyAllWindows()

print("The ouput file is 1999.mp4")
