from torch import nn


class MLP_layer(nn.Module):

    def __init__(self, in_dim=10, out_dim=10):
        super(MLP_layer, self).__init__()
        self.linear1 = nn.Linear(in_dim, out_dim)
        self.bn = nn.BatchNorm1d(out_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.linear1(x)
        x = self.bn(x)
        x = self.relu(x)
        return x

class Two_MLP_layer(nn.Module):

    def __init__(self, in_dim=10, hidden_dim=10, out_dim=10):
        super(Two_MLP_layer, self).__init__()
        self.mlp1 = MLP_layer(in_dim, hidden_dim)
        # self.mlp2 = MLP_layer(hidden_dim, out_dim)
        self.linear2 = nn.Linear(hidden_dim, out_dim)

    def forward(self, x):
        x = self.mlp1(x)
        # x = self.mlp2(x)
        x = self.linear2(x)
        
        return x