import os
import cv2
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

class preprocess:

    def __init__(self):
        self.dataset = pd.DataFrame()
        self.img_name_list=[]
    
    def load_data_img(self, rootpath):
        logging.info(f'Loading Images from {rootpath} started...')
        for i, filename in enumerate(os.listdir(os.path.join(rootpath, 'data'))):

            img = cv2.imread(os.path.join(rootpath, f'data\{filename}'),cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (600,600))
            file_name_no_ext=filename.replace('.jpg','')
            self.img_name_list.append(file_name_no_ext)
            self.dataset.loc[file_name_no_ext,'img']=[img]

        logging.info(f'{len(self.img_name_list)} Images loaded')
    
    def set_dataframe(self, rootpath):
        logging.info('Loading labels started...')
        cases = os.listdir(rootpath + '\data')
        cases = [i.split('.')[0] for i in cases]
        classi = pd.read_csv(rootpath + '\labels\classifications.csv')
        class_map = pd.read_csv(rootpath + '\metadata\classes.csv', names=['Labelname', 'label'])
        df = classi[(classi.Confidence > 0) & classi.ImageID.isin(cases)].merge(class_map, how='left', left_on='LabelName', right_on='Labelname')
        ref = ['Hot dog', 'Dog', 'Taco']
        self.dataset = df.groupby('ImageID', as_index=False).label.apply(lambda x: ' '.join([i for i in ref if i in list(x)]))
        self.dataset['img'] = [None] * len(self.dataset.index)
        self.dataset = self.dataset.set_index('ImageID')
        logging.info("Dataset labels finished")

    def process_one(self):
        logging.info('Preprocess one started...')
        self.dataset['img'] = self.dataset.img.apply(lambda x: x[0]/255)
        #.apply(lambda x: 'no' if x is None else print(x[0].shape))
        logging.info("Preprocess one finish")

    def augmentation_process(self):
        logging.info("Data Augmentation started...")
        second_df = pd.DataFrame()
        
        for id, (label, img) in enumerate(self.dataset.iterrows()):
            flip_img = np.flipud(img)
            pd.concat([second_df,{'ImagedID': str(id)+'r',
                                 'label': label,
                                 'img': flip_img}])
            
            turn_img = np.fliplr(img)
            pd.concat([second_df,{'ImagedID':str(id)+'fr',
                                 'label': label,
                                 'img': turn_img}])
        
        second_df.set_index('ImageID', inplace=True)

        self.dataset = pd.concat([self.dataset, second_df])
        logging.info("Data Augmentation finished")
            

    def out_put(self, path):
        #print(self.dataset.label.value_counts())
        self.dataset.to_csv('test.csv')
        logging.info(f'Data output in: {path}test.csv')

if __name__ == "__main__":
    # Execute pipeline
    path = "Dataset\open-images-v7\\train"
    current_process = preprocess()
    current_process.set_dataframe(path)
    current_process.load_data_img(path)
    current_process.process_one()
    current_process.augmentation_process()
    current_process.out_put("/")
