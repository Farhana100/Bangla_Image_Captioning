from googletrans import Translator as tr
import json
from tqdm import tqdm
from pathlib import Path
import argparse


def refine_json(filepath):
    filepath = Path(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
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
    refined_filepath = f'{filepath.stem}_refined.json'
    refined_filepath = f'{filepath.parent}/{filepath.stem}_refined.json'
    with open(refined_filepath, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=4)

    return refined_filepath


def get_records(refined_path):
    refined_path = Path(refined_path)

    data_ref = None
    with open(refined_path, 'r', encoding='utf-8') as f:
        data_ref = json.load(f)

    return data_ref


def translate(text, src='en', dest='bn'):
    translator = tr()
    result = translator.translate(text, src=src, dest=dest)

    result = [r.text for r in result]
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--refine', dest='refine',
                        default=False, action='store_true')
    parser.add_argument('--translate', dest='translate',
                        default=False, action='store_true')
    parser.add_argument('--path', dest='path', type=str,
                        help='input json path')
    parser.add_argument('--save_path', dest='save_path',
                        default='.', type=str, help='output json path')

    args = parser.parse_args()
    # args =  parser.parse_args(args=['--refine', '--translate', '--path', '/content/annotations/captions_val2017.json'])

    if args.refine:
        print('refining...')
        raw_path = args.path
        refined_path = refine_json(filepath=raw_path)
        print('done')

    if args.translate:
        if args.refine:
            # given path was raw
            refined_path = refined_path
        else:
            # given path was refined
            refined_path = args.path

        records = get_records(refined_path=refined_path)
        translated_records = records.copy()

        print('translating...')
        for id in tqdm(translated_records):
            caps = translated_records[id]['captions']
            new_caps = translate(caps)
            translated_records[id]['captions'] = new_caps
        print('done')

        if args.save_path is None or args.save_path == "." or args.save_path == "" or args.save_path == " ":
            save_path = f'{Path(refined_path).parent}/{Path(refined_path).stem}_translated.json'
        else:
            save_path = args.save_path

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(translated_records, f, indent=4)
