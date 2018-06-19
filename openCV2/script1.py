#
#   Opening all images from a directory
#

import cv2
# import os
import glob

## Method 1

# path = './sample-images'
# files = os.listdir(path)
#
# for name in files:
#     img = cv2.imread(path + "/" + name, 0)
#     # print(name)
#     resized_image = cv2.resize(img, (100, 100))
#     cv2.imshow(name, resized_image)
#    cv2.waitKey(1000)       # in miliseconds
#    cv2.destroyAllWindows()


## Method 2

images=glob.glob("./sample-images/*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
