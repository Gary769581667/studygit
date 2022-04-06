import os
import random



Train_rate = 0.8
folder = 'MMA'
motions = ['boxing','jump','jack','squats','walk']
trainset = []
testset = []
for motion in motions:
    path = os.path.join(folder,motion)
    
    files = os.listdir(path)
    random.shuffle(files)
    
    train_num = int(len(files)*Train_rate)
    trainset.append(files[0:train_num])
    testset.append(files[train_num-1:-1])
with open('MMA\\MMA_names.txt','w') as f:
    for motion in motions:
        f.write(motion)
        f.write('\n')

with open('MMA\\MMA_train.txt','w') as f:
    for motions in trainset:
        for motion in motions:
            f.write(motion)
            f.write('\n')

with open('MMA\\MMA_test.txt','w') as f:
    for motions in testset:
        for motion in motions:
            f.write(motion)
            f.write('\n')
    