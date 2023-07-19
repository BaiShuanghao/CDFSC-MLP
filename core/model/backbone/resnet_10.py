from torch import nn 
import torch
from torchsummary import summary
from config import CONFIG


class ResidualBlock(nn.Module):
    def __init__(self,in_channels,neurons,isdownsample=False,stride=1):
        super(ResidualBlock,self).__init__()
        self.conv1 = nn.Conv2d(in_channels,neurons,kernel_size=3,padding=1,stride=stride,bias=False)
        self.bn1 = nn.BatchNorm2d(neurons)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(neurons,neurons,kernel_size=3,padding=1,bias=False)
        self.bn2 = nn.BatchNorm2d(neurons)
        self.relu2 = nn.ReLU()
        self.downsample = nn.Sequential(
            nn.Conv2d(in_channels,neurons,kernel_size=1,stride=2,bias=False),
            nn.BatchNorm2d(neurons)
        )
        self.isdownsample = isdownsample
    
    def forward(self,x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.bn2(out)
        if self.isdownsample:
            residual = self.downsample(residual)
        out = out + residual
        out = self.relu2(out)
        return out
       

class ResNet10(nn.Module):
    def __init__(self):
        super(ResNet10,self).__init__()
        self.start = nn.Sequential(
            nn.Conv2d(3,64,kernel_size=7, stride=2, padding=3,bias=False),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=3,stride=2,padding=1),
            nn.ReLU()
        )
        self.conv1 = ResidualBlock(64,64)
        self.conv2 = ResidualBlock(64,128,isdownsample=True,stride=2)
        self.conv3 = ResidualBlock(128,256,isdownsample=True,stride=2)
        self.conv4 = ResidualBlock(256,512,isdownsample=True,stride=2)
        self.avgpool = nn.AvgPool2d(7,stride=1)
        self.fc1 = nn.Linear(512,315)
        self.dropout = nn.Dropout(p=0.2)
        
    def forward(self,x): # 3 * 224 * 224
        x = self.start(x) # 64 * 56 * 56
        x = self.conv1(x) # 64 * 56 * 56
        x = self.conv2(x) # 128 * 
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.avgpool(x)
        x = x.view(x.size(0),-1)
        #x = self.dropout(x)
        #print(x.size())
        x = self.fc1(x)
        return x


if __name__ == '__main__':
    net = ResNet10().to(CONFIG['device'])
    summary(net,(3,224,224))
    sample_input = torch.rand((1,3,224,224)).to(CONFIG['device'])
    output = net(sample_input)
    print(output.shape)
    print(output)