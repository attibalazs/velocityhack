import lasio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def filter_depth(depth, top, bottom):
    """Filters the depth indexes for a top and bottom depth"""
    depth_idx = np.where((bottom > depth) & (top < depth))
    return depth_idx


def plot_log(slider_range, depth, vp):
    """Plots velocity vs depth using a slider filter"""
    fig, ax = plt.subplots(1, 1, figsize=(15, 3))
    ax.clear()
    top = slider_range[0]
    bottom = slider_range[1]
    above_idx = np.where(depth < top)
    below_idx = np.where(depth > bottom)
    between_idx = filter_depth(depth, top, bottom)
    ax.plot(depth[above_idx], vp[above_idx], c="blue")
    ax.plot(depth[below_idx], vp[below_idx], c="blue")
    ax.plot(depth[between_idx], vp[between_idx], c="red")
    ax.axvline(top)
    ax.axvline(bottom)
    ax.set_ylim(1500, 6000)
    ax.set_xlim(0, 3000)


def plot_rmse_ellipse(ax, k, v0, rmse, max_rmse=500):

    # lowest rmse indices
    idx = np.where(rmse <= max_rmse)
    # best fit point
    idx_min = rmse.argmin()

    sc = ax.scatter(k[idx], v0[idx], c=rmse[idx], s=10)
    ax.scatter(k[idx_min], v0[idx_min], c='yellow', s=100, marker='X')
    # plt.colorbar()
    return sc, idx, idx_min


def plot_velocity_predictions(ax, depth, vel, pred_vel, rmse, min_rmse_idx, cutoff=500, nr_samples=5):
    """plot all velocity predictions through the data"""
    # get low, med,high index ranges
    low_rmse_idx = rmse.argsort()[:cutoff]
    med_rmse_idx = rmse.argsort()[cutoff:cutoff * 2]
    high_rmse_idx = rmse.argsort()[cutoff * 2:cutoff * 3]

    print('low:', len(low_rmse_idx), 'med:',len(high_rmse_idx),'high:', len(med_rmse_idx))

    #
    sample_rmse_idx = np.random.choice(low_rmse_idx, nr_samples)

    # fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    lp = ax.plot(depth, pred_vel[:, low_rmse_idx], c='red', alpha=0.1)
    lp = ax.plot(depth, pred_vel[:, med_rmse_idx], c='orange', alpha=0.1)
    lp = ax.plot(depth, pred_vel[:, high_rmse_idx], c='yellow', alpha=0.1)
    lp = ax.plot(depth, pred_vel[:, sample_rmse_idx], c='blue', linewidth=2)
    lp = ax.plot(depth, pred_vel[:, min_rmse_idx], c='green', linewidth=3)

    lp = ax.plot(depth, vel, c='blue', alpha=0.2)

    return lp, sample_rmse_idx
