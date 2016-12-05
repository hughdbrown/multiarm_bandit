from __future__ import division, print_function

import random


class MultiArmBandit(object):
    def __init__(self, arms, prob):
        self.arms = arms
        self.prob = prob
        self.rewards = [(0, 0.0)] * len(arms)
    def choose_arm(self):
        if random.random() < self.prob:
            r = max((rewards / (hits + 1), i) for i, (hits, rewards) in enumerate(self.rewards))[1]
        else:
            r = random.randint(0, len(self.arms) - 1)
        assert 0 <= r < len(self.arms)
        return r
    def update_arm(self, arm):
        reward = self.arms[arm].reward()
        hits, rewards = self.rewards[arm]
        self.rewards[arm] = (hits + 1, rewards + reward)
    def simulate(self, simulations):
        for _ in range(simulations):
            arm = self.choose_arm()
            self.update_arm(arm)
    def report(self):
        for (hits, rewards) in self.rewards:
            print((hits, rewards, rewards / (hits + 1)))


class Bandit(object):
    def __init__(self, limit):
        self.limit = limit
    def reward(self):
        return random.random() < self.limit

bandits = [Bandit(x) for x in [0.1, 0.3, 0.5, 0.7, 0.9]]
# bandits = [Bandit(0.1)]
mab = MultiArmBandit(bandits, 0.0)
mab.simulate(10000)
mab.report()

