'''
Created on 8 jul. 2017

@author: yasushishibe
'''
import numpy as np
import glob
from scipy import misc
import pandas as pd
import os


path_dir = '/Volumes/RODRIGO/baidu_competition/train_data_photos/'
def main():
    data_list = pd.read_table(path_dir+'data_train_image.txt', 
                              delimiter= ' ', 
                              names=['ID', 'label', 'URL'])
    
    types = (path_dir+'train/'+'*.jpg',)
    dogphotos = []
    for files in types:
        dogphotos.extend(glob.glob(files))
        
    for p,i in enumerate(dogphotos):
        ID_pos = np.where(data_list[data_list.columns[0]]==i[len(path_dir+'train/'):-4])[0][0]
        label_num = data_list[data_list.columns[1]][ID_pos]
        
        image_path = path_dir+'image/'+str(label_num)
        
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        
        image = misc.imread(i)
        misc.imsave(image_path+os.sep+i[len(path_dir+'train/'):-4]+'.jpg', image)
        if p%5==0:
            print '%d of %d' %(p, len(dogphotos)) 
    
    print 'finish'
    
if __name__=="__main__":
    main()