import pandas as pd
import collections
import matplotlib.pyplot as plt

if __name__ == "__main__":
    train = pd.read_csv('mitbih_train.csv', header=None)
    test = pd.read_csv('mitbih_test.csv',header=None)

    for i in range(len(train)): 
        plt.figure(figsize=(2,2))
        plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False,length=0)
        plt.plot(train.loc[i,:186])
        train_path = 'train_images/'+str(i)+'.png'
        plt.savefig(train_path)
        print('train: '+str(i))
        plt.close()
    
    for i in range(len(test)):
        plt.figure(figsize=(2,2))
        plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False,length=0)
        plt.plot(test.loc[i,:186])
        test_path = 'test_images/'+str(i)+'.png'
        plt.savefig(test_path)
        print('test: '+str(i))
        plt.close()