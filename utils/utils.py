import argparse, os, torch
from torch.utils.tensorboard import SummaryWriter
import torch.optim as optim
import numpy as np

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def set_loggers(conf):
    # experiment setting values
    setting = "epoch"+str(conf['epoch'])+"_lr"+str(conf['lr'])
    if conf['pretrain']:
        # make pretrained model
        checkpt = f"./model/weight/pretrain/{conf['model']}/{conf['dataset']}_{setting}.pt"
        board_name = str(conf['model'])+"/"+str(conf['dataset'])+"_"+setting
        writer = SummaryWriter("./results/log/pretrain/"+board_name)
        
        print('model:', conf['model'], ' dataset:', conf['dataset'], 'pretrain: ', conf['pretrain'])
    else:
        # save name setting for fine-tuning model
        checkpt = f"./model/weight/{conf['mode']}/{conf['model']}/{conf['dataset']}_{setting}.pt"
        board_name = f"{conf['mode']}/{conf['model']}/{conf['dataset']}_{setting}"
        writer = SummaryWriter(f"./results/log/{board_name}")
        os.makedirs(f"./model/weight/{conf['mode']}/{conf['model']}", exist_ok=True)
        
        print('model:', conf['model'], ' dataset:', conf['dataset'], 'fine-tuning mode:', conf['mode'])
        
    return checkpt, board_name, writer, setting

