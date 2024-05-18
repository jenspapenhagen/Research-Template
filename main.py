import torch
print(
    f"Pytorch CUDA availability: {torch.cuda.is_available()}, num gpus:"
    f" {torch.cuda.device_count()}"
)