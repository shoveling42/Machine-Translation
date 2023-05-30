import json
from typing import List, Tuple
import torch
from torch.utils.data import DataLoader, random_split


# extract_en, extract_ko functions are deprecated
def extract_en(file_path: str, type: str, num: int):
    with open(file_path, 'r', encoding='utf-8') as file:
        sents = json.load(file)
        raw_file = r'.\json2txt\raw_data\english_{}_{}.en'.format(type, num)
        with open(raw_file, 'w', encoding='utf-8') as f:
            for sent in sents["data"]:
                f.write(sent["en"] + '\n')
    
def extract_ko(file_path: str, type: str, num: int):
    with open(file_path, 'r', encoding='utf-8') as file:
        sents = json.load(file)
        raw_file = r'.\json2txt\raw_data\korean_{}_{}.ko'.format(type, num)
        with open(raw_file, 'w', encoding='utf-8') as f:
            for sent in sents["data"]:
                f.write(sent["ko"] + '\n')

def create_parallel(file_path: str) -> List[Tuple]:
    form = list()
    with open(file_path, 'r', encoding='utf-8') as file:
        sents = json.load(file)
        for sent in sents:
            temp = (sent["D"], sent["C"])
            form.append(temp)
        return form

train_file = r'.\json2txt\dataset\kss_train.json'
valid_file = r'.\json2txt\dataset\kss_dev.json'
test_file = r'.\json2txt\dataset\kss_test.json'

train_iter = create_parallel(train_file)
valid_iter = create_parallel(valid_file)
test_iter = create_parallel(test_file)

train_iter = DataLoader(train_iter, batch_size=64)
valid_iter = DataLoader(valid_iter, batch_size=64)