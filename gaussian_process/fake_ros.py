from os import replace
from bagpy import bagreader
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd


class FakeRos:
    def __init__(self, num_uav=0, bag_file="") -> None:
        self.num_uav = num_uav
        self.bag_file = bag_file
        self.bag = bagreader(bag_file)
        self.start_time, self.end_time = self.__get_offboard_time()
        self.__set_poses()

    def __get_offboard_time(self):
        """
        return OFFBOARD start and end time
        """
        mavros_state_files = [
            self.bag.message_by_topic("/drone_{}/mavros/state".format(i))
            for i in range(1, self.num_uav + 1)
        ]
        mavros_states = [
            pd.read_csv(mavros_state_file) for mavros_state_file in mavros_state_files
        ]
        start_times = [
            s.loc[s["mode"].str.contains("OFFBOARD", na=False)].head(1).values[0][0]
            for s in mavros_states
        ]
        end_times = [
            s.loc[s["mode"].str.contains("OFFBOARD", na=False)].tail(1).values[0][0]
            for s in mavros_states
        ]
        START_TIME = min(start_times)
        END_TIME = max(end_times)
        print("start time: {}, end time: {}".format(START_TIME, END_TIME))
        return START_TIME, END_TIME

    def __set_poses(self):
        """
        set self.poses as  UAV poses from self.start_time to self.end_time
        set self.max_index
        """
        pose_files = [
            self.bag.message_by_topic("/drone_{}/mavros/vision_pose/pose".format(i))
            for i in range(1, self.num_uav + 1)
        ]
        poses = [pd.read_csv(pose_file) for pose_file in pose_files]
        poses = [
            pose.loc[
                (pose["Time"] >= self.start_time) & (pose["Time"] <= self.end_time)
            ]
            for pose in poses
        ]
        self.poses = [pose.reset_index(drop=True) for pose in poses]
        self.max_index = self.poses[0].index.stop

    def run(self):
        """
        generate ros msg
        """
        for index in tqdm(range(self.max_index)):
            # return_msg = dict()
            # for i in range(1, self.num_uav + 1):
            #     return_msg["uav_{}_pose".format(i)] = self.poses[i - 1].loc[index]
            # yield return_msg
            yield index


if __name__ == "__main__":
    pass
    bag_file = (
        "/home/lih/from_git/BagPy/bags/demo_all_migration_2023-11-29-10-52-12.bag"
    )
    fake_ros = FakeRos(3, bag_file)
