from matplotlib import pyplot as plt
from fake_ros import FakeRos
from uav import UAV


def main():
    num_uav = 3
    bag_file = (
        "/home/lih/from_git/BagPy/bags/demo_all_migration_2023-11-29-10-52-12.bag"
    )
    fake_ros = FakeRos(num_uav, bag_file)
    uavs = [
        UAV(id, fake_ros=True, visualization=True, poses=fake_ros.poses)
        for id in range(1, num_uav + 1)
    ]

    for fake_ros_msg in fake_ros.run():
        for uav in uavs:
            uav.step(fake_ros_msg)


if __name__ == "__main__":
    main()
