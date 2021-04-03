import os
from sklearn.model_selection import train_test_split


def create_markup(path_data='mozilla-1', path_markup='filelists'):
    with open(os.path.join(path_data, 'metadata.csv'), 'r', encoding='utf-8') as f:
        data = f.read().split('\n')[:-1]

    data = [f'{path_data}/wavs/{sample}' for sample in data]
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    test, valid = train_test_split(test, test_size=0.3, random_state=42)

    with open(os.path.join(path_markup, 'ljs_audio_text_train_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in train]

    with open(os.path.join(path_markup, 'ljs_audio_text_test_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in test]

    with open(os.path.join(path_markup, 'ljs_audio_text_val_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in valid]

    data = [f'{path_data}/wavs/{sample.replace(".wav", ".pt")}' for sample in data]
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    test, valid = train_test_split(test, test_size=0.3, random_state=42)

    with open(os.path.join(path_markup, 'ljs_mel_text_train_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in train]

    with open(os.path.join(path_markup, 'ljs_mel_text_test_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in test]

    with open(os.path.join(path_markup, 'ljs_mel_text_val_filelist.txt'), 'w', encoding='utf-8') as f:
        [f.write(sample + '\n') for sample in valid]


if __name__ == '__main__':
    create_markup()