import os
import cv2
import pandas as pd


class preprocess:

    def __init__(self):
        self.dataset = pd.DataFrame()
        self.img_name_list=[]
    
    def load_data_img(self, rootpath):
        
        for i, filename in enumerate(os.listdir(os.path.join(rootpath, 'train/'))):

            img = cv2.imread(os.path.join(rootpath, f'train/{filename}'),cv2.IMREAD_GRAYSCALE)
            
            file_name_no_ext=filename.replace('.jpg','')
            self.img_name_list.append(file_name_no_ext)
            
            self.dataset.loc[file_name_no_ext,'img']=[img]
    
    def set_dataframe(self, rootpath):

        cases = os.listdir('Dataset\open-images-v7\\train\data')
        cases = [i.split('.')[0] for i in cases]
        classi = pd.read_csv('Dataset\open-images-v7\\train\labels\classifications.csv')
        class_map = pd.read_csv('Dataset\open-images-v7\\train\metadata\classes.csv', names=['Labelname', 'label'])
        df = classi[(classi.Confidence > 0) & classi.ImageID.isin(cases)].merge(class_map, how='left', left_on='LabelName', right_on='Labelname')
        self.dataset = df.groupby('ImageID').label.unique()

    def process_one(self):
        pass

    def process_two(self):
        pass

    def out_put(self, path):
        pass

if __name__ == "__main__":
    # Execute pipeline
    current_process = preprocess()
    current_process.set_dataframe("/")
    current_process.load_data_img("/")
    current_process.process_one()
    current_process.process_two()
    current_process.out_put("/")



    


