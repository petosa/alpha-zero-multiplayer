import sys
import torch
import numpy as np
sys.path.append("..")
from model import Model


class DumbNet(Model):


  def forward(self, x):
    batch_size = len(x)
    this_output_shape = tuple([batch_size] + list(self.output_shape))

    p_logits = torch.ones(this_output_shape)
    v = torch.zeros((batch_size, 1))

    return p_logits, v
