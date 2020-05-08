
## loading data 

import os 


dir = 'data/UCF50/full_extractedresize_bw'

categories = os.listdir(dir)
cat_count = 0
mapping = {}
for category in list1:
    mapping.add(cat_count,category)
    video_seqs = os.listdir(os.path.join(dir,category))
    for seq in video_seqs:
        images =  os.listdir(os.path.join(os.path.join(dir,category),seq))
        for img in images:
            img_name = os.path.join(os.path.join(dir,category),seq) + '/'+img
            