
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np
import matplotlib.pyplot as plt

from HelperClass2.NeuralNet2 import *
from HelperClass2.DataReader import *

x_data_name = "../../Data/ch09.train.npz"
y_data_name = "../../Data/ch09.test.npz"


def train(hp, folder):
    net = NeuralNet2(hp, folder)
    net.train(dataReader, 50, True)
    trace = net.GetTrainingTrace()
    return trace


def ShowLossHistory(folder, file1, hp1, file2, hp2, file3, hp3, file4, hp4):
    lh = TrainingTrace.Load(file1)
    axes = plt.subplot(2,2,1)
    lh.ShowLossHistory4(axes, hp1)
    
    lh = TrainingTrace.Load(file2)
    axes = plt.subplot(2,2,2)
    lh.ShowLossHistory4(axes, hp2)

    lh = TrainingTrace.Load(file3)
    axes = plt.subplot(2,2,3)
    lh.ShowLossHistory4(axes, hp3)

    lh = TrainingTrace.Load(file4)
    axes = plt.subplot(2,2,4)
    lh.ShowLossHistory4(axes, hp4)

    plt.show()


def try_hyperParameters(folder, n_hidden, batch_size, eta):
    hp = HyperParameters2(1, n_hidden, 1, eta, 10000, batch_size, 0.001, NetType.Fitting, InitialMethod.Xavier)
    filename = str.format("{0}\\{1}_{2}_{3}.pkl", folder, ne, batch, eta).replace('.', '', 1)
    file = Path(filename)
    if file.exists():
        return file, hp
    else:
        lh = train(hp, folder)
        lh.Dump(file)
        return file, hp


if __name__ == '__main__':
  
    dataReader = DataReader(x_data_name, y_data_name)
    dataReader.ReadData()
    dataReader.GenerateValidationSet()
    
    folder = "complex_turn"

    ne, batch, eta = 4, 10, 0.1
    file_1, hp1 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 4, 10, 0.3
    file_2, hp2 = try_hyperParameters(folder, ne, batch, eta)
    
    ne, batch, eta = 4, 10, 0.5
    file_3, hp3 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 4, 10, 0.7
    file_4, hp4 = try_hyperParameters(folder, ne, batch, eta)
    
    ShowLossHistory(folder, file_1, hp1, file_2, hp2, file_3, hp3, file_4, hp4)
    
    ne, batch, eta = 4, 5, 0.5
    file_1, hp1 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 4, 10, 0.5
    file_2, hp2 = try_hyperParameters(folder, ne, batch, eta)

    # already have this data
    ne, batch, eta = 4, 15, 0.5
    file_3, hp3 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 4, 20, 0.5
    file_4, hp4 = try_hyperParameters(folder, ne, batch, eta)
    
    ShowLossHistory(folder, file_1, hp1, file_2, hp2, file_3, hp3, file_4, hp4)

    ne, batch, eta = 2, 10, 0.5
    file_1, hp1 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 4, 10, 0.5
    file_2, hp2 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 6, 10, 0.5
    file_3, hp3 = try_hyperParameters(folder, ne, batch, eta)

    ne, batch, eta = 8, 10, 0.5
    file_4, hp4 = try_hyperParameters(folder, ne, batch, eta)

    ShowLossHistory(folder, file_1, hp1, file_2, hp2, file_3, hp3, file_4, hp4)


