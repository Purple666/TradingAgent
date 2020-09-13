import torch
import math


def test_mean_var1():
    x = torch.randn(512)
    for i in range(100):
        a = torch.randn(512, 512)
        x = a @ x
    print(x.mean(), x.std())


def test_mean_var2():
    x = torch.randn(512)
    for i in range(100):
        a = torch.randn(512, 512)
        x = a @ x
        if torch.isnan(x.std()):
            print("x.std() is nan at step: ", i)
            break
    print(x.mean(), x.std())


def test_mean_var3():
    mean, var = 0.0, 0.0
    for i in range(100):
        x = torch.randn(512)
        a = torch.randn(512, 512)
        y = a @ x
        mean += y.mean().item()
        var += y.pow(2).mean().item()
    print(mean / 100, math.sqrt(var / 100))


if __name__ == '__main__':
    # test_mean_var1()
    # test_mean_var2()
    test_mean_var3()
    # mean, var = 0.0, 0.0
    # for i in range(10000):
    #     x = torch.randn(1)
    #     a = torch.randn(1)
    #     y = a * x
    #     mean += y.item()
    #     var += y.pow(2).item()
    # print(mean / 10000, math.sqrt(var / 10000))
