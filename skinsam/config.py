from box import Box

config = {
    "num_devices": 2,
    "batch_size": 4,
    "num_workers": 4,
    "num_epochs": 20,
    "eval_interval": 2,
    "out_dir": "out/training",
    "opt": {
        "learning_rate": 8e-4,
        "weight_decay": 1e-4,
        "decay_factor": 10,
        "steps": [60000, 86666],
        "warmup_steps": 250,
    },
    "model": {
        "type": 'vit_h',
        "checkpoint": "sam_vit_h_4b8939.pth",
        "freeze": {
            "image_encoder": True,
            "prompt_encoder": True,
            "mask_decoder": False,
        },
    },
    "dataset": {
        "train": {
            "root_dir": "../custom_data/train",
            "annotation_file": "../custom_data/train/annotations.json"
        },
        "val": {
            "root_dir": "../custom_data/val",
            "annotation_file": "../custom_data/val/annotations.json"
        }
    }
}

cfg = Box(config)