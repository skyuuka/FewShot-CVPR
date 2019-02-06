import json
import shutil
import os

image_dir = '/nfs_1/data/ImageNet'


with open('split.json') as f:
    split_data = json.load(f)


def copy_image(item):
    type_ = item['type']
    path_ = item['path']
    name_ = item['name']
    if type_ == 'file':
        split_, class_, name_ = path_.split('/')[-3:]
        train_split_ = split_ 
        src_file = os.path.join(image_dir, 'train', class_, name_)
        tar_file = os.path.join(split_, class_, name_)
        dirname = os.path.dirname(tar_file)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        if not os.path.exists(tar_file):
            print (src_file, '->', tar_file)
            shutil.copyfile(src_file, tar_file)
    else:
        for item_ in item['children']:
            copy_image(item_)

if __name__ == '__main__':
    copy_image(split_data)
