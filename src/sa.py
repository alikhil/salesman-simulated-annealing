"""
Implementation of Simulated Annealing algorithm for solving Traveling Salesman problem

Author: Alik Khilazhev
"""

from geopy.distance import geodesic
from matplotlib.animation import FuncAnimation
from matplotlib.collections import PatchCollection
from matplotlib.lines import Line2D  

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(19680801)

N = 30 # number of cities
loc_dist_cache = {} # cache for location distances 

def city_location(city_id, df):
    return (df.iloc[city_id]["latitude"], df.iloc[city_id]["longitude"])

def compute_location_dist(a, b):
    # using caching for computing dist between 2 geo position
    if a in loc_dist_cache and b in loc_dist_cache[a]:
        return loc_dist_cache[a][b]
    if b in loc_dist_cache and a in loc_dist_cache[b]:
        return loc_dist_cache[b][a]
    dist = geodesic(a, b)
    if a not in loc_dist_cache:
        loc_dist_cache[a] = {}
    if b not in loc_dist_cache:
        loc_dist_cache[b] = {}
    loc_dist_cache[b][a] = loc_dist_cache[a][b] = dist
    return dist

def compute_path_dist(path, df):
    dist = 0
    for i in range(N):
        cur_city_id = path[i]
        next_city_id = path[(i+1) % N]
        dist += compute_location_dist(city_location(cur_city_id, df), city_location(next_city_id, df)).kilometers
    return dist

def p_path(path, T, df):
    return np.exp(-compute_path_dist(path, df)/T)

def generate_updated_path(cur_path):
    path = cur_path[:]
    # choose 2 random in path and swap them
    a, b = np.random.randint(low=0, high=N-1, size=2)
    path[a], path[b] = path[b], path[a]
    return path


def run_simulated_annealing(df, anneal_rate=0.99):
    T = 32000
    # setting initial path
    current_path = [i for i in range(N)]
    np.random.shuffle(current_path)
    
    steps = 0
    distances = []
    distances.append(compute_path_dist(current_path, df))
    accepted_paths = [current_path]
    while T > 0.000001:
        new_path = generate_updated_path(current_path)
        accept_ratio = p_path(new_path, T, df) / p_path(current_path, T, df)
        u = np.random.uniform()
        if u < accept_ratio:
            current_path = new_path
            accepted_paths.append(current_path)
            
        distances.append(compute_path_dist(current_path, df))
        T = T * anneal_rate
        steps += 1
    
    return steps, distances, current_path, accepted_paths


def init():
    """This method is needed for animation """
    global line
    ax.set_xlim(min(lat),max(lat))
    ax.set_ylim(min(lon),max(lon))
    ax.invert_xaxis()
    ax.invert_yaxis()
    
    for i, xy in enumerate(zip(lat, lon)):                                       # <--
        ax.annotate('%s' % df['city'].values[i], xy=xy, textcoords='data')
    
    return line, cities, distText

def update(path):
    """This method is needed for animation """
    global line
    global distText
    dist = compute_path_dist(path, df)
    late = [lat[i] for i in path]
    lone = [lon[i] for i in path]
    late.append(late[0])
    lone.append(lone[0])
    
    line.set_data(late, lone)
    distText.set_text('dist = %dkm' % dist)
    return line, distText

if __name__ == '__main__':

    df = pd.read_csv("../dataset/top30_cities.csv", 
        header=0, 
        encoding="utf8", 
        names=["city", "latitude", "longitude", "population"])

    df[["latitude", "longitude"]] = df[["latitude", "longitude"]].apply(pd.to_numeric)

    lat = df['latitude'].values
    lon = df['longitude'].values

    steps_995, distances_995, shortest_path_995, _ = run_simulated_annealing(df, 0.995)
    steps_97, distances_97, shortest_path_97, _ = run_simulated_annealing(df, 0.97)
    steps_99, distances_99, shortest_path_99, accepted_paths_99 = run_simulated_annealing(df, 0.99)

    # drawing figure showing convergence of SA with different cooling rates
    plt.figure(figsize=(10,10))
    plt.plot(np.arange(0, steps_995 + 1, 1)[:1500], distances_995[:1500], 'g', label='slow cooling(0.995)')
    plt.plot(np.arange(0, steps_99 + 1, 1)[:1500], distances_99[:1500], 'b', label='middle cooling(0.99)')
    plt.plot(np.arange(0, steps_97 + 1, 1), distances_97, 'r', label='fast cooling(0.97)')
    plt.legend()
    plt.ylabel('path distance')
    plt.xlabel('steps count')

    plt.show()

    # clear
    plt.cla()
    plt.clf()
    plt.close()

    # drawing animation how path changes for cooling rate 0.99
    fig, ax = plt.subplots()
    cities, = plt.plot(lat,lon,'o')
    line = Line2D([0],[0], alpha=0.5)
    ax.add_artist(line)
    ax.axis('off')

    distText = plt.text(56, 120, 'dist = 1km', fontsize=12)

    ani = FuncAnimation(fig, update, frames=accepted_paths_99,
                    init_func=init, blit=True)

    ani.save('animation.gif')