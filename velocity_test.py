import unittest
import numpy as np
import velocity as v


class VelocityTest(unittest.TestCase):

    def test_simulate_linear_velocity(self):
        depth = np.linspace(100, 2000, 1000).reshape(-1, 1)
        vel = np.linspace(400, 5000, 1000).reshape(-1, 1)
        k, v0, pred_vel, rmse = v.simulate_linear_velocity(depth, vel)

        assert len(pred_vel) > 0
        assert len(rmse) > 0


def main():
    unittest()


if __name__ == "__main__":
    main()
