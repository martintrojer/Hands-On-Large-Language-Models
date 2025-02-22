import os

import torch

# os.environ["HSA_OVERRIDE_GFX_VERSION"] = "11.0.1"
# os.environ["PYTORCH_ROCM_ARCH"] = "gfx1101"
# os.environ["HIP_VISIBLE_DEVICES"] = "0"
# os.environ["ROCM_PATH"] = "/opt/rocm"

print(torch.cuda.is_available())
print(os.getenv("HSA_OVERRIDE_GFX_VERSION"))
print("device name [0]:", torch.cuda.get_device_name(0))

d = torch.device("cuda")
print(torch.cuda.get_device_capability(d))
print(torch.__version__)

res = torch.rand(3, 3).to(d)
print(res)

# Creating a tensor from a list
tensor = torch.tensor([1, 2, 3])

# Reshaping the tensor
reshaped_tensor = tensor.view(1, -1)  # Reshape to 1x3 matrix
print("Reshaped Tensor:", reshaped_tensor)

# Performing operations
added_tensor = tensor + tensor
print("Added Tensor:", added_tensor)

# Moving tensor to GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor = tensor.to(device)
print("Tensor device:", tensor.device)
