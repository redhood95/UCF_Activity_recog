import sys
import warnings
import time
import os.path
import numpy as np
warnings.filterwarnings("ignore")
from sklearn.preprocessing import OneHotEncoder
from keras.utils import to_categorical
from dataset.UCF50 import UCF50

class Load:
    def load(self):
        if os.path.isfile('arrays_dump/train_x.npy'):
            print ("File exist")
            train_x= np.load("arrays_dump/train_x.npy")
            train_y=np.load("arrays_dump/train_y.npy")
            eval_x=np.load("arrays_dump/eval_x.npy")
            eval_y=np.load("arrays_dump/eval_y.npy")
            test_x=np.load("arrays_dump/test_x.npy")
            test_y=np.load("arrays_dump/test_y.npy")

        else:
            print ("File not exist")
            activity = UCF50()

            train_x , train_y,eval_x , eval_y, test_x  , test_y = activity.load_data('data/UCF50/full_extractedresize_bw')

            np.save("arrays_dump/train_x.npy",train_x)
            np.save("arrays_dump/train_y.npy",train_y)
            np.save("arrays_dump/eval_x.npy",eval_x)
            np.save("arrays_dump/eval_y.npy",eval_y)
            np.save("arrays_dump/test_x.npy",test_x)
            np.save("arrays_dump/test_y.npy",test_y)
            print('arrays saved')

        train_y = to_categorical(train_y)
        eval_y = to_categorical(eval_y)

        return train_x , train_y,eval_x , eval_y, test_x  , test_y