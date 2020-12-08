import os
import tokenizers
DEVICE = "cpu"
MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 16
EPOCHS = 10
BERT_PATH = "./bert-base-uncased"
MODEL_PATH = "./bert-base-uncased/pytorch_model.bin"
TRAINING_FILE = "./input/train.csv"
TOKENIZER = tokenizers.BertWordPieceTokenizer(
    os.path.join(BERT_PATH,"vocab.txt"),
    #lowercase=True
)