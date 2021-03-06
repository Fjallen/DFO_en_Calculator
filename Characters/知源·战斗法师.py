from PublicReference.carry.base import *


# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型, 输出类型):
#         if 武器类型 == '矛':
#             return round(self.CD / self.恢复 * 1.05, 1)
#         if 武器类型 == '棍棒':
#             return round(self.CD / self.恢复 * 0.95, 1)


class 技能0(被动技能):
    名称 = '尼巫的战斗术'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)


class 技能1(被动技能):
    名称 = '炫纹'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20+0.00*self.等级, 3)


class 技能2(被动技能):
    名称 = '矛精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['星纹陨爆','一骑当千碎霸','太古星河·殒灭']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.05

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '矛':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能3(被动技能):
    名称 = '棍棒精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['星纹陨爆','一骑当千碎霸','太古星河·殒灭']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '棍棒':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能4(主动技能):
    名称 = '炫纹发射'
    备注 = '(个数,TP为强化炫纹)'
    是否主动 = 0
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46

    data = [int(i * 1.1611) for i in [0, 242, 266, 293, 316, 342, 365, 390, 413, 439, 464, 490, 513, 538, 563, 587, 612, 638, 662, 686, 712, 735, 760, 784, 809, 835, 860, 883, 909, 932, 957, 980, 1007, 1032, 1057, 1081, 1105, 1131, 1154, 1181, 1205, 1229, 1252, 1278, 1302, 1326, 1351, 1377, 1402, 1426, 1451, 1476, 1500, 1523, 1551, 1574, 1599, 1623, 1648, 1671, 1697, 1721, 1748, 1771, 1796, 1819, 1845, 1870, 1893, 1920, 1944]]

    # 95被动,默认超大炫纹,倍率*1.5
    倍率 = 1.5

    CD = 0.25
    TP成长 = 0.10
    TP上限 = 1

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能5(主动技能):
    名称 = '双重锤击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 第一击物理攻击力：<data0>%10.6
    data0 = [int(x*1.179) for x in[0, 456, 503, 553, 600, 645, 692, 739, 787, 834, 881, 926, 972, 1023, 1070, 1116, 1169, 1216, 1262, 1308, 1356, 1403, 1450, 1497, 1543, 1589, 1639, 1686, 1732, 1780, 1828, 1874, 1920, 1966, 2014, 2063, 2110, 2158, 2203, 2250, 2298, 2344, 2392, 2440, 2483, 2537, 2583, 2629, 2679, 2726, 2774, 2820, 2868, 2914, 2960, 3008, 3057, 3102, 3151, 3197, 3244, 3290, 3338, 3386, 3432, 3477, 3528, 3574, 3621, 3668, 3714]]
    攻击次数 = 1.0
    # 最后一击物理攻击力：<data1>%
    data1 = [int(x*1.179) for x in[0, 1675, 1851, 2021, 2194, 2369, 2542, 2715, 2890, 3060, 3234, 3409, 3582, 3753, 3928, 4100, 4276, 4449, 4617, 4793, 4968, 5140, 5316, 5487, 5657, 5833, 6007, 6181, 6352, 6527, 6698, 6873, 7045, 7219, 7392, 7564, 7741, 7916, 8083, 8258, 8432, 8607, 8781, 8950, 9123, 9300, 9474, 9642, 9817, 9990, 10166, 10340, 10509, 10682, 10858, 11034, 11206, 11374, 11550, 11723, 11898, 12074, 12240, 12416, 12593, 12763, 12938, 13109, 13284, 13456, 13633]]
    攻击次数2 = 1.0
    # 冲击波独立物理攻击力：<data2>%
    data2 = [int(x*1.179) for x in[0, 1280, 1410, 1543, 1675, 1807, 1941, 2070, 2203, 2336, 2473, 2603, 2736, 2868, 2998, 3131, 3262, 3395, 3528, 3658, 3791, 3923, 4060, 4189, 4325, 4455, 4586, 4718, 4849, 4986, 5116, 5244, 5380, 5510, 5648, 5779, 5907, 6042, 6173, 6305, 6437, 6573, 6701, 6833, 6967, 7094, 7235, 7365, 7493, 7630, 7761, 7894, 8025, 8159, 8286, 8420, 8555, 8684, 8823, 8952, 9080, 9218, 9347, 9478, 9612, 9741, 9877, 10007, 10141, 10272, 10409]]
    攻击次数2 = 1.0
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(主动技能):
    名称 = '炫纹爆弹'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 直刺5.97
    data0 = [int(x*1.179) for x in[0, 1170, 1294, 1410, 1535, 1665, 1777, 1908, 2026, 2147, 2266, 2387, 2507, 2632, 2747, 2872, 2992, 3112, 3231, 3350, 3472, 3601, 3713, 3842, 3971, 4082, 4214, 4333, 4453, 4572, 4693, 4814, 4938, 5053, 5177, 5297, 5418, 5538, 5660, 5778, 5909, 6019, 6149, 6275, 6388, 6512, 6628, 6754, 6875, 6994, 7112, 7233, 7354, 7484, 7602, 7724, 7845, 7965, 8085, 8216, 8334, 8455, 8575, 8696, 8815, 8934, 9058, 9180, 9300, 9421, 9539]]
    攻击次数 = 1.0
    # 多段
    data1 = [int(x*1.179) for x in[0, 146, 159, 174, 190, 210, 225, 239, 251, 270, 281, 295, 320, 331, 343, 349, 375, 391, 400, 426, 429, 451, 465, 480, 496, 512, 531, 535, 560, 570, 586, 609, 616, 630, 639, 664, 680, 690, 710, 718, 735, 750, 771, 786, 801, 817, 826, 849, 855, 871, 896, 906, 919, 935, 950, 970, 986, 991, 1011, 1027, 1040, 1056, 1072, 1091, 1106, 1120, 1136, 1145, 1160, 1176, 1192]]
    攻击次数2 = 13.0
    # 爆炸
    data2 = [int(x*1.179) for x in[0, 3522, 3883, 4243, 4613, 4976, 5339, 5699, 6069, 6432, 6789, 7155, 7524, 7884, 8254, 8614, 8980, 9351, 9701, 10070, 10429, 10794, 11158, 11527, 11898, 12257, 12616, 12982, 13351, 13704, 14073, 14438, 14797, 15167, 15529, 15899, 16264, 16619, 16983, 17345, 17715, 18075, 18440, 18810, 19171, 19530, 19891, 20266, 20620, 20986, 21355, 21718, 22083, 22442, 22802, 23173, 23533, 23902, 24264, 24629, 24988, 25357, 25720, 26086, 26444, 26813, 27173, 27546, 27905, 28266, 28629]]
    攻击次数2 = 1.0
    演出时间 = 12.0
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.6

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '碎霸'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data = [int(x*1.155) for x in[0, 4057, 4475, 4897, 5316, 5734, 6151, 6570, 6992, 7412, 7830, 8251, 8671, 9091, 9511, 9931, 10347, 10767, 11187, 11605, 12028, 12447, 12866, 13286, 13707, 14128, 14544, 14961, 15382, 15801, 16223, 16641, 17063, 17483, 17902, 18318, 18737, 19157, 19578, 20000, 20417, 20837, 21260, 21677, 22099, 22514, 22933, 23354, 23772, 24193, 24614, 25034, 25453, 25872, 26294, 26708, 27131, 27548, 27969, 28389, 28809, 29230, 29649, 30070, 30485, 30904, 31324, 31743, 32166, 32584, 33004]]
    CD = 8
    基础释放次数 = 0
    TP成长 = 0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0

    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = '炫纹融合(旋转)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 成长有变化 整个技能需改
    data = [int(x*1.167) for x in[0, 279, 307, 336, 364, 393, 420, 448, 477, 505, 534, 562, 591, 619, 646, 675, 703, 732, 760, 789, 817, 846, 874, 901, 930, 958, 987, 1015, 1044, 1072, 1101, 1129, 1156, 1186, 1213, 1242, 1270, 1299, 1327, 1356, 1384, 1412, 1441, 1468, 1497, 1525, 1554, 1582, 1611, 1639, 1667, 1696, 1723, 1752, 1780, 1809, 1837, 1866, 1894, 1922, 1951, 1978, 2007, 2035, 2064, 2092, 2121, 2149, 2177, 2206, 2233]]
    攻击次数 = 15
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * self.攻击次数 * self.倍率


class 技能9(主动技能):
    名称 = '流星闪影击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data = [int(x*1.179) for x in[0, 9154, 10084, 11013, 11941, 12870, 13802, 14726, 15659, 16590, 17512, 18442, 19373, 20302, 21228, 22160, 23084, 24014, 24941, 25873, 26804, 27732, 28660, 29589, 30519, 31449, 32379, 33300, 34232, 35163, 36091, 37020, 37950, 38876, 39805, 40730, 41662, 42593, 43521, 44445, 45378, 46307, 47235, 48167, 49095, 50022, 50951, 51881, 52809, 53736, 54666, 55594, 56522, 57453, 58383, 59312, 60236, 61165, 62097, 63024, 63956, 64882, 65810, 66740, 67670, 68599, 69527, 70457, 71383, 72312, 73240]]
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.6

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '炫纹强压'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data = [int(x*1.05) for x in[0, 9768, 10759, 11750, 12741, 13732, 14723, 15714, 16705, 17696, 18687, 19678, 20669, 21660, 22651, 23642, 24633, 25624, 26615, 27606, 28597, 29588, 30579, 31570, 32561, 33552, 34543, 35534, 36525, 37516, 38507, 39498, 40489, 41480, 42471, 43462, 44453, 45444, 46435, 47426, 48417, 49408, 50399, 51390, 52381, 53372, 54363, 55354, 56345, 57336, 58328, 59319, 60310, 61301, 62292, 63284, 64275, 65266, 66257, 67248, 68239, 69230, 70221, 71212, 72203, 73194, 74185, 75176, 76167, 77158, 78149]]
    CD = 17
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.4

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
            self.CD *= 0.92

        elif x == 1:
            self.倍率 *= 1.31
            self.CD *= 0.92

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能11(主动技能):
    名称 = '强袭流星打'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data = [int(x*1.179) for x in[0, 10504, 11592, 12681, 13760, 14846, 15937, 17025, 18112, 19197, 20289, 21372, 22450, 23544, 24629, 25720, 26800, 27883, 28975, 30061, 31144, 32236, 33317, 34411, 35491, 36577, 37670, 38754, 39835, 40926, 42008, 43101, 44188, 45267, 46360, 47443, 48536, 49616, 50702, 51796, 52877, 53955, 55048, 56133, 57227, 58306, 59393, 60486, 61568, 62653, 63741, 64824, 65916, 67000, 68085, 69176, 70262, 71344, 72432, 73520, 74612, 75696, 76773, 77863, 78954, 80040, 81122, 82210, 83299, 84386, 85470]]
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.05*1.13
        elif x == 1:
            self.倍率 *= 1.05*1.22

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(主动技能):
    名称 = '煌龙偃月'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(x*1.179) for x in[0, 4188, 4619, 5058, 5487, 5921, 6353, 6787, 7217, 7656, 8087, 8520, 8954, 9384, 9819, 10255, 10687, 11122, 11551, 11984, 12418, 12853, 13284, 13720, 14151, 14583, 15020, 15451, 15884, 16320, 16752, 17179, 17620, 18050, 18482, 18917, 19348, 19779, 20219, 20650, 21082, 21515, 21948, 22378, 22815, 23249, 23684, 24115, 24546, 24983, 25413, 25847, 26283, 26715, 27145, 27583, 28014, 28445, 28880, 29310, 29743, 30182, 30612, 31044, 31478, 31912, 32341, 32783, 33213, 33641, 34077]]
    攻击次数 = 1.0
    data1 = [int(x*1.179) for x in[0, 1397, 1540, 1688, 1833, 1976, 2117, 2262, 2405, 2552, 2697, 2840, 2984, 3128, 3274, 3417, 3563, 3708, 3851, 3996, 4143, 4287, 4430, 4574, 4717, 4859, 5008, 5152, 5295, 5438, 5585, 5729, 5874, 6018, 6161, 6306, 6450, 6594, 6739, 6885, 7028, 7171, 7316, 7459, 7605, 7750, 7893, 8038, 8181, 8329, 8476, 8617, 8761, 8905, 9049, 9195, 9339, 9483, 9626, 9770, 9915, 10061, 10205, 10349, 10493, 10638, 10780, 10929, 11072, 11217, 11359]]
    攻击次数2 = 7.0
    data2 = [int(x*1.179) for x in[0, 5990, 6605, 7228, 7848, 8464, 9087, 9707, 10321, 10945, 11564, 12180, 12806, 13423, 14036, 14660, 15281, 15900, 16518, 17138, 17757, 18376, 18994, 19618, 20237, 20852, 21477, 22093, 22709, 23335, 23953, 24568, 25193, 25811, 26425, 27049, 27667, 28284, 28912, 29527, 30145, 30771, 31384, 32002, 32626, 33243, 33867, 34483, 35100, 35725, 36342, 36959, 37586, 38201, 38820, 39443, 40059, 40678, 41301, 41918, 42536, 43155, 43774, 44395, 45012, 45633, 46251, 46871, 47488, 48108, 48732]]
    攻击次数3 = 1.0
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 += 3
            self.data2 = [int(i*1.1) for i in self.data2]
        elif x == 1:
            self.攻击次数2 += 3
            self.data2 = [int(i*1.36) for i in self.data2]

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能13(主动技能):
    名称 = '煌龙乱舞'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(x*1.179) for x in[0, 1423, 1568, 1712, 1857, 2001, 2146, 2290, 2435, 2579, 2723, 2868, 3012, 3157, 3300, 3446, 3590, 3734, 3879, 4024, 4168, 4312, 4457, 4601, 4746, 4889, 5035, 5179, 5324, 5468, 5613, 5756, 5902, 6046, 6189, 6335, 6479, 6623, 6768, 6913, 7057, 7202, 7345, 7491, 7635, 7778, 7924, 8068, 8212, 8357, 8502, 8645, 8791, 8935, 9079, 9224, 9369, 9512, 9657, 9801, 9946, 10091, 10234, 10380, 10524, 10668, 10813, 10958, 11101, 11246, 11391]]
    攻击次数 = 5.0
    data1 = [int(x*1.179) for x in[0, 10679, 11762, 12844, 13928, 15012, 16096, 17179, 18263, 19346, 20428, 21512, 22595, 23680, 24763, 25847, 26929, 28012, 29096, 30179, 31263, 32347, 33431, 34513, 35597, 36680, 37763, 38847, 39929, 41013, 42097, 43181, 44264, 45346, 46430, 47513, 48597, 49680, 50765, 51848, 52931, 54014, 55097, 56181, 57264, 58347, 59431, 60515, 61598, 62681, 63765, 64847, 65931, 67014, 68098, 69182, 70266, 71348, 72431, 73515, 74598, 75682, 76764, 77850, 78932, 80015, 81099, 82182, 83266, 84348, 85432]]
    攻击次数2 = 1.0
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1
            self.data0 = [int(i*1.14) for i in self.data0]
            self.data1 = [int(i*1.18) for i in self.data1]
        elif x == 1:
            self.攻击次数 += 1
            self.data0 = [int(i*1.14) for i in self.data0]
            self.data1 = [int(i*1.29) for i in self.data1]

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(被动技能):
    名称 = '斗神意志'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级, 3)


class 技能15(主动技能):
    名称 = '星纹陨爆'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data = [int(x*1.179) for x in[0, 55403, 68248, 81095, 93942, 106790, 119637, 132483, 145331, 158177, 171024, 183872, 196718, 209565, 222412, 235259, 248105, 260952, 273800, 286647, 299493, 312341, 325187, 338034, 350880, 363728, 376575, 389422, 402270, 415115, 427962, 440810, 453657, 466504, 479350, 492197, 505044, 517891, 530739, 543585, 556432, 569280, 582126, 594972, 607819, 620667, 633514, 646361, 659208, 672054, 684901, 697749, 710595, 723442, 736289, 749136, 761982, 774829, 787677, 800524, 813371, 826217, 839064, 851911, 864758, 877606, 890452, 903299, 916147, 928993, 941839]]
    CD = 145.0
    演出时间 = 2

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * self.攻击次数 * self.倍率


class 技能16(主动技能):
    名称 = '变身贝亚娜'
    备注 = '(一轮)'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    data0 = [int(x*1.0) for x in[0, 385, 475, 565, 655, 745, 834, 925, 1015, 1107, 1196, 1286, 1377, 1466, 1558, 1646, 1736, 1827, 1916, 2006, 2098, 2187, 2278, 2368, 2457, 2549, 2638, 2727, 2818, 2908, 2999, 3089, 3179, 3269, 3359, 3451, 3539, 3629, 3720, 3809, 3900, 3991, 4080, 4171, 4261, 4351, 4442, 4530, 4620, 4711, 4800, 4892, 4982, 5071, 5162, 5253, 5344, 5432, 5522, 5612, 5702, 5793, 5883, 5973, 6064, 6153, 6244, 6335, 6423, 6513, 6604]]
    攻击次数 = 2.0
    data1 = [int(x*1.0) for x in[0, 770, 949, 1130, 1309, 1491, 1670, 1850, 2031, 2211, 2391, 2572, 2751, 2932, 3113, 3292, 3472, 3652, 3834, 4013, 4192, 4374, 4554, 4734, 4913, 5094, 5275, 5456, 5634, 5815, 5995, 6177, 6355, 6535, 6717, 6897, 7077, 7256, 7437, 7618, 7799, 7977, 8158, 8338, 8520, 8698, 8878, 9060, 9240, 9419, 9599, 9780, 9961, 10140, 10320, 10501, 10681, 10861, 11041, 11221, 11403, 11582, 11762, 11942, 12123, 12302, 12483, 12663, 12844, 13023, 13204]]
    攻击次数2 = 1.0
    # 基本攻击第三段
    data2 = [int(x*1.0) for x in[0, 961, 1187, 1411, 1638, 1862, 2088, 2312, 2540, 2764, 2989, 3214, 3440, 3665, 3890, 4116, 4342, 4567, 4792, 5016, 5243, 5467, 5694, 5918, 6145, 6369, 6595, 6819, 7047, 7271, 7495, 7722, 7946, 8172, 8396, 8624, 8848, 9074, 9298, 9525, 9749, 9974, 10199, 10426, 10651, 10876, 11101, 11327, 11552, 11777, 12001, 12229, 12453, 12679, 12903, 13130, 13354, 13581, 13805, 14032, 14256, 14480, 14706, 14931, 15158, 15382, 15608, 15833, 16059, 16283, 16508]]
    攻击次数3 = 1.0
    CD = 1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2+self.data2[self.等级] * self.攻击次数3) * self.倍率


class 技能17(主动技能):
    名称 = '变身贝亚娜苍天击'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    data = [int(x*1.179) for x in[0, 1446, 1785, 2123, 2461, 2799, 3138, 3474, 3816, 4156, 4492, 4829, 5169, 5507, 5845, 6186, 6525, 6862, 7202, 7540, 7878, 8217, 8557, 8895, 9233, 9572, 9909, 10248, 10589, 10926, 11266, 11604, 11942, 12280, 12620, 12959, 13295, 13637, 13975, 14312, 14650, 14990, 15328, 15666, 16006, 16343, 16684, 17023, 17360, 17699, 18037, 18375, 18714, 19054, 19394, 19731, 20070, 20408, 20746, 21087, 21425, 21763, 22101, 22441, 22777, 23116, 23458, 23793, 24133, 24471, 24810]]
    CD = 1

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * self.攻击次数 * self.倍率


class 技能18(主动技能):
    名称 = '变身贝亚娜天地碎霸'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    data0 = [int(x*1.179) for x in[0, 693, 856, 1018, 1181, 1344, 1656, 1834, 2014, 2192, 2371, 2552, 2729, 2910, 3088, 3266, 3445, 3625, 3802, 3982, 4159, 4340, 4518, 4696, 4877, 5056, 5234, 5413, 5591, 5771, 5950, 6126, 6306, 6485, 6663, 6842, 7020, 7198, 7380, 7559, 7737, 7917, 8094, 8274, 8452, 8630, 8810, 8989, 9167, 9346, 9524, 9705, 9884, 10061, 10242, 10420, 10599, 10776, 10957, 11134, 11313, 11490, 11671, 11849, 12030, 12208, 12387, 12566, 12744, 12923, 13102]]
    攻击次数 = 1.0
    data1 = [int(x*1.179) for x in[0, 3052, 3768, 4480, 5196, 5910, 7289, 8076, 8861, 9652, 10438, 11221, 12009, 12795, 13581, 14367, 15153, 15943, 16728, 17514, 18302, 19087, 19872, 20660, 21447, 22236, 23021, 23807, 24596, 25381, 26166, 26954, 27740, 28525, 29314, 30101, 30887, 31673, 32457, 33248, 34032, 34818, 35607, 36392, 37179, 37964, 38752, 39539, 40324, 41110, 41898, 42684, 43473, 44259, 45045, 45831, 46617, 47405, 48192, 48978, 49763, 50551, 51336, 52124, 52911, 53696, 54485, 55267, 56056, 56844, 57629]]
    攻击次数2 = 1.0
    CD = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * self.倍率


class 技能19(主动技能):
    名称 = '闪击碎霸'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data = [int(x*1.179) for x in[0, 16576, 18257, 19937, 21619, 23303, 24987, 26665, 28348, 30029, 31711, 33390, 35074, 36756, 38438, 40117, 41801, 43485, 45165, 46846, 48528, 50210, 51892, 53569, 55254, 56938, 58614, 60296, 61982, 63663, 65341, 67023, 68707, 70388, 72067, 73749, 75435, 77115, 78794, 80478, 82162, 83842, 85523, 87204, 88886, 90570, 92247, 93931, 95614, 97291, 98974, 100659, 102341, 104021, 105699, 107381, 109068, 110743, 112427, 114109, 115794, 117471, 119156, 120835, 122520, 124201, 125880, 127564, 129247, 130925, 132605]]
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.9
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
            self.CD *= 0.90

        elif x == 1:
            self.倍率 *= 1.24
            self.CD *= 0.90

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能20(主动技能):
    名称 = '流星雷连击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data = [int(x*1.179) for x in[0, 27346, 30117, 32890, 35661, 38437, 41207, 43980, 46752, 49524, 52296, 55071, 57842, 60615, 63386, 66160, 68932, 71705, 74477, 77251, 80022, 82796, 85565, 88339, 91113, 93883, 96656, 99427, 102200, 104974, 107746, 110519, 113292, 116062, 118836, 121607, 124380, 127154, 129927, 132699, 135472, 138242, 141018, 143785, 146560, 149333, 152105, 154877, 157648, 160422, 163195, 165967, 168739, 171513, 174284, 177057, 179827, 182603, 185375, 188146, 190918, 193692, 196463, 199238, 202007, 204781, 207553, 210325, 213098, 215872, 218644]]
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.10
        elif x == 1:
            self.倍率 *= 1.19

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能21(被动技能):
    名称 = '战灵潜能'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级, 3)


class 技能22(主动技能):
    名称 = '炫纹簇'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(x*1.179) for x in[0, 5820, 6410, 7000, 7592, 8182, 8773, 9363, 9953, 10544, 11135, 11725, 12315, 12904, 13495, 14085, 14676, 15267, 15857, 16448, 17038, 17628, 18220, 18810, 19401, 19991, 20581, 21172, 21763, 22353, 22943, 23533, 24124, 24714, 25306, 25896, 26486, 27077, 27667, 28258, 28848, 29440, 30030, 30619, 31209, 31800, 32390, 32981, 33571, 34161, 34752, 35342, 35933, 36524, 37114, 37705, 38295, 38886, 39476, 40068, 40658, 41248, 41839, 42429, 43019, 43611, 44200, 44791, 45381, 45971, 46562]]
    攻击次数 = 7.0
    CD = 45
    演出时间 = 1.3
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] *self.攻击次数* self.倍率

    def 装备护石(self, x):
        self.攻击次数 -=6
        self.倍率 *= 1+6.95+1.25


class 技能23(主动技能):
    名称 = '使徒之舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(x*1.179) for x in[0, 1710, 1882, 2056, 2230, 2405, 2578, 2752, 2924, 3097, 3270, 3446, 3617, 3791, 3964, 4140, 4313, 4486, 4659, 4832, 5006, 5180, 5355, 5527, 5698, 5872, 6046, 6223, 6394, 6567, 6741, 6914, 7089, 7263, 7435, 7608, 7781, 7957, 8130, 8301, 8474, 8648, 8822, 8997, 9171, 9344, 9516, 9690, 9865, 10039, 10211, 10383, 10558, 10731, 10903, 11077, 11251, 11424, 11597, 11774, 11946, 12119, 12292, 12466, 12641, 12814, 12985, 13161, 13332, 13506, 13679]]
    攻击次数 = 3.0
    data1 = [int(x*1.179) for x in[0, 3421, 3767, 4115, 4461, 4807, 5155, 5501, 5848, 6196, 6544, 6889, 7237, 7582, 7929, 8276, 8624, 8971, 9319, 9667, 10013, 10358, 10705, 11053, 11400, 11748, 12094, 12441, 12786, 13134, 13483, 13828, 14175, 14524, 14871, 15216, 15565, 15909, 16257, 16605, 16952, 17300, 17646, 17991, 18338, 18687, 19033, 19381, 19727, 20076, 20422, 20768, 21114, 21462, 21808, 22157, 22502, 22852, 23198, 23543, 23891, 24238, 24586, 24931, 25279, 25625, 25973, 26318, 26666, 27014, 27361]]
    攻击次数2 = 1.0
    data2 = [int(x*1.179) for x in[0, 34210, 37676, 41141, 44605, 48070, 51551, 55016, 58480, 61962, 65442, 68893, 72373, 75821, 79303, 82766, 86248, 89714, 93193, 96658, 100124, 103589, 107053, 110534, 113999, 117480, 120946, 124409, 127875, 131339, 134821, 138284, 141751, 145231, 148712, 152161, 155641, 159090, 162572, 166052, 169516, 172982, 176462, 179912, 183393, 186873, 190323, 193819, 197269, 200748, 204214, 207679, 211145, 214625, 218072, 221570, 225020, 228500, 231982, 235430, 238910, 242375, 245858, 249320, 252785, 256251, 259732, 263181, 266662, 270143, 273607]]
    攻击次数3 = 1.0
    CD = 40
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.36801

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * self.倍率


class 技能24(主动技能):
    名称 = '一骑当千碎霸'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(x*1.179) for x in[0, 55000, 67751, 80505, 93260, 106011, 118763, 131519, 144272, 157027, 169780, 182535, 195287, 208041, 220790, 233544, 246297, 259052, 271806, 284561, 297315, 310066, 322820, 335574, 348328, 361081, 373833, 386586, 399339, 412092, 424848, 437600, 450355, 463107, 475860, 488614, 501368, 514122, 526875, 539625, 552378, 565133, 577889, 590641, 603395, 616148, 628902, 641657, 654408, 667160, 679914, 692666, 705419, 718175, 730928, 743683, 756437, 769187, 781940, 794695, 807448, 820201, 832954, 845708, 858461, 871217, 883968, 896722, 909476, 922230, 934983]]
    攻击次数 = 1.0
    data1 = [int(x*1.179) for x in[0, 36666, 45169, 53671, 62174, 70677, 79178, 87677, 96181, 104683, 113186, 121688, 130188, 138693, 147195, 155696, 164200, 172702, 181207, 189707, 198208, 206711, 215213, 223716, 232219, 240718, 249223, 257725, 266228, 274729, 283230, 291734, 300235, 308740, 317239, 325741, 334246, 342746, 351249, 359753, 368254, 376758, 385258, 393761, 402264, 410766, 419267, 427769, 436270, 444774, 453275, 461780, 470281, 478783, 487287, 495788, 504293, 512793, 521296, 529800, 538298, 546800, 555302, 563806, 572308, 580810, 589311, 597814, 606317, 614819, 623323]]
    攻击次数2 = 1.0
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * self.倍率


class 技能25(主动技能):
    名称 = '炫纹之源：太古神光'
    所在等级 = 95
    等级上限 = 60
    基础等级 = 6
    data0 = [int(x*1.179) for x in[0, 100911, 111148, 121385, 131623, 141860, 152097, 162335, 172572, 182809, 193047, 203284, 213522, 223759, 233996, 244234, 254471, 264708, 274946, 285183, 295420, 305658, 315895, 326132, 336370, 346607, 356845, 367082, 377319, 387557, 397794, 408031, 418269, 428506, 438743, 448981, 459218, 469455, 479693, 489930, 500168, 510405, 520642, 530880, 541117, 551354, 561592, 571829, 582066, 592304, 602541, 612778, 623016, 633253, 643491, 653728, 663965, 674203, 684440, 694677, 704915, 715152, 725389, 735627, 745864, 756101, 766339, 776576, 786814, 797051, 807288]]
    # 额外计算10次炫纹
    炫纹倍率 = 0
    炫纹次数 = 10
    CD = 58

    def 等效百分比(self, 武器类型):
        return int(self.攻击次数 * self.data0[self.等级]* self.倍率 + self.炫纹倍率 * self.炫纹次数)


class 技能26(被动技能):
    名称 = '太古之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)


class 技能27(主动技能):
    名称 = '太古星河·殒灭'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(x*1.179) for x in[0, 12582, 15499, 18417, 21334, 24253, 27170, 30087, 33005, 35922, 38840, 41757, 44676, 47593, 50511, 53428, 56345, 59263, 62181, 65099, 68016, 70934, 73851, 76769, 79687, 82604, 85522, 88439, 91357, 94274, 97193, 100110, 103028, 105945, 108862, 111780, 114698, 117616, 120533, 123451, 126368, 129286, 132203, 135121, 138039, 140956, 143874, 146791, 149709, 152627, 155545, 158462, 161379, 164297, 167214, 170133, 173050, 175968, 178885, 181803, 184720, 187638, 190556, 193473, 196391, 199308, 202226, 205144, 208062, 210979, 213896]]
    攻击次数 = 4
    data1 = [int(x*1.179) for x in[0, 10066, 12399, 14733, 17067, 19401, 21736, 24070, 26404, 28738, 31072, 33406, 35740, 38075, 40409, 42743, 45076, 47410, 49744, 52079, 54413, 56747, 59081, 61415, 63749, 66083, 68418, 70752, 73086, 75420, 77753, 80087, 82422, 84756, 87090, 89424, 91758, 94092, 96426, 98761, 101095, 103429, 105763, 108097, 110430, 112765, 115099, 117433, 119767, 122101, 124435, 126769, 129104, 131438, 133772, 136106, 138440, 140774, 143108, 145442, 147776, 150110, 152444, 154778, 157112, 159447, 161781, 164115, 166449, 168783, 171117]]
    攻击次数2 = 5
    data2 = [int(x*1.179) for x in[0, 50329, 61998, 73669, 85339, 97010, 108681, 120350, 132021, 143692, 155362, 167032, 178703, 190373, 202044, 213714, 225384, 237055, 248725, 260396, 272066, 283736, 295407, 307078, 318747, 330418, 342089, 353759, 365430, 377100, 388770, 400441, 412112, 423781, 435452, 447122, 458793, 470464, 482133, 493804, 505475, 517145, 528815, 540486, 552156, 563827, 575498, 587167, 598838, 610508, 622179, 633849, 645519, 657190, 668861, 680530, 692201, 703872, 715542, 727213, 738883, 750553, 762224, 773894, 785564, 797235, 808905, 820576, 832247, 843916, 855587]]
    攻击次数3 = 1
    data3 = [int(x*1.179) for x in[0, 33552, 41332, 49113, 56893, 64673, 72453, 80234, 88014, 95794, 103574, 111355, 119135, 126916, 134695, 142476, 150256, 158037, 165816, 173597, 181377, 189158, 196937, 204718, 212498, 220279, 228059, 235839, 243620, 251400, 259180, 266960, 274741, 282521, 290302, 298081, 305862, 313642, 321423, 329202, 336983, 344763, 352544, 360323, 368104, 375884, 383665, 391444, 399225, 407005, 414786, 422565, 430346, 438126, 445907, 453687, 461467, 469248, 477028, 484809, 492588, 500369, 508149, 515930, 523709, 531490, 539270, 547051, 554830, 562611, 570391]]
    攻击次数4 = 1
    data4 = [int(x*1.179) for x in[0, 10066, 12399, 14733, 17067, 19401, 21736, 24070, 26404, 28738, 31072, 33406, 35740, 38075, 40409, 42743, 45076, 47410, 49744, 52079, 54413, 56747, 59081, 61415, 63749, 66083, 68418, 70752, 73086, 75420, 77753, 80087, 82422, 84756, 87090, 89424, 91758, 94092, 96426, 98761, 101095, 103429, 105763, 108097, 110430, 112765, 115099, 117433, 119767, 122101, 124435, 126769, 129104, 131438, 133772, 136106, 138440, 140774, 143108, 145442, 147776, 150110, 152444, 154778, 157112, 159447, 161781, 164115, 166449, 168783, 171117]]
    攻击次数5 = 15
    # 基础 = 9665*4 + 7733*5 + 38660 + 25772 + 7733*15
    # 成长 = 2917*4 + 2333*5 + 11669 + 7780 + 2333*15
    CD = 290
    演出时间 = 5

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        return int((self.攻击次数 * self.data0[self.等级]
        +self.攻击次数2 * self.data1[self.等级]
        +self.攻击次数3 * self.data2[self.等级]
        +self.攻击次数4 * self.data3[self.等级]
        +self.攻击次数5 * self.data4[self.等级]
        )* self.倍率)


class 技能28(主动技能):
    名称 = '基本攻击'
    备注 = '(一轮,TP为基础精通)'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    基础 = 225.2*2.662/1.115*1.1
    基础2 = 1.16 * 225.2*2.662/1.115*1.1
    基础3 = 1.8 * 225.2*2.662/1.115*1.1
    CD = 1
    TP成长 = 0.10
    TP上限 = 3


class 技能29(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['基本攻击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能'+str(i)+'())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

知源·战斗法师一觉序号 = 15
知源·战斗法师二觉序号 = 0
知源·战斗法师三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 85:
        知源·战斗法师二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        知源·战斗法师三觉序号 = 技能序号[i.名称]

知源·战斗法师护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·战斗法师护石选项.append(i.名称)

知源·战斗法师符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·战斗法师符文选项.append(i.名称)


class 知源·战斗法师角色属性(角色属性):

    实际名称 = '知源·战斗法师'
    角色 = '魔法师(女)'
    职业 = '战斗法师'

    武器选项 = ['矛', '棍棒']

    类型选择 = ['物理百分比', '魔法百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量', '智力']

    主BUFF = 1.790

    远古记忆 = 0

    碎霸触发概率 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        if self.武器类型 == '矛':
            self.技能栏[self.技能序号['棍棒精通']].关联技能 = ['无']
        elif self.武器类型 == '棍棒':
            self.技能栏[self.技能序号['矛精通']].关联技能 = ['无']
        for i in [16, 17, 18]:
            self.技能栏[i].等级 = self.技能栏[15].等级
        if self.装备栏[11] == '歼灵灭魂矛':
            self.技能栏[self.技能序号['碎霸']].触发概率 = self.碎霸触发概率
        super().被动倍率计算()
        self.技能栏[self.技能序号['炫纹之源：太古神光']
                 ].炫纹倍率 = self.技能栏[self.技能序号['炫纹发射']].等效百分比(self.武器类型)

    def 站街力量(self):
        return int(max(self.力量, self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        return max(super().面板力量(), super().面板智力())

    def 面板智力(self):
        return self.面板力量()

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if '/CD' in self.次数输入[self.技能序号[i.名称]]:
                    技能释放次数.append(int((self.时间输入 - i.演出时间) /
                                  i.等效CD(self.武器类型, self.类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(round(float(self.次数输入[self.技能序号[i.名称]]), 2))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '闪击碎霸' in [self.护石第一栏, self.护石第二栏, self.护石第三栏]:
            技能释放次数[self.技能序号['碎霸']] += 技能释放次数[self.技能序号['闪击碎霸']]

        return self.技能释放次数解析(技能释放次数)

    def 武器基础(self):
        temp = equ.get_equ_by_name(self.装备栏[11])

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.物理攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级, temp.品质,
                               self.强化等级[11], self.武器类型, '物理')
            self.魔法攻击力 += 武器计算(temp.等级, temp.品质,
                               self.强化等级[11], self.武器类型, '物理')
            self.独立攻击力 += 锻造计算(temp.等级, temp.品质, self.武器锻造等级)


class 知源·战斗法师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·战斗法师角色属性()
        self.角色属性A = 知源·战斗法师角色属性()
        self.角色属性B = 知源·战斗法师角色属性()
        self.一觉序号 = 知源·战斗法师一觉序号
        self.二觉序号 = 知源·战斗法师二觉序号
        self.三觉序号 = 知源·战斗法师三觉序号
        self.护石选项 = deepcopy(知源·战斗法师护石选项)
        self.符文选项 = deepcopy(知源·战斗法师符文选项)

    def 界面(self):
        super().界面()
        self.碎霸概率 = MyQComboBox(self.main_frame2)
        self.碎霸概率.resize(130, 20)
        self.碎霸概率.move(320, 450)
        for i in range(11):
            self.碎霸概率.addItem('歼灵灭魂矛：' + str(i * 10) + '%')
        self.碎霸概率.setCurrentIndex(1)

        self.职业存档.append(('碎霸概率', self.碎霸概率, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        属性.碎霸触发概率 = round(self.碎霸概率.currentIndex() / 10, 2)
