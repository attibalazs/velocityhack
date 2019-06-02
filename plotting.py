import lasio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interactive, FloatRangeSlider, FloatSlider, fixed


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
    ax.set_ylim(2, 7)
    ax.set_xlim(0, 3000)
