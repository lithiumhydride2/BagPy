import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class UAV:
    def __init__(self, id=0, fake_ros=True, visualization=False, poses=None) -> None:
        self.id = id
        self.fake_ros = fake_ros  # if true, use ros info from fake ros
        self.visualization = visualization
        self.poses = poses  # all data from fake gps
        try:
            self.pose = self.poses[self.id - 1]
        except IndexError as e:
            print(e)
        self.curr_index = 0  # 能够获取信息的索引

        if self.visualization:
            self.setPlot()
            self.figure = plt.figure(num="uav_{}".format(self.id))
            self.ax = self.figure.add_subplot(111)

    def setPlot(self):
        plt.style.use("default")
        plt.rcParams["figure.figsize"] = [10, 10]
        plt.rcParams["font.family"] = "serif"
        plt.rcParams["mathtext.fontset"] = "dejavuserif"
        plt.rcParams["font.size"] = 12.0
        plt.rcParams["figure.facecolor"] = "#ffffff"
        # plt.rcParams[ 'font.family'] = 'Roboto'
        # plt.rcParams['font.weight'] = 'bold'
        plt.rcParams["xtick.color"] = "#01071f"
        plt.rcParams["xtick.minor.visible"] = True
        plt.rcParams["ytick.minor.visible"] = True
        plt.rcParams["xtick.labelsize"] = 10
        plt.rcParams["ytick.labelsize"] = 10
        plt.rcParams["ytick.color"] = "#01071f"
        plt.rcParams["axes.labelcolor"] = "#000000"
        plt.rcParams["text.color"] = "#000000"
        plt.rcParams["axes.labelcolor"] = "#000000"
        plt.rcParams["grid.color"] = "#f0f1f5"
        plt.rcParams["axes.labelsize"] = 10
        plt.rcParams["axes.titlesize"] = 10
        # plt.rcParams['axes.labelweight'] = 'bold'
        # plt.rcParams['axes.titleweight'] = 'bold'
        plt.rcParams["figure.titlesize"] = 24.0
        plt.rcParams["figure.titleweight"] = "bold"
        plt.rcParams["legend.markerscale"] = 1.0
        plt.rcParams["legend.fontsize"] = 8.0
        plt.rcParams["legend.framealpha"] = 0.5

    def __update_from_fake_ros(self, fake_ros_msg=None):
        if fake_ros_msg is None:
            print("error: no fake ros msg")
        self.curr_index = fake_ros_msg

    def __update_visualization(self):
        self.ax.cla()
        self.ax.set_xlim(-6, 2)
        self.ax.set_ylim(-6, 6)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.plot(
            self.pose.loc[: self.curr_index]["pose.position.x"],
            self.pose.loc[: self.curr_index]["pose.position.y"],
            "r-",
        )
        self.figure.canvas.draw()
        plt.show()

    def step(self, fake_ros_msg=None):
        if self.fake_ros:
            self.__update_from_fake_ros(fake_ros_msg)
        else:
            pass

        if self.visualization:
            self.__update_visualization()


if __name__ == "__main__":
    uav = UAV(1, visualization=True)
