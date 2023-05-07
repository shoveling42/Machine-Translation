import json

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
        raw_file = r'.\json2txt\raw_data\korean_{}_{}.en'.format(type, num)
        with open(raw_file, 'w', encoding='utf-8') as f:
            for sent in sents["data"]:
                f.write(sent["ko"] + '\n')

train = 'train'
valid = 'valid'

def main():
    file_path = r'' # input file path
    '''
    type: train, valid
    num: index of dataset
    '''
    extract_en(file_path, type=valid, num=3)
    extract_ko(file_path, type=valid, num=3)
    return 0

if __name__ == "__main__":
    main()