import torch 

checkpoint = torch.load('asset/weights/PATH-ViT-B.pth', map_location='cpu')
print(checkpoint.keys())
print(checkpoint['model'].keys())