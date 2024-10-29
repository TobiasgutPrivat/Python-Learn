from RL2048 import *

if __name__ == "__main__":
    # model = load("10k",4)
    model = train(4,100000)
    save("100kNormal",model)
    # evaluate(load("100kHighLearning",4),4,10)
    # evaluate(load("100k",4),4,10)
    evaluate(load("100kNormal",4),4,10)
    # evaluateRandom(4,10)