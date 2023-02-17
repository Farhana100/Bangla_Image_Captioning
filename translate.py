from googletrans import Translator as tr
import json
from tqdm import tqdm

def import_json(train=True):

    file_name = 'captions_train' if train else 'captions_val'

    with open(file_name + '2017.json', 'r', encoding='utf-8') as f:
        data_raw = json.load(f)


    images = data_raw['images']
    annotations = data_raw['annotations']


    records = dict()
    for img in images:
        record = dict()

        record['id'] = img['id']
        record['file_name'] = img['file_name']
        record['captions'] = list()

        records[img['id']] = record

    
    for ann in annotations:
        records[ann['image_id']]['captions'].append(ann['caption'])


    # json dump records
    with open(file_name + '_refined.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=4)

    return records



def translate(text, src='en', dest='bn'):
    translator = tr()
    result = translator.translate(text, src=src, dest=dest)

    result = [r.text for r in result]
    return result


if __name__ == '__main__':

    train = False


    records = import_json(train=train)

    img_ids = list(records.keys())
    print(records[img_ids[0]])    

    
    translated_records = records.copy()

    # with tqdm 
    for id in tqdm(translated_records):
    # for id in translated_records:
        caps = translated_records[id]['captions']
        new_caps = translate(caps)

        translated_records[id]['captions'] = new_caps


    file_name = 'captions_train' if train else 'captions_val'

    # json dump records
    with open(file_name + '_translated.json', 'w', encoding='utf-8') as f:
        json.dump(translated_records, f, indent=4)    


