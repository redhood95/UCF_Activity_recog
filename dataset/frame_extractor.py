import os 
import cv2 

path = "../data/UCF50/UCF50"

extracted = '../data/UCF50/extracted'


list1 =  os.listdir(path)

os.mkdir(extracted)
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
                cv2.imwrite(image_path+".png",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        print("number of frames extracted :"+str(count))
        cap.release()
