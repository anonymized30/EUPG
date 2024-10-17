import torch
from torch.utils.data import Dataset
from PIL import Image
import os

# Custom dataset for loading DP-obfuscated CIFAR-10 images
class DPCIFAR10Dataset(Dataset):
    def __init__(self, root_dir, labels, transform=None):
        """
        Args:
            root_dir (string): Directory with all the obfuscated images.
            transform (callable, optional): Optional transform to be applied
                                            on a sample (default is None).
        """
        self.root_dir = root_dir
        self.labels = labels
        self.transform = transform
        # Sort files numerically by extracting the integer part from the filenames
        self.image_files = sorted(
            [f for f in os.listdir(root_dir) if f.endswith('.png')],
            key=lambda x: int(os.path.splitext(x)[0])
        )
        # print(self.image_files[:50])

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.image_files[idx])
        image = Image.open(img_name)

        if self.transform:
            image = self.transform(image)

        return image, self.labels[idx]  # Return image and its index