# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:10:32 2022

@author: keyne
"""

# 引入pypsa库(潮流计算库)
# pypsa库对于潮流的构建形式与构建神经网络类似
import pypsa
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# 利用pypsa生成潮流网络
network = pypsa.Network()
# 设置潮流网络的节点数目
n_buses = 9

# 在网络中添加母线
# 添加母线的个数为节点数目个
network.add('Bus', 'My bus {}'.format(0),
            v_nom=345.,
            v_mag_pu_min = 0.9,
            v_mag_pu_max = 1.1)
network.add('Bus', 'My bus {}'.format(1),
            v_nom=345.,
            v_mag_pu_min = 0.9,
            v_mag_pu_max = 1.1)
network.add('Bus', 'My bus {}'.format(2),
            v_nom=345.,
            v_mag_pu_min = 0.9,
            v_mag_pu_max = 1.1)
network.add('Bus', 'My bus {}'.format(3),
            v_nom=345.)
network.add('Bus', 'My bus {}'.format(4),
            v_nom=345.)
network.add('Bus', 'My bus {}'.format(5),
            v_nom=345.)
network.add('Bus', 'My bus {}'.format(6),
            v_nom=345.)
network.add('Bus', 'My bus {}'.format(7),
            v_nom=345.)
network.add('Bus', 'My bus {}'.format(8),
            v_nom=345.)

# 查看节点信息，其本质上是network对象的一个属性
# 当只想看前5行数据(判断是否正确提取)时，输入
# network.buses.head()
# 当想看前k行时，可输入
# network.buses.head(n=k)
network.buses

# 添加各个节点之间的线路
# 此处设置的为3节点系统的环网结构
# 其中bus0和bus1为这根线路的两端母线(即bus0和bus1由该线路连接)
# 其中bus0为起点，bus1为终点
# 此处各条线路阻抗采用相同参数
network.add('Line', 'My line 0-3',
            bus0='My bus {}'.format(0),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(3),
            # 设置线路阻抗
            x=0.0576,
            r=0.,
            b=0.)
network.add('Line', 'My line 1-7',
            bus0='My bus {}'.format(1),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(7),
            # 设置线路阻抗
            x=0.0625,
            r=0.,
            b=0.)
network.add('Line', 'My line 2-5',
            bus0='My bus {}'.format(2),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(5),
            # 设置线路阻抗
            x=0.0586,
            r=0.,
            b=0.)
network.add('Line', 'My line 3-4',
            bus0='My bus {}'.format(3),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(4),
            # 设置线路阻抗
            x=0.092,
            r=0.017,
            b=0.158)
network.add('Line', 'My line 3-8',
            bus0='My bus {}'.format(3),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(8),
            # 设置线路阻抗
            x=0.085,
            r=0.01,
            b=0.176)
network.add('Line', 'My line 4-5',
            bus0='My bus {}'.format(4),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(5),
            # 设置线路阻抗
            x=0.17,
            r=0.039,
            b=0.358)
network.add('Line', 'My line 5-6',
            bus0='My bus {}'.format(5),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(6),
            # 设置线路阻抗
            x=0.1008,
            r=0.0119,
            b=0.209)
network.add('Line', 'My line 6-7',
            bus0='My bus {}'.format(6),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(7),
            # 设置线路阻抗
            x=0.072,
            r=0.0085,
            b=0.149)
network.add('Line', 'My line 7-8',
            bus0='My bus {}'.format(7),
            # 当i到了3的时候，i%3=0, 此时是3-0
            bus1='My bus {}'.format(8),
            # 设置线路阻抗
            x=0.161,
            r=0.032,
            b=0.306)

# 查看线路信息
network.lines

# 在节点(节点1)加入发电机，设置为PV节点
network.add('Generator', 'My gen 0',
            bus='My bus 1',
            p_set=163,
            v_mag_pu_set = 345,
            control='PV')
# 在节点(节点2)加入发电机，设置为PV节点
network.add('Generator', 'My gen 1',
            bus='My bus 2',
            p_set=85,
            v_mag_pu_set = 345,
            control='PV')

# 查看发电机信息
network.generators
# 查看发电机节点注入有功
network.generators.p_set


# 在节点(节点4)加入负荷
network.add('Load', 'My load 0',
            bus='My bus 4',
            p_set=90,
            q_set=30)
# 在节点(节点6)加入负荷
network.add('Load', 'My load 1',
            bus='My bus 6',
            p_set=100,
            q_set=35)
# 在节点(节点8)加入负荷
network.add('Load', 'My load 2',
            bus='My bus 8',
            p_set=125,
            q_set=50)

# 在节点(节点0)加入平衡节点
network.add('Generator', 'My Slack',
            bus = 'My bus 0',
            control = 'Slack')

# 查看负荷信息
network.loads
# 查看负荷消耗有功
network.loads.p_set

# 计算前进行一致性检查
network.consistency_check()

# 查看网络结构图
# 若不对节点大小进行设置，可能会导致导线被节点遮盖
# 建议设置节点大小bus_sizes = 0.002
# network.plot()
network.plot(bus_sizes = 0.002)

#计算潮流(牛拉法)并查看结果
network.pf()
# iterations with error of 0.000000 in 0.025739 seconds
# {'n_iter': 0
# now 3,-->收敛代数
# 'error': 0
# now 4.753531e-10, -->收敛误差
# 'converged': 0
# now True} -->收敛

# 线路有功
# 其中p0、q0为从bus0中流到line的有功、无功
# 其中p1、q1为从bus1中流到line的有功、无功
network.lines_t.p0
# 母线注入功率
network.buses_t.p
network.buses_t.q
# 电压相角(默认是弧度制)
network.buses_t.v_ang*180/np.pi
# 电压幅值（标幺值）
network.buses_t.v_mag_pu