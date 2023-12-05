# Initial Date: March 2, 2020
# Author: Rahul Bhadani
# Copyright (c)  Rahul Bhadani, Arizona Board of Regents
# All rights reserved.

# from .bagreader import bagreader
from .BagReader import *

from .bagreader import animate_timeseries
from .bagreader import create_fig


# 增加动态方法
@add_method
class bagreader(bagreader):
    pass


print("bagreader init done")
