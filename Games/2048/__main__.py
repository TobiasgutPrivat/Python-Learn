from RL2048 import *

if __name__ == "__main__":
    # model = train(4,10000000)
    # save("10000k",model)
    evaluate(load("10000k",4),4,100)
    evaluateRandom(4,100)