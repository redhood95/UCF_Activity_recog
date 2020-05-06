

import os 
import cv2 

path = "../data/UCF50/UCF50"

extracted = '../data/UCF50/full_extractedresize_bw'


list1 =  os.listdir(path)

os.mkdir(extracted)
c = 0
for i in list1:
    os.mkdir(os.path.join(extracted,i))
    list2 = os.listdir(os.path.join(path,i))
    for seq in range(0,len(list2)):

        os.mkdir(os.path.join(os.path.join(extracted,i),str(seq)))
        path_to_vid = os.path.join(os.path.join(path,i),list2[seq])
        cap = cv2.VideoCapture(path_to_vid)
        count = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            
            if ret == True:
                count = count + 1
                image_path = os.path.join(os.path.join(os.path.join(extracted,i),str(seq)),str(count))
                frame = cv2.resize(frame,(60,80))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(image_path+".png",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        # print("number of frames extracted :"+str(count))
        cap.release()
    c = c + 1 
    print(c)