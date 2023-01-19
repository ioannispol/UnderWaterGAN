#!/usr/bin/bash

nvidia-smi


echo "The Python version is: $(python --version)"


# view the training results
#python -m visdom.server

# Train the model
python train.py --gpu_ids 1 \
    --n_epochs 50 \
    --n_epochs_decay 50 \
    --save_epoch_freq 20 \
    --batch_size 4 \
    --dataroot ./underwater_data \
    --name gan_train_100ep_cracks_new



