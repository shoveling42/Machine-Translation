import tarfile

train = tarfile.open(r'.\example_training.tar.gz')
train.extractall()
train.close()

valid = tarfile.open(r'.\example_validation.tar.gz')
valid.extractall()
valid.close