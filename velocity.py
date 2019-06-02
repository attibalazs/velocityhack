import numpy as np


def simulate_linear_velocity(depth, vel, k_range=(-3, 3), v0_range=(1500, 5000), nr_samples=100000):
    """
    Simulate linear velocities for each k and v0 combination

    :param depth: depth values
    :param vel: velocities at each depth
    :param k_range: range of the slope, rate of change of velocity by depth
    :param v0_range: initial velocity at the top of the formation
    :param nr_samples: nr of samples to run through the simulation
    :return:
    """
    k = np.random.uniform(*k_range, nr_samples)
    v0 = np.random.uniform(*v0_range, nr_samples)
    pred_vel = depth * k + v0

    # calculate the errors
    mse = np.mean((vel - pred_vel) ** 2, axis=0)
    rmse = np.sqrt(mse)

    return k, v0, pred_vel, rmse


def main():
    depth = np.linspace(100, 2000, 1000).reshape(-1, 1)
    vel = np.linspace(400, 5000, 1000).reshape(-1, 1)
    simulate_linear_velocity(depth, vel)


if __name__ == "__main__":
    main()
