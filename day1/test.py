import torch
import platform

print(torch.__version__)
print(torch.tensor(0))
print(platform.architecture())
print(platform.mac_ver())