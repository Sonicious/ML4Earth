import torch
import xarray as xr
import lightning.pytorch as pl

print(f"Is CUDA supported by this system? {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
  
available_devices = [torch.cuda.device(i) for i in range(torch.cuda.device_count())]
#available_devices = [range(torch.cuda.device_count())]
print(f"Found {len(available_devices)} CUDA Devices:")

for idx, gpu_id in enumerate(available_devices):
    print(f"{idx:02}: {torch.cuda.get_device_name(gpu_id)}")
