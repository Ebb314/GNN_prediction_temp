import argparse

import torch
import yaml










def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def main(args):

    model_config = load_config(args.model_config_path)
    train_config = load_config(args.train_config_path)

    torch.manual_seed(train_config['seed'])
    torch.cuda.manual_seed(train_config['seed'])

    # ------------ Load data -------------------

    # get dataset config
    data_config = model_config['dataset']
    device = torch.device(data_config['device'])

    # method of data standardize
    # ......

    



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_config_path', type=str, default='./config/train_config.yaml')
    parser.add_argument('--model_config_path', type=str, default='./config/model_config.yaml')
    parser.add_argument('--model_name', type=str, default='GNN')
    parser.add_argument('--model_save_path', type=str, default='./results/GNN_prediction_temp.pkl')

    args = parser.parse_args()

    main(args)

    # else...

