from math import *
from PublicReference.carry.base import *

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '图腾':
#             return round(self.CD / self.恢复 * 0.9, 1)
#         if 武器类型 == '镰刀':
#             return round(self.CD / self.恢复 * 0.95, 1)
#         if 武器类型 == '战斧':
#             return round(self.CD / self.恢复 * 1.1, 1)
#         if 武器类型 == '十字架':
#             return round(self.CD / self.恢复 * 1, 1)
#         if 武器类型 == '念珠':
#             return round(self.CD / self.恢复 * 0.95, 1)

class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数5
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数6
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数7
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能0(职业主动技能):
    名称 = '直拳冲击'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    #第一击和第二击物理攻击力：<data0>%
    data0 = [0, 273, 300, 328, 356, 384, 411, 439, 467, 495, 522, 550, 578, 605, 633, 661, 689, 716, 744, 772, 799, 827, 855, 883, 910, 938, 966, 993, 1021, 1049, 1077, 1104, 1132, 1160, 1188, 1215, 1243, 1271, 1298, 1326, 1354, 1382, 1409, 1437, 1465, 1492, 1520, 1548, 1576, 1603, 1631, 1659, 1686, 1714, 1742, 1770, 1797, 1825, 1853, 1881, 1908, 1936, 1964, 1991, 2019, 2047, 2075, 2102, 2130, 2158, 2185]
    攻击次数 = 2
    #最后一击物理攻击力：<data1>%
    data1 = [0, 819, 902, 986, 1069, 1152, 1235, 1318, 1401, 1485, 1568, 1651, 1734, 1817, 1900, 1983, 2067, 2150, 2233, 2316, 2399, 2482, 2566, 2649, 2732, 2815, 2898, 2981, 3065, 3148, 3231, 3314, 3397, 3480, 3564, 3647, 3730, 3813, 3896, 3979, 4062, 4146, 4229, 4312, 4395, 4478, 4561, 4645, 4728, 4811, 4894, 4977, 5060, 5144, 5227, 5310, 5393, 5476, 5559, 5643, 5726, 5809, 5892, 5975, 6058, 6141, 6225, 6308, 6391, 6474, 6557]
    攻击次数2 = 1
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 5


class 技能1(被动技能):
    名称 = '意念驱动'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    是否主动 = 1
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['泯灭神击','制裁：怒火疾风','正义执行：雷米迪奥斯的圣座']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.013 + 0.02 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '图腾':
            return 0.9
        else:
            return 1.0


class 技能2(被动技能):
    名称 = '技巧精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能2 = ['俯冲直拳','俯冲腹拳','俯冲翔拳']
    关联技能3 = ['圣拳连击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(1.10 + 0.015 * (self.等级 - 10), 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03, 5)

class 技能3(职业主动技能):
    名称 = '圣拳锤击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 43
    # 直接攻击物理攻击力：<int>%
    data0 = [0, 269, 296, 323, 351, 378, 405, 433, 460, 487, 515, 542, 569, 597, 624, 651, 679, 706, 733, 761, 788, 815, 843, 870, 897, 925, 952, 979, 1007, 1034, 1061, 1089, 1116, 1143, 1171, 1198, 1225, 1252, 1280, 1307, 1334, 1362, 1389, 1416, 1444, 1471, 1498, 1526, 1553, 1580, 1608, 1635, 1662, 1690, 1717, 1744, 1772, 1799, 1826, 1854, 1881, 1908, 1936, 1963, 1990, 2018, 2045, 2072, 2099, 2127, 2154]
    # 冲击波攻击力：<int>%
    data1 = [0, 2423, 2669, 2915, 3161, 3407, 3653, 3899, 4145, 4391, 4637, 4883, 5128, 5374, 5620, 5866, 6112, 6358, 6604, 6850, 7096, 7342, 7588, 7834, 8079, 8325, 8571, 8817, 9063, 9309, 9555, 9801, 10047, 10293, 10539, 10784, 11030, 11276, 11522, 11768, 12014, 12260, 12506, 12752, 12998, 13244, 13489, 13735, 13981, 14227, 14473, 14719, 14965, 15211, 15457, 15703, 15949, 16194, 16440, 16686, 16932, 17178, 17424, 17670, 17916, 18162, 18408, 18654, 18899, 19145, 19391]
    攻击次数2 = 1
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 5


class 技能4(职业主动技能):
    名称 = '俯冲翔拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1501.3778 * 1.1 * 1.169
    # 成长 = 169.2222 * 1.1 * 1.169
    #物理攻击力：<data0>%
    data0 = [int(i*1.255) for i in [0, 1954, 2152, 2350, 2548, 2747, 2945, 3143, 3341, 3540, 3738, 3936, 4134, 4333, 4531, 4729, 4927, 5126, 5324, 5522, 5720, 5919, 6117, 6315, 6513, 6712, 6910, 7108, 7306, 7504, 7703, 7901, 8099, 8297, 8496, 8694, 8892, 9090, 9289, 9487, 9685, 9883, 10082, 10280, 10478, 10676, 10875, 11073, 11271, 11469, 11668, 11866, 12064, 12262, 12461, 12659, 12857, 13055, 13254, 13452, 13650, 13848, 14047, 14245, 14443, 14641, 14840, 15038, 15236, 15434, 15633]]
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 5


class 技能5(职业主动技能):
    名称 = '俯冲直拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1492.4667 * 1.1 * 1.173
    # 成长 = 168.5333 * 1.1 * 1.173
    #物理攻击力：<data0>%
    data0 = [int(x*1.256) for x in [0, 1949, 2146, 2344, 2542, 2740, 2937, 3135, 3333, 3530, 3728, 3926, 4124, 4321, 4519, 4717, 4915, 5112, 5310, 5508, 5706, 5903, 6101, 6299, 6496, 6694, 6892, 7090, 7287, 7485, 7683, 7881, 8078, 8276, 8474, 8672, 8869, 9067, 9265, 9462, 9660, 9858, 10056, 10253, 10451, 10649, 10847, 11044, 11242, 11440, 11638, 11835, 12033, 12231, 12428, 12626, 12824, 13022, 13219, 13417, 13615, 13813, 14010, 14208, 14406, 14604, 14801, 14999, 15197, 15394, 15592]]
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 5


class 技能6(职业主动技能):
    名称 = '俯冲腹拳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 基础 = 1630.0238 * 1.1 * 1.151
    # 成长 = 183.9761 * 1.1 * 1.151
    # 物理攻击力：<data0>%
    data0 = [int(x*1.256) for x in [0, 2088, 2300, 2511, 2723, 2935, 3147, 3359, 3571, 3783, 3994, 4206, 4418, 4630, 4842, 5054, 5265, 5477, 5689, 5901, 6113, 6325, 6537, 6748, 6960, 7172, 7384, 7596, 7808, 8020, 8231, 8443, 8655, 8867, 9079, 9291, 9502, 9714, 9926, 10138, 10350, 10562, 10774, 10985, 11197, 11409, 11621, 11833, 12045, 12257, 12468, 12680, 12892, 13104, 13316, 13528, 13739, 13951, 14163, 14375, 14587, 14799, 15011, 15222, 15434, 15646, 15858, 16070, 16282, 16494, 16705]]
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 5

    def 神圣反击百分比(self):
        # 神圣反击倍率与腹拳一样，但在修炼场手动开只有80%
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * 0.8


class 技能7(职业主动技能):
    名称 = '瞬拳'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.255) for i in [0, 2098, 2311, 2524, 2737, 2950, 3163, 3376, 3589, 3802, 4015, 4228, 4441, 4654, 4867, 5080, 5293, 5505, 5718, 5931, 6144, 6357, 6570, 6783, 6996, 7209, 7422, 7635, 7848, 8061, 8274, 8487, 8700, 8912, 9125, 9338, 9551, 9764, 9977, 10190, 10403, 10616, 10829, 11042, 11255, 11468, 11681, 11894, 12107, 12320, 12532, 12745, 12958, 13171, 13384, 13597, 13810, 14023, 14236, 14449, 14662, 14875, 15088, 15301, 15514, 15727, 15939, 16152, 16365, 16578, 16791]]
    data1 = [int(i*1.255) for i in [0, 524, 577, 631, 684, 737, 790, 844, 897, 950, 1003, 1057, 1110, 1163, 1216, 1270, 1323, 1376, 1429, 1482, 1536, 1589, 1642, 1695, 1749, 1802, 1855, 1908, 1962, 2015, 2068, 2121, 2175, 2228, 2281, 2334, 2387, 2441, 2494, 2547, 2600, 2654, 2707, 2760, 2813, 2867, 2920, 2973, 3026, 3080, 3133, 3186, 3239, 3292, 3346, 3399, 3452, 3505, 3559, 3612, 3665, 3718, 3772, 3825, 3878, 3931, 3984, 4038, 4091, 4144, 4197]]
    # 基础 = 1667.6 * 1.13
    # 成长 = 188.4 * 1.13
    # 基础2 = 416.925 * 1.13
    # 成长2 = 47.075 * 1.13
    攻击次数2 = 1
    CD = 4
    TP成长 = 0.10
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '圣拳连击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 刺拳物理攻击力：<data0>%
    data0 = [int(i*1.2554) for i in [0, 1050, 1156, 1263, 1369, 1476, 1582, 1689, 1796, 1902, 2009, 2115, 2222, 2328, 2435, 2541, 2648, 2754, 2861, 2968, 3074, 3181, 3287, 3394, 3500, 3607, 3713, 3820, 3926, 4033, 4140, 4246, 4353, 4459, 4566, 4672, 4779, 4885, 4992, 5098, 5205, 5312, 5418, 5525, 5631, 5738, 5844, 5951, 6057, 6164, 6270, 6377, 6484, 6590, 6697, 6803, 6910, 7016, 7123, 7229, 7336, 7442, 7549, 7655, 7762, 7869, 7975, 8082, 8188, 8295, 8401]]
    # 直拳物理攻击力：<data1>%
    data1 = [int(i*1.2554) for i in [0, 1283, 1413, 1544, 1674, 1804, 1934, 2064, 2195, 2325, 2455, 2585, 2716, 2846, 2976, 3106, 3236, 3367, 3497, 3627, 3757, 3888, 4018, 4148, 4278, 4408, 4539, 4669, 4799, 4929, 5060, 5190, 5320, 5450, 5580, 5711, 5841, 5971, 6101, 6232, 6362, 6492, 6622, 6752, 6883, 7013, 7143, 7273, 7404, 7534, 7664, 7794, 7924, 8055, 8185, 8315, 8445, 8575, 8706, 8836, 8966, 9096, 9227, 9357, 9487, 9617, 9747, 9878, 10008, 10138, 10268]]
    # 摆拳物理攻击力：<data2>%
    data2 = [int(i*1.2554) for i in [0, 1555, 1713, 1871, 2029, 2187, 2345, 2502, 2660, 2818, 2976, 3134, 3292, 3450, 3607, 3765, 3923, 4081, 4239, 4397, 4554, 4712, 4870, 5028, 5186, 5344, 5501, 5659, 5817, 5975, 6133, 6291, 6449, 6606, 6764, 6922, 7080, 7238, 7396, 7553, 7711, 7869, 8027, 8185, 8343, 8501, 8658, 8816, 8974, 9132, 9290, 9448, 9605, 9763, 9921, 10079, 10237, 10395, 10552, 10710, 10868, 11026, 11184, 11342, 11500, 11657, 11815, 11973, 12131, 12289, 12447]]
    攻击次数2 = 1
    攻击次数3 = 1
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = '神圣反击'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1
    俯冲腹拳倍率 = 0
    CD = 6
    def 等效百分比(self, 武器类型):
        return (self.俯冲腹拳倍率+self.TP等级*303)*self.倍率


class 技能10(职业主动技能):
    名称 = '破碎之锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #物理攻击力：<data0>%
    data0 = [int(i*1.232) for i in [0, 2634, 2902, 3169, 3436, 3704, 3971, 4238, 4505, 4773, 5040, 5307, 5575, 5842, 6109, 6377, 6644, 6911, 7178, 7446, 7713, 7980, 8248, 8515, 8782, 9050, 9317, 9584, 9851, 10119, 10386, 10653, 10921, 11188, 11455, 11723, 11990, 12257, 12524, 12792, 13059, 13326, 13594, 13861, 14128, 14396, 14663, 14930, 15197, 15465, 15732, 15999, 16267, 16534, 16801, 17069, 17336, 17603, 17870, 18138, 18405, 18672, 18940, 19207, 19474, 19742, 20009, 20276, 20543, 20811, 21078]]
    #冲击波物理攻击力：<data1>
    data1 = [int(i*1.232) for i in [0, 1756, 1934, 2112, 2291, 2469, 2647, 2825, 3003, 3182, 3360, 3538, 3716, 3894, 4073, 4251, 4429, 4607, 4785, 4964, 5142, 5320, 5498, 5676, 5855, 6033, 6211, 6389, 6567, 6746, 6924, 7102, 7280, 7458, 7637, 7815, 7993, 8171, 8349, 8528, 8706, 8884, 9062, 9240, 9419, 9597, 9775, 9953, 10131, 10310, 10488, 10666, 10844, 11022, 11201, 11379, 11557, 11735, 11913, 12092, 12270, 12448, 12626, 12804, 12983, 13161, 13339, 13517, 13695, 13874, 14052]]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5


class 技能11(职业主动技能):
    名称 = '旋涡重拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 旋转多段攻击力：<int>% x 10
    data0 = [int(i*1.256) for i in [0, 474, 522, 571, 619, 667, 715, 763, 811, 860, 908, 956, 1004, 1052, 1100, 1149, 1197, 1245, 1293, 1341, 1389, 1438, 1486, 1534, 1582, 1630, 1678, 1726, 1775, 1823, 1871, 1919, 1967, 2015, 2064, 2112, 2160, 2208, 2256, 2304, 2353, 2401, 2449, 2497, 2545, 2593, 2642, 2690, 2738, 2786, 2834, 2882, 2931, 2979, 3027, 3075, 3123, 3171, 3220, 3268, 3316, 3364, 3412, 3460, 3509, 3557, 3605, 3653, 3701, 3749, 3797]]
    攻击次数 = 10
    # 最后一击攻击力：<int>%
    data1 = [int(i*1.256) for i in [0, 7121, 7843, 8566, 9288, 10010, 10733, 11455, 12178, 12900, 13623, 14345, 15068, 15790, 16512, 17235, 17957, 18680, 19402, 20125, 20847, 21570, 22292, 23014, 23737, 24459, 25182, 25904, 26627, 27349, 28072, 28794, 29516, 30239, 30961, 31684, 32406, 33129, 33851, 34574, 35296, 36018, 36741, 37463, 38186, 38908, 39631, 40353, 41076, 41798, 42520, 43243, 43965, 44688, 45410, 46133, 46855, 47578, 48300, 49022, 49745, 50467, 51190, 51912, 52635, 53357, 54079, 54802, 55524, 56247, 56969]]
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(x*1.4) for x in self.data0]
            self.data1 = [int(x*1.2) for x in self.data1]
        elif x == 1:
            self.data0 = [int(x*1.4) for x in self.data0]
            self.data1 = [int(x*1.35) for x in self.data1]


class 技能12(职业主动技能):
    名称 = '刺拳猛击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #刺拳连击物理攻击力：<data0>%
    data0 = [int(i*1.2565) for i in [0, 483, 532, 581, 630, 679, 728, 777, 826, 875, 924, 973, 1023, 1072, 1121, 1170, 1219, 1268, 1317, 1366, 1415, 1464, 1513, 1562, 1611, 1660, 1709, 1758, 1807, 1856, 1905, 1954, 2004, 2053, 2102, 2151, 2200, 2249, 2298, 2347, 2396, 2445, 2494, 2543, 2592, 2641, 2690, 2739, 2788, 2837, 2886, 2935, 2984, 3034, 3083, 3132, 3181, 3230, 3279, 3328, 3377, 3426, 3475, 3524, 3573, 3622, 3671, 3720, 3769, 3818, 3867]]
    #最后锤击物理攻击力：<data1>%
    data1 = [int(i*1.2565) for i in [0, 1443, 1589, 1736, 1882, 2028, 2175, 2321, 2468, 2614, 2760, 2907, 3053, 3200, 3346, 3493, 3639, 3785, 3932, 4078, 4225, 4371, 4517, 4664, 4810, 4957, 5103, 5250, 5396, 5542, 5689, 5835, 5982, 6128, 6274, 6421, 6567, 6714, 6860, 7007, 7153, 7299, 7446, 7592, 7739, 7885, 8031, 8178, 8324, 8471, 8617, 8764, 8910, 9056, 9203, 9349, 9496, 9642, 9788, 9935, 10081, 10228, 10374, 10521, 10667, 10813, 10960, 11106, 11253, 11399, 11545]]
    #追击攻击物理攻击力：<data2>%
    data2 = [int(i*1.2565) for i in [0, 938, 1033, 1128, 1223, 1318, 1413, 1509, 1604, 1699, 1794, 1889, 1984, 2080, 2175, 2270, 2365, 2460, 2555, 2651, 2746, 2841, 2936, 3031, 3127, 3222, 3317, 3412, 3507, 3602, 3698, 3793, 3888, 3983, 4078, 4173, 4269, 4364, 4459, 4554, 4649, 4744, 4840, 4935, 5030, 5125, 5220, 5315, 5411, 5506, 5601, 5696, 5791, 5886, 5982, 6077, 6172, 6267, 6362, 6457, 6553, 6648, 6743, 6838, 6933, 7028, 7124, 7219, 7314, 7409, 7504]]
    攻击次数 = 10
    攻击次数2 = 1
    攻击次数3 = 1
    CD = 10
    TP成长 = 0
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * (self.攻击次数 + self.TP等级)
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级)
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级)
        return 等效倍率 * self.倍率

class 技能13(职业主动技能):
    名称 = '神圣组合拳'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    #第一击物理攻击力：<data0>%
    data0 = [int(i*1.255) for i in [0, 2600, 2864, 3127, 3391, 3655, 3919, 4183, 4446, 4710, 4974, 5238, 5502, 5765, 6029, 6293, 6557, 6821, 7085, 7348, 7612, 7876, 8140, 8404, 8667, 8931, 9195, 9459, 9723, 9986, 10250, 10514, 10778, 11042, 11305, 11569, 11833, 12097, 12361, 12624, 12888, 13152, 13416, 13680, 13943, 14207, 14471, 14735, 14999, 15262, 15526, 15790, 16054, 16318, 16581, 16845, 17109, 17373, 17637, 17900, 18164, 18428, 18692, 18956, 19219, 19483, 19747, 20011, 20275, 20539, 20802]]
    #第二击物理攻击力：<data1>%
    data1 = [int(i*1.255) for i in [0, 3391, 3735, 4079, 4424, 4768, 5112, 5456, 5800, 6144, 6488, 6832, 7176, 7520, 7864, 8209, 8553, 8897, 9241, 9585, 9929, 10273, 10617, 10961, 11305, 11649, 11994, 12338, 12682, 13026, 13370, 13714, 14058, 14402, 14746, 15090, 15434, 15779, 16123, 16467, 16811, 17155, 17499, 17843, 18187, 18531, 18875, 19219, 19564, 19908, 20252, 20596, 20940, 21284, 21628, 21972, 22316, 22660, 23005, 23349, 23693, 24037, 24381, 24725, 25069, 25413, 25757, 26101, 26445, 26790, 27134]]
    #第三击物理攻击力：<data2>%
    data2 = [int(i*1.255) for i in [0, 5313, 5852, 6391, 6930, 7470, 8009, 8548, 9087, 9626, 10165, 10704, 11243, 11782, 12321, 12860, 13399, 13939, 14478, 15017, 15556, 16095, 16634, 17173, 17712, 18251, 18790, 19329, 19868, 20407, 20947, 21486, 22025, 22564, 23103, 23642, 24181, 24720, 25259, 25798, 26337, 26876, 27415, 27955, 28494, 29033, 29572, 30111, 30650, 31189, 31728, 32267, 32806, 33345, 33884, 34423, 34963, 35502, 36041, 36580, 37119, 37658, 38197, 38736, 39275, 39814, 40353, 40892, 41431, 41971, 42510]]
    攻击次数2 = 1
    攻击次数3 = 1
    CD = 16
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.17
        elif x == 1:
            self.倍率 *= 1.26


class 技能14(职业主动技能):
    名称 = '极速飓风拳'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    #摆拳物理攻击力：<data0>%
    data0 = [int(i*1.2558) for i in [0, 1747, 1924, 2101, 2278, 2455, 2633, 2810, 2987, 3164, 3342, 3519, 3696, 3873, 4051, 4228, 4405, 4582, 4759, 4937, 5114, 5291, 5468, 5646, 5823, 6000, 6177, 6355, 6532, 6709, 6886, 7064, 7241, 7418, 7595, 7772, 7950, 8127, 8304, 8481, 8659, 8836, 9013, 9190, 9368, 9545, 9722, 9899, 10077, 10254, 10431, 10608, 10785, 10963, 11140, 11317, 11494, 11672, 11849, 12026, 12203, 12381, 12558, 12735, 12912, 13089, 13267, 13444, 13621, 13798, 13976]]
    #上勾拳物理攻击力：<data1>%
    data1 = [int(i*1.2558) for i in [0, 7487, 8246, 9006, 9765, 10525, 11285, 12044, 12804, 13563, 14323, 15082, 15842, 16602, 17361, 18121, 18880, 19640, 20399, 21159, 21919, 22678, 23438, 24197, 24957, 25716, 26476, 27236, 27995, 28755, 29514, 30274, 31033, 31793, 32553, 33312, 34072, 34831, 35591, 36350, 37110, 37870, 38629, 39389, 40148, 40908, 41667, 42427, 43187, 43946, 44706, 45465, 46225, 46985, 47744, 48504, 49263, 50023, 50782, 51542, 52302, 53061, 53821, 54580, 55340, 56099, 56859, 57619, 58378, 59138, 59897]]
    攻击次数 = 10
    攻击次数2 = 1
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(x*0.97) for x in self.data0]
            self.攻击次数 = 6
            self.攻击次数2 = 0
            self.CD /=3
            self.基础释放次数 = 2
        elif x == 1:
            self.data0 = [int(x*1.04) for x in self.data0]
            self.攻击次数 = 6
            self.攻击次数2 = 0
            self.CD /=3
            self.基础释放次数 = 2


class 技能15(被动技能):
    名称 = '干涸之泉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能16(职业主动技能):
    名称 = '泯灭神击'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 不明的1.1
    #第1击物理攻击力：<data0>%
    data0 = [int(i*1.256) for i in [0, 6572, 8096, 9620, 11144, 12668, 14192, 15716, 17240, 18764, 20288, 21812, 23336, 24860, 26384, 27908, 29432, 30956, 32480, 34004, 35528, 37052, 38577, 40101, 41625, 43149, 44673, 46197, 47721, 49245, 50769, 52293, 53817, 55341, 56865, 58389, 59913, 61437, 62961, 64485, 66009, 67533, 69057, 70581, 72105, 73629, 75153, 76677, 78201, 79725, 81249, 82773, 84297, 85821, 87346, 88870, 90394, 91918, 93442, 94966, 96490, 98014, 99538, 101062, 102586, 104110, 105634, 107158, 108682, 110206, 111730]]
    #第2击物理攻击力：<data1>%
    data1 = [int(i*1.256) for i in [0, 10157, 12512, 14867, 17223, 19578, 21933, 24289, 26644, 28999, 31355, 33710, 36065, 38421, 40776, 43131, 45487, 47842, 50197, 52553, 54908, 57263, 59619, 61974, 64329, 66684, 69040, 71395, 73750, 76106, 78461, 80816, 83172, 85527, 87882, 90238, 92593, 94948, 97304, 99659, 102014, 104370, 106725, 109080, 111436, 113791, 116146, 118502, 120857, 123212, 125567, 127923, 130278, 132633, 134989, 137344, 139699, 142055, 144410, 146765, 149121, 151476, 153831, 156187, 158542, 160897, 163253, 165608, 167963, 170319, 172674]]
    攻击次数2 = 1
    #第3击物理攻击力：<data2>%
    data2 = [int(i*1.256) for i in [0, 13144, 16192, 19240, 22288, 25337, 28385, 31433, 34481, 37529, 40577, 43625, 46673, 49721, 52769, 55817, 58865, 61913, 64961, 68009, 71057, 74105, 77154, 80202, 83250, 86298, 89346, 92394, 95442, 98490, 101538, 104586, 107634, 110682, 113730, 116778, 119826, 122874, 125923, 128971, 132019, 135067, 138115, 141163, 144211, 147259, 150307, 153355, 156403, 159451, 162499, 165547, 168595, 171643, 174692, 177740, 180788, 183836, 186884, 189932, 192980, 196028, 199076, 202124, 205172, 208220, 211268, 214316, 217364, 220412, 223460]]
    攻击次数3 = 1
    #第4击物理攻击力：<data3>%
    data3 = [int(i*1.256) for i in [0, 29874, 36801, 43729, 50656, 57584, 64511, 71438, 78366, 85293, 92221, 99148, 106075, 113003, 119930, 126858, 133785, 140713, 147640, 154567, 161495, 168422, 175350, 182277, 189204, 196132, 203059, 209987, 216914, 223841, 230769, 237696, 244624, 251551, 258479, 265406, 272333, 279261, 286188, 293116, 300043, 306970, 313898, 320825, 327753, 334680, 341607, 348535, 355462, 362390, 369317, 376245, 383172, 390099, 397027, 403954, 410882, 417809, 424736, 431664, 438591, 445519, 452446, 459373, 466301, 473228, 480156, 487083, 494011, 500938, 507865]]
    攻击次数4 = 1
    # 不明的1.1
    # 倍率 = 1.1
    # 基础 = 40394 * 1.1 * 1.136
    # 成长 = 12198 * 1.1 * 1.136
    CD = 145.0

    def 等效百分比(self, 武器类型):
        if self.等级 >= 9:
            self.倍率 *= 1.1
        return super().等效百分比(武器类型)



class 技能17(职业主动技能):
    名称 = '破碎之拳'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    #连续物理攻击力：<data0>%
    data0 = [int(i*1.255) for i in [0, 1576, 1736, 1896, 2056, 2216, 2375, 2535, 2695, 2855, 3015, 3175, 3335, 3495, 3655, 3815, 3975, 4135, 4295, 4454, 4614, 4774, 4934, 5094, 5254, 5414, 5574, 5734, 5894, 6054, 6214, 6373, 6533, 6693, 6853, 7013, 7173, 7333, 7493, 7653, 7813, 7973, 8133, 8293, 8452, 8612, 8772, 8932, 9092, 9252, 9412, 9572, 9732, 9892, 10052, 10212, 10372, 10531, 10691, 10851, 11011, 11171, 11331, 11491, 11651, 11811, 11971, 12131, 12291, 12450, 12610]]
    攻击次数 = 10
    #最后下勾拳物理攻击：<data1>%
    data1 = [int(i*1.255) for i in [0, 3940, 4340, 4740, 5140, 5540, 5939, 6339, 6739, 7139, 7539, 7938, 8338, 8738, 9138, 9538, 9937, 10337, 10737, 11137, 11537, 11936, 12336, 12736, 13136, 13536, 13935, 14335, 14735, 15135, 15535, 15934, 16334, 16734, 17134, 17534, 17933, 18333, 18733, 19133, 19533, 19932, 20332, 20732, 21132, 21532, 21931, 22331, 22731, 23131, 23531, 23931, 24330, 24730, 25130, 25530, 25930, 26329, 26729, 27129, 27529, 27929, 28328, 28728, 29128, 29528, 29928, 30327, 30727, 31127, 31527]]
    #爆炸物理攻击力：<data2>%
    data2 = [int(i*1.255) for i in [0, 6568, 7234, 7900, 8567, 9233, 9899, 10566, 11232, 11898, 12565, 13231, 13897, 14564, 15230, 15896, 16563, 17229, 17895, 18562, 19228, 19894, 20561, 21227, 21893, 22560, 23226, 23892, 24559, 25225, 25891, 26558, 27224, 27890, 28557, 29223, 29889, 30556, 31222, 31888, 32555, 33221, 33887, 34554, 35220, 35886, 36553, 37219, 37885, 38552, 39218, 39885, 40551, 41217, 41884, 42550, 43216, 43883, 44549, 45215, 45882, 46548, 47214, 47881, 48547, 49213, 49880, 50546, 51212, 51879, 52545]]
    # 基础 = 12525.9091 * 1.13
    # 成长 = 1414.0909 * 1.13
    # 基础2 = 3131.3636 * 1.13
    # 成长2 = 353.6363 * 1.13
    攻击次数2 = 1
    # 基础3 = 5218.6363 * 1.13
    # 成长3 = 589.3636 * 1.13
    攻击次数3 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(1.3*x) for x in self.data0]
            self.data2 = [int(1.28*x) for x in self.data2]
            self.CD *= 0.88
        elif x == 1:
            self.data0 = [int(1.3*x) for x in self.data0]
            self.data2 = [int(1.78*x) for x in self.data2]
            self.CD *= 0.88


class 技能18(职业主动技能):
    名称 = '破坏之拳'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    #物理攻击力：<data0>%
    data0 = [int(x*1.2563) for x in [0, 29387, 32368, 35350, 38331, 41312, 44294, 47275, 50256, 53238, 56219, 59200, 62182, 65163, 68144, 71126, 74107, 77088, 80070, 83051, 86032, 89014, 91995, 94976, 97958, 100939, 103920, 106902, 109883, 112864, 115846, 118827, 121808, 124790, 127771, 130752, 133734, 136715, 139696, 142678, 145659, 148640, 151622, 154603, 157584, 160566, 163547, 166528, 169510, 172491, 175472, 178454, 181435, 184416, 187398, 190379, 193360, 196342, 199323, 202304, 205286, 208267, 211248, 214230, 217211, 220192, 223174, 226155, 229136, 232118, 235099]]
    #冲击波物理攻击力：<data1>%
    data1 = [int(x*1.2563) for x in [0, 3265, 3596, 3927, 4259, 4590, 4921, 5252, 5584, 5915, 6246, 6577, 6909, 7240, 7571, 7902, 8234, 8565, 8896, 9227, 9559, 9890, 10221, 10552, 10884, 11215, 11546, 11878, 12209, 12540, 12871, 13203, 13534, 13865, 14196, 14528, 14859, 15190, 15521, 15853, 16184, 16515, 16846, 17178, 17509, 17840, 18171, 18503, 18834, 19165, 19496, 19828, 20159, 20490, 20822, 21153, 21484, 21815, 22147, 22478, 22809, 23140, 23472, 23803, 24134, 24465, 24797, 25128, 25459, 25790, 26122]]
    攻击次数2 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *=1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
        elif x == 1:
            self.倍率 *=1.28

class 技能19(职业主动技能):
    名称 = '仲裁怒击'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    #物理攻击力：<data0>%
    data0 = [int(i*1.2557) for i in [0, 43904, 48358, 52812, 57266, 61720, 66174, 70629, 75083, 79537, 83991, 88445, 92899, 97353, 101807, 106261, 110715, 115169, 119623, 124078, 128532, 132986, 137440, 141894, 146348, 150802, 155256, 159710, 164164, 168618, 173072, 177527, 181981, 186435, 190889, 195343, 199797, 204251, 208705, 213159, 217613, 222067, 226521, 230976, 235430, 239884, 244338, 248792, 253246, 257700, 262154, 266608, 271062, 275516, 279970, 284425, 288879, 293333, 297787, 302241, 306695, 311149, 315603, 320057, 324511, 328965, 333419, 337874, 342328, 346782, 351236]]
    #冲击波物理攻击力：<data1>%
    data1 = [int(i*1.2557) for i in [0, 18816, 20725, 22634, 24542, 26451, 28360, 30269, 32178, 34087, 35996, 37905, 39814, 41722, 43631, 45540, 47449, 49358, 51267, 53176, 55085, 56994, 58902, 60811, 62720, 64629, 66538, 68447, 70356, 72265, 74174, 76083, 77991, 79900, 81809, 83718, 85627, 87536, 89445, 91354, 93263, 95171, 97080, 98989, 100898, 102807, 104716, 106625, 108534, 110443, 112351, 114260, 116169, 118078, 119987, 121896, 123805, 125714, 127623, 129532, 131440, 133349, 135258, 137167, 139076, 140985, 142894, 144803, 146712, 148620, 150529]]
    攻击次数2 =1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *=1.36
            # self.基础 *= 1.36
            # self.成长 *= 1.36


class 技能20(被动技能):
    名称 = '正义惩戒'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能21(职业主动技能):
    名称 = '超重拳'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(i*1.255) for i in [0, 14270, 15718, 17165, 18613, 20061, 21509, 22956, 24404, 25852, 27299, 28747, 30195, 31643, 33090, 34538, 35986, 37434, 38881, 40329, 41777, 43224, 44672, 46120, 47568, 49015, 50463, 51911, 53359, 54806, 56254, 57702, 59149, 60597, 62045, 63493, 64940, 66388, 67836, 69284, 70731, 72179, 73627, 75074, 76522, 77970, 79418, 80865, 82313, 83761, 85209, 86656, 88104, 89552, 90999, 92447, 93895, 95343, 96790, 98238, 99686, 101134, 102581, 104029, 105477, 106924, 108372, 109820, 111268, 112715, 114163]]
    data1 = [int(i*1.255) for i in [0, 57081, 62872, 68663, 74454, 80245, 86036, 91827, 97618, 103409, 109199, 114990, 120781, 126572, 132363, 138154, 143945, 149736, 155527, 161318, 167109, 172899, 178690, 184481, 190272, 196063, 201854, 207645, 213436, 219227, 225018, 230808, 236599, 242390, 248181, 253972, 259763, 265554, 271345, 277136, 282927, 288718, 294508, 300299, 306090, 311881, 317672, 323463, 329254, 335045, 340836, 346627, 352418, 358208, 363999, 369790, 375581, 381372, 387163, 392954, 398745, 404536, 410327, 416118, 421908, 427699, 433490, 439281, 445072, 450863, 456654]]
    攻击次数2 = 1
    基础 = 56623.16667 * 1.132
    成长 = 6392.83333 * 1.132
    CD = 50.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class 技能22(职业主动技能):
    名称 = '制裁：怒火疾风'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    #连续攻击物理攻击力：<data0>%
    data0 = [int(i*1.255) for i in [0, 3558, 4383, 5208, 6033, 6858, 7683, 8509, 9334, 10159, 10984, 11809, 12634, 13459, 14284, 15109, 15935, 16760, 17585, 18410, 19235, 20060, 20885, 21710, 22535, 23361, 24186, 25011, 25836, 26661, 27486, 28311, 29136, 29962, 30787, 31612, 32437, 33262, 34087, 34912, 35737, 36562, 37388, 38213, 39038, 39863, 40688, 41513, 42338, 43163, 43989, 44814, 45639, 46464, 47289, 48114, 48939, 49764, 50589, 51415, 52240, 53065, 53890, 54715, 55540, 56365, 57190, 58015, 58841, 59666, 60491]]
    攻击次数 = 19
    #最后一击物理攻击力：<data1>%
    data1 = [int(i*1.255) for i in [0, 5189, 6393, 7596, 8800, 10003, 11207, 12410, 13614, 14817, 16020, 17224, 18427, 19631, 20834, 22038, 23241, 24445, 25648, 26851, 28055, 29258, 30462, 31665, 32869, 34072, 35276, 36479, 37683, 38886, 40089, 41293, 42496, 43700, 44903, 46107, 47310, 48514, 49717, 50920, 52124, 53327, 54531, 55734, 56938, 58141, 59345, 60548, 61752, 62955, 64158, 65362, 66565, 67769, 68972, 70176, 71379, 72583, 73786, 74989, 76193, 77396, 78600, 79803, 81007, 82210, 83414, 84617, 85821, 87024, 88227]]
    攻击次数2 = 2
    #最后一击的爆炸物理攻击力：<data2>%
    data2 = [int(i*1.255) for i in [0, 78589, 96813, 115036, 133260, 151484, 169707, 187931, 206155, 224379, 242602, 260826, 279050, 297273, 315497, 333721, 351944, 370168, 388392, 406615, 424839, 443063, 461286, 479510, 497734, 515957, 534181, 552405, 570628, 588852, 607076, 625299, 643523, 661747, 679970, 698194, 716418, 734641, 752865, 771089, 789312, 807536, 825760, 843983, 862207, 880431, 898654, 916878, 935102, 953325, 971549, 989773, 1007997, 1026220, 1044444, 1062668, 1080891, 1099115, 1117339, 1135562, 1153786, 1172010, 1190233, 1208457, 1226681, 1244904, 1263128, 1281352, 1299575, 1317799, 1336023]]
    攻击次数3 = 1
    # 基础 = 100940 * 1.192
    # 成长 = 30458 * 1.192
    CD = 180.0


class 技能23(被动技能):
    名称 = '绝对正义'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能24(职业主动技能):
    名称 = '正义铁拳'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    # 下捶冲击波攻击力：<int>%
    data0 = [int(i*1.256) for i in [0, 22979, 25310, 27642, 29973, 32304, 34635, 36967, 39298, 41629, 43960, 46292, 48623, 50954, 53285, 55617, 57948, 60279, 62611, 64942, 67273, 69604, 71936, 74267, 76598, 78929, 81261, 83592, 85923, 88254, 90586, 92917, 95248, 97579, 99911, 102242, 104573, 106905, 109236, 111567, 113898, 116230, 118561, 120892, 123223, 125555, 127886, 130217, 132548, 134880, 137211, 139542, 141873, 144205, 146536, 148867, 151198, 153530, 155861, 158192, 160524, 162855, 165186, 167517, 169849, 172180, 174511, 176842, 179174, 181505, 183836]]
    # 连续攻击攻击力：<int>% x <int>
    data1 = [int(i*1.256) for i in [0, 1723, 1898, 2073, 2248, 2422, 2597, 2772, 2947, 3122, 3297, 3471, 3646, 3821, 3996, 4171, 4346, 4520, 4695, 4870, 5045, 5220, 5395, 5570, 5744, 5919, 6094, 6269, 6444, 6619, 6793, 6968, 7143, 7318, 7493, 7668, 7843, 8017, 8192, 8367, 8542, 8717, 8892, 9066, 9241, 9416, 9591, 9766, 9941, 10116, 10290, 10465, 10640, 10815, 10990, 11165, 11339, 11514, 11689, 11864, 12039, 12214, 12388, 12563, 12738, 12913, 13088, 13263, 13438, 13612, 13787]]
    # 最后勾拳攻击力：<int>%
    data2 = [int(i*1.256) for i in [0, 57448, 63277, 69105, 74933, 80761, 86589, 92417, 98246, 104074, 109902, 115730, 121558, 127386, 133214, 139043, 144871, 150699, 156527, 162355, 168183, 174012, 179840, 185668, 191496, 197324, 203152, 208980, 214809, 220637, 226465, 232293, 238121, 243949, 249778, 255606, 261434, 267262, 273090, 278918, 284746, 290575, 296403, 302231, 308059, 313887, 319715, 325544, 331372, 337200, 343028, 348856, 354684, 360512, 366341, 372169, 377997, 383825, 389653, 395481, 401310, 407138, 412966, 418794, 424622, 430450, 436278, 442107, 447935, 453763, 459591]]
    攻击次数2 = 20
    攻击次数3 = 1
    CD = 60.0


class 技能25(职业主动技能):
    名称 = '正义执行：雷米迪奥斯的圣座'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(i*1.256) for i in [0, 159960, 197052, 234144, 271237, 308329, 345421, 382513, 419606, 456698, 493790, 530882, 567975, 605067, 642159, 679251, 716343, 753436, 790528, 827620, 864712, 901805, 938897, 975989, 1013081, 1050174, 1087266, 1124358, 1161450, 1198543, 1235635, 1272727, 1309819, 1346912, 1384004, 1421096, 1458188, 1495281, 1532373, 1569465, 1606557, 1643650, 1680742, 1717834, 1754926, 1792019, 1829111, 1866203, 1903295, 1940388, 1977480, 2014572, 2051664, 2088757, 2125849, 2162941, 2200033, 2237126, 2274218, 2311310, 2348402, 2385495, 2422587, 2459679, 2496771, 2533864, 2570956, 2608048, 2645140, 2682233, 2719325]]
    data1 = [int(i*1.256) for i in [0, 239940, 295578, 351217, 406855, 462493, 518132, 573770, 629409, 685047, 740685, 796324, 851962, 907600, 963239, 1018877, 1074516, 1130154, 1185792, 1241431, 1297069, 1352707, 1408346, 1463984, 1519622, 1575261, 1630899, 1686538, 1742176, 1797814, 1853453, 1909091, 1964729, 2020368, 2076006, 2131645, 2187283, 2242921, 2298560, 2354198, 2409836, 2465475, 2521113, 2576751, 2632390, 2688028, 2743667, 2799305, 2854943, 2910582, 2966220, 3021858, 3077497, 3133135, 3188774, 3244412, 3300050, 3355689, 3411327, 3466965, 3522604, 3578242, 3633881, 3689519, 3745157, 3800796, 3856434, 3912072, 3967711, 4023349, 4078987]]

    # 基础 = 135155 / 1.1
    # 成长 = 40802 / 1.1
    # 基础2 = 202734 / 1.1
    # 成长2 = 61202 / 1.1
    攻击次数2 = 1
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


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

神启·蓝拳圣使一觉序号 = 0
神启·蓝拳圣使二觉序号 = 0
神启·蓝拳圣使三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        神启·蓝拳圣使一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        神启·蓝拳圣使二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        神启·蓝拳圣使三觉序号 = 技能序号[i.名称]

神启·蓝拳圣使护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        神启·蓝拳圣使护石选项.append(i.名称)

神启·蓝拳圣使符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        神启·蓝拳圣使符文选项.append(i.名称)


class 神启·蓝拳圣使角色属性(角色属性):

    实际名称 = '神启·蓝拳圣使'
    角色 = '圣职者(男)'
    职业 = '蓝拳圣使'

    武器选项 = ['图腾', '战斧', '镰刀', '念珠', '十字架']

    类型选择 = ['物理百分比']

    # 默认
    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.99

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        # 神圣反击倍率与腹拳一样，但在修炼场手动开只有80%
        self.技能栏[self.技能序号['神圣反击']].俯冲腹拳倍率 = self.技能栏[self.技能序号['俯冲腹拳']].神圣反击百分比()


class 神启·蓝拳圣使(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神启·蓝拳圣使角色属性()
        self.角色属性A = 神启·蓝拳圣使角色属性()
        self.角色属性B = 神启·蓝拳圣使角色属性()
        self.一觉序号 = 神启·蓝拳圣使一觉序号
        self.二觉序号 = 神启·蓝拳圣使二觉序号
        self.三觉序号 = 神启·蓝拳圣使三觉序号
        self.护石选项 = deepcopy(神启·蓝拳圣使护石选项)
        self.符文选项 = deepcopy(神启·蓝拳圣使符文选项)
