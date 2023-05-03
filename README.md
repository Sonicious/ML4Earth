# ML4Earth

Project Repository for the ML4Earth Project

simple conda approach:

- xarray
- cubo
- pytorch
- Lightning??

## Installation

### Conda

CPU only, no rapids

```
conda create -n ML4Earth matplotlib zarr cubo xarray pytorch torchvision torchaudio cpuonly -c pytorch -c conda-forge
```

GPU enabled, no rapids

```
conda create -n ML4Earth zarr matplotlib ipykernel lightning cubo xarray pytorch torchvision torchaudio pytorch-cuda -c pytorch -c nvidia -c conda-forge
```

### Docker

- NVIDIA RAPIDS Setup based on PyTorch
	- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/rapidsai
	- Base Image: `nvcr.io/nvidia/pytorch:23.03-py3`
- Everything should be compose oriented
- 