import torch.nn as nn

class ResNetBlock(nn.Module):
  def __init__(self, channels):
    super(ResNetBlock, self).__init__()
    
    # defining different layers 
    self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False)
    self.bn1 = nn.BatchNorm2d(channels)
    self.relu = nn.ReLU(inplace=True)
    self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False)
    self.bn2 = nn.BatchNorm2d(channels)

  def forward(self, x):
    residual = x
    
    # block - 1
    out = self.conv1(x)
    out = self.bn1(out)
    out = self.relu(out)
    # block -2
    out = self.conv2(out)
    out = self.bn2(out)
    # skip connection (identiy pass for input)
    out += residual
    # Again adding a final relu function layer
    out = self.relu(out)

    return out