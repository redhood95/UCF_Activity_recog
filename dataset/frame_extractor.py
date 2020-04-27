import os 
import cv2 

path = "../data/UCF50/UCF50"

extracted = '../data/UCF50/'

list1 =  os.listdir(path)

for i in list1:
    list2 = os.listdir(os.path.join(path,i))
    for seq in range(0,len(list2)):
        path_to_vid = os.path.join(os.path.join(path,i),list2[seq])
        cap = cv2.VideoCapture(path_to_vid)
