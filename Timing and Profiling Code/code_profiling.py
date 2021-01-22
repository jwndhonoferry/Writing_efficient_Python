import line_profiler
import numpy as np

heroes = ['Batman', 'Superman', 'CatWoman']
height = np.array([188, 191, 183])
weight = np.array([95, 101, 74])

def convert(hero, h, w):
    new_h = [ht * 0.39370 for ht in h]
    new_w = [wt * 2.20462 for wt in w]

    data_hero = {}

    for i, hero in enumerate(heroes):
        data_hero[hero] = (new_h[i], new_w[i])

    return data_hero
#print
print(convert(heroes, height, weight))
