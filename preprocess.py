import json
from typing import List, Tuple
from torch.utils.data import DataLoader

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
        for sent in sents["data"]:
            temp = (sent["en"], sent["ko"])
            form.append(temp)
        return form

train_file = r'' # train_set.json file_path
valid_file = r'' # valid_set.json file_path

train_iter = create_parallel(train_file)
valid_iter = create_parallel(valid_file)
train_dataloader = DataLoader(train_iter, batch_size=64)
valid_dataloader = DataLoader(valid_iter, batch_size=64)
