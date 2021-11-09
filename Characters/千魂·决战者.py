from PublicReference.carry.base import *


class 职业主动技能(主动技能):

    data0 = []
    data1 = []
    data2 = []
    data3 = []

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
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    # def 等效CD(self, 武器类型, 输出类型):
    #     # 长枪+5%,长枪精通-13%
    #     if self.所在等级 == 100 or self.所在等级 == 85 or self.所在等级 == 50:
    #         return round(self.CD / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)
    #     return round(self.CD * 0.87 / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)


class 技能0(被动技能):
    名称 = '长枪精通'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['流云幻灭','极影无形杀','问鼎·千军破云']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1 + 0.01 * self.等级, 5)
        else:
            return round(0.8 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.87

class 技能1(职业主动技能):
    名称 = '双重刺击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # #第1击攻击力：<data0>%
    # data0 = [0, 1695, 1868, 2040, 2211, 2383, 2556, 2728, 2900, 3071, 3244, 3416, 3588, 3760, 3932, 4104, 4276, 4449, 4621, 4792, 4964, 5137, 5309, 5481, 5652, 5825, 5997, 6169, 6340, 6513, 6685, 6857, 7029, 7201, 7373, 7545, 7717, 7890, 8061, 8233, 8405, 8578, 8750, 8921, 9094, 9266, 9438, 9610, 9782, 9954, 10126, 10298, 10471, 10642, 10814, 10986, 11159, 11331, 11502, 11674, 11847, 12019, 12190, 12362, 12535, 12707, 12879, 13050, 13223, 13395, 13567]
    # #第1击枪尾攻击力：<data1>%
    # data1 = [0, 1860, 2050, 2239, 2427, 2616, 2805, 2993, 3183, 3372, 3561, 3749, 3937, 4126, 4315, 4504, 4693, 4882, 5070, 5259, 5449, 5638, 5826, 6015, 6204, 6392, 6582, 6770, 6959, 7147, 7336, 7525, 7715, 7903, 8092, 8281, 8469, 8658, 8848, 9037, 9225, 9414, 9602, 9790, 9980, 10169, 10358, 10546, 10735, 10924, 11114, 11302, 11491, 11680, 11868, 12057, 12247, 12435, 12623, 12812, 13001, 13189, 13379, 13568, 13757, 13945, 14134, 14323, 14513, 14701, 14890]

    # 近距离攻击和枪尾攻击不会同时命中一个敌人， 判定重叠时， 会优先判定为枪尾攻击
    # 第2击攻击力：<data2>%
    data0 = [(i*1.1243) for i in [0, 1978, 2179, 2379, 2581, 2781, 2982, 3183, 3383, 3585, 3785, 3986, 4186, 4387, 4587, 4789, 4990, 5190, 5391, 5591, 5792, 5993, 6194, 6395, 6595, 6796, 6997, 7198, 7398, 7599, 7798, 7999, 8202, 8402, 8603, 8802, 9003, 9205, 9406, 9605, 9806, 10007, 10207, 10409, 10609, 10810, 11010, 11211, 11411, 11613, 11814, 12014, 12215, 12415, 12617, 12817, 13018, 13218, 13419, 13620, 13821, 14022, 14222, 14423, 14623, 14824, 15026, 15226, 15427, 15627, 15828]]
    # 第2击枪尾攻击力：<data3>%
    data1 = [(i*1.1243) for i in [0, 2365, 2604, 2846, 3086, 3325, 3566, 3805, 4045, 4284, 4526, 4765, 5005, 5246, 5485, 5725, 5965, 6206, 6445, 6684, 6926, 7165, 7405, 7646, 7886, 8125, 8365, 8606, 8845, 9085, 9326, 9566, 9805, 10045, 10285, 10525, 10765, 11006, 11246, 11485, 11725, 11965, 12204, 12447, 12686, 12926, 13165, 13405, 13645, 13884, 14127, 14366, 14606, 14846, 15085, 15325, 15564, 15806, 16046, 16286, 16526, 16765, 17005, 17246, 17486, 17725, 17966, 18206, 18445, 18685, 18926]]
    攻击次数2 = 1
    # 基础 = 3694.57142857143
    # 成长 = 417.428571428571
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5


class 技能2(职业主动技能):
    名称 = '行云：风'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 稍稍对不上
    # 刺击攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 158, 174, 189, 206, 222, 238, 254, 270, 286, 302, 318, 335, 350, 366, 382, 398, 415, 431, 446, 462, 479, 495, 511, 526, 543, 559, 575, 591, 607, 623, 639, 655, 672, 687,
                               703, 719, 736, 752, 767, 783, 799, 816, 832, 848, 863, 880, 896, 912, 928, 944, 960, 976, 992, 1009, 1024, 1040, 1056, 1073, 1089, 1104, 1120, 1137, 1153, 1169, 1184, 1201, 1217, 1233, 1249, 1264]]
    # 旋风攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 263, 289, 316, 343, 369, 396, 423, 449, 476, 502, 529, 556, 582, 609, 636, 662, 689, 716, 742, 769, 796, 822, 849, 876, 902, 929, 955, 982, 1009, 1035, 1062, 1089, 1115, 1142, 1169,
                               1195, 1222, 1249, 1275, 1302, 1329, 1355, 1382, 1409, 1435, 1462, 1488, 1515, 1542, 1568, 1595, 1622, 1648, 1675, 1702, 1728, 1755, 1782, 1808, 1835, 1862, 1888, 1915, 1942, 1968, 1995, 2021, 2048, 2075, 2101]]
    攻击次数2 = 8
    # 基础 = 2094.93333333333
    # 成长 = 236.066666666667
    CD = 5
    TP成长 = 0.1
    TP上限 = 5


class 技能3(职业主动技能):
    名称 = '行云：疾'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 横扫攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 2932, 3231, 3529, 3826, 4124, 4421, 4719, 5016, 5314, 5611, 5909, 6206, 6504, 6801, 7099, 7397, 7695, 7993, 8290, 8588, 8885, 9183, 9480, 9778, 10075, 10373, 10670, 10968, 11265, 11563, 11861, 12159, 12457, 12754, 13052,
                               13349, 13647, 13944, 14242, 14539, 14837, 15134, 15432, 15730, 16027, 16326, 16623, 16921, 17218, 17516, 17813, 18111, 18408, 18706, 19003, 19301, 19599, 19896, 20194, 20491, 20790, 21087, 21385, 21682, 21980, 22277, 22575, 22872, 23170, 23468]]
    # 基础 = 2634.38095238095
    # 成长 = 297.619047619048
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5


class 技能4(职业主动技能):
    名称 = '行云：落'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 3784.675
    # 成长 = 427.325
    data0 = [(i*1.0) for i in [0, 4212, 4639, 5067, 5494, 5921, 6348, 6776, 7203, 7631, 8058, 8485, 8912, 9339, 9768, 10195, 10622, 11049, 11476, 11903, 12332, 12759, 13186, 13613, 14040, 14468, 14896, 15323, 15750, 16177, 16604, 17032, 17459, 17887, 18314,
                               18741, 19169, 19596, 20023, 20451, 20878, 21305, 21733, 22160, 22587, 23014, 23442, 23870, 24297, 24724, 25151, 25578, 26006, 26434, 26861, 27288, 27715, 28142, 28571, 28998, 29425, 29852, 30279, 30707, 31135, 31562, 31989, 32416, 32843, 33271, 33698]]
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 5


class 技能5(被动技能):
    名称 = '行云：沐'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(0.95 + 0.02 * self.等级, 5)


class 技能6(职业主动技能):
    名称 = '旋风枪'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 4467.65
    # 成长 = 504.35
    CD = 9
    data0 = [(i*1.24) for i in [0, 475, 523, 569, 618, 667, 715, 763, 811, 860, 907, 956, 1004, 1051, 1100, 1149, 1196, 1244, 1293, 1341, 1388, 1436, 1486, 1534, 1580, 1630, 1678, 1725, 1775, 1822, 1871, 1918, 1967, 2016, 2062, 2111, 2160, 2208, 2255, 2304, 2352, 2400, 2448, 2497, 2545, 2592, 2641, 2689, 2736, 2786, 2833, 2882, 2930, 2978, 3027, 3073, 3122, 3171, 3219, 3267, 3315, 3363, 3411, 3459, 3507, 3556, 3604, 3653, 3700, 3747, 3797]]
    攻击次数 = 11
    TP成长 = 0.1
    TP上限 = 5


class 技能7(职业主动技能):
    名称 = '无畏波动枪'
    # 其余部分能被撞出去的才有,固定怪物没有
    备注 = '突进+刺击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 固定怪物吃以下
    # 普通突进攻击力：<data2>%
    data0 = [(i*1.1267) for i in [0, 1844, 2031, 2218, 2405, 2591, 2778, 2965, 3152, 3339, 3526, 3714, 3902, 4089, 4276, 4463, 4649, 4836, 5023, 5210, 5397, 5584, 5771, 5958, 6147, 6334, 6521, 6707, 6894, 7081, 7268, 7455, 7642, 7829, 8016, 8203, 8390, 8579, 8765, 8952, 9139, 9326, 9513, 9700, 9887, 10074, 10261, 10448, 10634, 10821, 11010, 11197, 11384, 11571, 11758, 11945, 12132, 12319, 12506, 12692, 12879, 13066, 13253, 13442, 13629, 13816, 14003, 14190, 14377, 14564, 14750]]
    攻击次数 = 1
    # 普通刺击攻击力：<data3>%
    data1 = [(i*1.1267) for i in [0, 4302, 4739, 5174, 5611, 6048, 6485, 6921, 7357, 7793, 8230, 8667, 9104, 9539, 9976, 10412, 10849, 11285, 11722, 12159, 12595, 13032, 13467, 13904, 14341, 14778, 15215, 15650, 16086, 16523, 16960, 17396, 17833, 18269, 18705, 19142, 19578, 20015, 20452, 20889, 21324, 21760, 22197, 22634, 23071, 23507, 23944, 24379, 24816, 25253, 25689, 26126, 26563, 26999, 27434, 27871, 28308, 28745, 29182, 29618, 30053, 30490, 30927, 31364, 31800, 32237, 32674, 33109, 33545, 33982, 34419]]
    攻击次数2 = 1

    # 能推开的吃以下的
    # 对被刺穿敌人的攻击力：<data0>%
    # data0 = [0, 1463, 1612, 1759, 1908, 2057, 2206, 2353, 2502, 2651, 2799, 2947, 3096, 3245, 3393, 3541, 3690, 3839, 3986, 4135, 4284, 4432, 4580, 4729, 4878, 5026, 5174, 5323, 5472, 5619, 5768, 5917, 6066, 6213, 6362, 6511, 6659, 6807, 6956, 7105, 7253, 7401, 7550, 7699, 7846, 7995, 8144, 8292, 8440, 8589, 8738, 8886, 9034, 9183, 9332, 9480, 9628, 9777, 9925, 10073, 10222, 10371, 10519, 10667, 10816, 10965, 11113, 11261, 11410, 11559, 11707]
    # 攻击次数 = 1
    # 被刺穿后弹开时的攻击力：<data1>%
    # data1 = [0, 3512, 3868, 4224, 4580, 4937, 5294, 5650, 6006, 6362, 6718, 7074, 7431, 7788, 8144, 8500, 8856, 9212, 9569, 9925, 10282, 10638, 10994, 11350, 11707, 12063, 12420, 12776, 13132, 13488, 13844, 14201, 14557, 14914, 15270, 15626, 15982, 16339, 16695, 17052, 17408, 17764, 18120, 18476, 18833, 19189, 19546, 19902, 20258, 20614, 20971, 21327, 21683, 22040, 22396, 22752, 23109, 23465, 23821, 24178, 24534, 24890, 25246, 25603, 25959, 26315, 26672, 27028, 27384, 27741, 28097]
    # 弹开的敌人撞到地面时的冲撞攻击力：<data4>%
    # data4 = [0, 878, 967, 1056, 1145, 1234, 1323, 1412, 1501, 1590, 1679, 1768, 1857, 1946, 2035, 2124, 2213, 2302, 2391, 2481, 2570, 2659, 2748, 2837, 2927, 3016, 3105, 3194, 3283, 3372, 3461, 3550, 3639, 3728, 3817, 3906, 3995, 4084, 4173, 4262, 4351, 4440, 4529, 4618, 4707, 4797, 4886, 4975, 5064, 5153, 5243, 5332, 5421, 5510, 5599, 5688, 5777, 5866, 5955, 6044, 6133, 6222, 6311, 6400, 6489, 6578, 6667, 6756, 6845, 6934, 7023]
    # 弹开的敌人撞到墙壁时的冲撞攻击力：<data5>%
    # data5 = [0, 994, 1095, 1197, 1297, 1399, 1499, 1600, 1702, 1802, 1904, 2004, 2105, 2206, 2307, 2408, 2509, 2610, 2710, 2812, 2912, 3014, 3115, 3215, 3317, 3417, 3518, 3620, 3720, 3822, 3922, 4023, 4124, 4225, 4327, 4427, 4528, 4629, 4730, 4830, 4932, 5033, 5133, 5235, 5335, 5437, 5537, 5638, 5740, 5840, 5942, 6042, 6143, 6245, 6345, 6446, 6547, 6648, 6748, 6850, 6951, 7052, 7153, 7253, 7355, 7455, 7557, 7658, 7758, 7860, 7960]

    # 基础 = 5259.13513513513
    # 成长 = 593.864864864865
    CD = 9.0
    TP成长 = 0.1
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '螺旋波动枪'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 38
    # 基本和韩服一样
    data0 = [int(i*1.1571) for i in [0,2769, 3050, 3331, 3612, 3893, 4173, 4454, 4735, 5016, 5297, 5578, 5860, 6140, 6421, 6702, 6983, 7264, 7545, 7826, 8106, 8387, 8668, 8949, 9231, 9512, 9793, 10073, 10354, 10635, 10916, 11197, 11478, 11759, 12039, 12320, 12601, 12883, 13164, 13445, 13726, 14007, 14287, 14568, 14849, 15130, 15411, 15692, 15973, 16253, 16535, 16816, 17097, 17378, 17659, 17940, 18220, 18501, 18782, 19063, 19344, 19625, 19907, 20188, 20468, 20749, 21030, 21311, 21592, 21873, 22154]]
    data1 = [int(i*1.1571) for i in [0,4615, 5083, 5551, 6019, 6488, 6956, 7424, 7892, 8360, 8828, 9296, 9766, 10234, 10702, 11170, 11638, 12106, 12575, 13043, 13511, 13979, 14447, 14915, 15385, 15853, 16321, 16789, 17257, 17725, 18193, 18662, 19130, 19598, 20066, 20534, 21002, 21472, 21940, 22408, 22876, 23344, 23812, 24280, 24749, 25217, 25685, 26153, 26621, 27089, 27559, 28027, 28495, 28963, 29431, 29899, 30367, 30836, 31304, 31772, 32240, 32708, 33178, 33646, 34114, 34582, 35050, 35518, 35986, 36454, 36923]]
    data2 = [int(i*1.1571) for i in [0,1846, 2033, 2221, 2408, 2595, 2782, 2969, 3157, 3344, 3531, 3718, 3906, 4094, 4281, 4468, 4655, 4843, 5030, 5217, 5404, 5592, 5779, 5966, 6154, 6341, 6528, 6716, 6903, 7090, 7277, 7465, 7652, 7839, 8026, 8214, 8401, 8589, 8776, 8963, 9150, 9338, 9525, 9712, 9899, 10087, 10274, 10461, 10648, 10836, 11024, 11211, 11398, 11585, 11772, 11960, 12147, 12334, 12521, 12709, 12896, 13083, 13271, 13458, 13646, 13833, 14020, 14207, 14395, 14582, 14769]]
    攻击次数2 = 1
    攻击次数3 = 1
    CD = 15
    TP成长 = 0.1
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = '升龙破空枪'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 数据对不上
    # 基础 = 8384.54285714286
    # 成长 = 1091.45714285714
    # 横扫攻击力：<data0>%
    data0 = [(i*1.15) for i in [0, 2420, 2665, 2911, 3156, 3402, 3647, 3893, 4138, 4385, 4629, 4875, 5121, 5367, 5611, 5857, 6103, 6347, 6594, 6839, 7084, 7330, 7576, 7820, 8067, 8312, 8558, 8803, 9049, 9294, 9540, 9785, 10032, 10276, 10522, 10768, 11013, 11258, 11505, 11750, 11995, 12241, 12487, 12731, 12978, 13223, 13469, 13714, 13959, 14205, 14450, 14696, 14942, 15187, 15432, 15679, 15923, 16169, 16415, 16660, 16905, 17152, 17396, 17642, 17888, 18134, 18378, 18625, 18870, 19116, 19361]]
    # 上挑攻击力：<data1>%
    data1 = [(i*1.15) for i in [0, 3630, 3998, 4367, 4734, 5103, 5471, 5840, 6208, 6576, 6944, 7313, 7681, 8049, 8417, 8785, 9154, 9522, 9890, 10259, 10628, 10996, 11364, 11732, 12101, 12469, 12837, 13205, 13573, 13942, 14310, 14678, 15047, 15415, 15784, 16151, 16520, 16887, 17257, 17625, 17993, 18361, 18730, 19098, 19466, 19835, 20203, 20572, 20939, 21308, 21675, 22045, 22412, 22781, 23148, 23518, 23885, 24254, 24621, 24990, 25360, 25727, 26096, 26463, 26833, 27200, 27569, 27936, 28305, 28673, 29042]]
    攻击次数2 = 1
    # 最后一击攻击力：<data2>%
    data2 = [(i*1.15) for i in [0, 4950, 5452, 5955, 6456, 6958, 7461, 7963, 8466, 8967, 9469, 9972, 10474, 10977, 11479, 11981, 12483, 12985, 13488, 13989, 14491, 14994, 15496, 15999, 16501, 17003, 17506, 18008, 18510, 19011, 19513, 20016, 20518, 21021, 21523, 22025, 22528, 23030, 23533, 24033, 24535, 25038, 25540, 26043, 26545, 27047, 27550, 28052, 28555, 29056, 29558, 30060, 30562, 31065, 31567, 32069, 32572, 33074, 33576, 34078, 34580, 35083, 35585, 36087, 36589, 37091, 37594, 38096, 38598, 39100, 39602]]
    攻击次数3 = 1
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.10
            self.CD *= 0.88
        if x == 1:
            self.倍率 *= 1.19
            self.CD *= 0.88


class 技能10(职业主动技能):
    名称 = '狂龙怒啸'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 旋转攻击力：<data0>%
    data0 = [(i*1.1813) for i in [0, 667, 735, 803, 870, 939, 1006, 1073, 1142, 1210, 1277, 1345, 1413, 1481, 1549, 1616, 1683, 1751, 1820, 1887, 1954, 2023, 2091, 2158, 2226, 2293, 2361, 2430, 2497, 2564, 2633, 2701, 2768, 2836, 2903, 2972, 3039, 3107, 3174, 3241, 3311, 3378, 3445, 3513, 3582, 3649, 3717, 3784, 3852, 3921, 3988, 4055, 4122, 4192, 4259, 4326, 4394, 4463, 4530, 4598, 4665, 4732, 4802, 4869, 4936, 5004, 5073, 5140, 5207, 5275, 5342]]
    攻击次数 = 15
    # 基础 = 8556.5625
    # 成长 = 968.4375
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.76
        if x == 1:
            self.倍率 *= 1.188
            self.CD *= 0.76


class 技能11(职业主动技能):
    名称 = '夺命雷霆枪'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 近距离刺击攻击力：<data0>%
    data0 = [(i*1.1199) for i in [0, 893, 984, 1074, 1166, 1256, 1345, 1436, 1527, 1618, 1708, 1799, 1890, 1980, 2071, 2162, 2252, 2344, 2434, 2524, 2616, 2705, 2796, 2886, 2977, 3068, 3158, 3250, 3340, 3430, 3522, 3612, 3702, 3794, 3883, 3975, 4065, 4155, 4246, 4337, 4428, 4518, 4608, 4700, 4790, 4880, 4972, 5062, 5153, 5243, 5333, 5424, 5515, 5606, 5696, 5787, 5878, 5968, 6060, 6150, 6240, 6332, 6422, 6511, 6602, 6693, 6784, 6874, 6965, 7056, 7146]]
    攻击次数 = 15
    # 引起受创效果的刺击攻击力：<data1>%
    # data1 = [0, 850, 937, 1023, 1110, 1196, 1281, 1368, 1454, 1541, 1627, 1713, 1800, 1886, 1972, 2059, 2145, 2232, 2318, 2404, 2491, 2576, 2663, 2749, 2835, 2922, 3008, 3095, 3181, 3267, 3354, 3440, 3526, 3613, 3698, 3786, 3871, 3957, 4044, 4130, 4217, 4303, 4389, 4476, 4562, 4648, 4735, 4821, 4908, 4993, 5079, 5166, 5252, 5339, 5425, 5511, 5598, 5684, 5771, 5857, 5943, 6030, 6116, 6201, 6288, 6374, 6461, 6547, 6633, 6720, 6806]
    # #每1次刺击对应的横斩攻击力：<data2>%
    data1 = [(i*1.1199) for i in [0, 162, 179, 194, 211, 228, 245, 261, 277, 294, 310, 327, 343, 359, 376, 393, 410, 426, 442, 458, 475, 491, 508, 524, 541, 558, 574, 591, 606, 623, 639, 656, 673, 690, 706, 722, 739, 755, 772, 788, 804, 821, 838, 855, 870, 886, 903, 920, 937, 952, 969, 986, 1003, 1020, 1034, 1051, 1068, 1085, 1101, 1117, 1134, 1151, 1168, 1183, 1199, 1216, 1233, 1250, 1266, 1283, 1299]]
    攻击次数2 = 15
    # 最后横斩攻击力：<data3>%
    data2 = [(i*1.1198) for i in [0, 9746, 10734, 11722, 12712, 13700, 14688, 15678, 16667, 17655, 18644, 19633, 20621, 21610, 22599, 23587, 24576, 25565, 26553, 27543, 28532, 29520, 30509, 31497, 32486, 33475, 34463, 35452, 36441, 37429, 38418, 39408, 40396, 41385, 42374, 43362, 44351, 45340, 46328, 47316, 48306, 49294, 50282, 51273, 52261, 53249, 54239, 55227, 56215, 57205, 58193, 59181, 60170, 61159, 62147, 63137, 64126, 65114, 66103, 67092, 68080, 69069, 70058, 71046, 72035, 73024, 74012, 75002, 75990, 76979, 77968]]
    攻击次数3 = 1
    # 基础 = 21869.8666666667
    # 成长 = 2472.13333333333
    CD = 47
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data2 = [(i * 1.65) for i in self.data2]
        if x == 1:
            self.data2 = [(i * 1.86) for i in self.data2]


class 技能12(被动技能):
    名称 = '行云：启'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.06 + 0.015 * self.等级, 5)


class 技能13(职业主动技能):
    名称 = '流云幻灭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 43306.1
    # 成长 = 13091
    # 原数据是游戏数据的1.1倍,需要确认
    # 第一击攻击力：<data0>%
    data0 = [(i*1.191) for i in [0, 964, 1188, 1411, 1635, 1858, 2081, 2305, 2529, 2752, 2976, 3200, 3424, 3647, 3871, 4094, 4317, 4541, 4765, 4988, 5212, 5436, 5660, 5883, 6106, 6330, 6553, 6777, 7001, 7224, 7448, 7672, 7896, 8119, 8342, 8566,
                               8789, 9013, 9237, 9461, 9684, 9908, 10132, 10355, 10578, 10802, 11025, 11249, 11473, 11697, 11920, 12144, 12368, 12590, 12814, 13038, 13261, 13485, 13709, 13933, 14156, 14380, 14604, 14826, 15050, 15274, 15497, 15721, 15945, 16169, 16392]]
    攻击次数 = 1
    # 第2击攻击力：<data1>%
    data1 = [(i*1.048) for i in [0, 2739, 3375, 4010, 4645, 5281, 5916, 6552, 7187, 7821, 8458, 9092, 9728, 10363, 10999, 11633, 12270, 12904, 13540, 14175, 14811, 15445, 16082, 16716, 17353, 17987, 18622, 19258, 19893, 20528, 21164, 21799, 22434, 23070, 23705,
                               24340, 24976, 25611, 26247, 26882, 27517, 28153, 28788, 29423, 30059, 30694, 31329, 31964, 32600, 33234, 33871, 34505, 35142, 35776, 36412, 37047, 37683, 38317, 38954, 39588, 40224, 40859, 41495, 42129, 42766, 43400, 44035, 44671, 45306, 45942, 46577]]
    攻击次数2 = 1
    # 第3击攻击力：<data2>%
    data2 = [(i*1.048) for i in [0, 3288, 4049, 4811, 5574, 6337, 7100, 7861, 8624, 9387, 10149, 10911, 11673, 12437, 13199, 13960, 14723, 15485, 16249, 17011, 17772, 18535, 19298, 20061, 20822, 21584, 22348, 23110, 23872, 24634, 25396, 26160, 26921, 27684, 28446,
                               29210, 29972, 30733, 31496, 32259, 33022, 33783, 34545, 35308, 36071, 36833, 37595, 38357, 39121, 39883, 40645, 41407, 42170, 42933, 43694, 44457, 45219, 45982, 46744, 47506, 48269, 49032, 49795, 50556, 51318, 52082, 52844, 53605, 54368, 55130, 55894]]
    攻击次数3 = 1
    # 第4击攻击力：<data3>%
    data3 = [(i*1.048) for i in [0, 3835, 4725, 5614, 6503, 7394, 8283, 9172, 10062, 10951, 11840, 12729, 13619, 14508, 15397, 16289, 17178, 18067, 18957, 19846, 20735, 21624, 22514, 23403, 24293, 25183, 26072, 26961, 27851, 28740, 29629, 30518, 31409, 32299, 33189,
                               34078, 34967, 35856, 36746, 37635, 38524, 39414, 40304, 41193, 42083, 42972, 43861, 44752, 45641, 46530, 47419, 48310, 49199, 50088, 50978, 51867, 52756, 53645, 54535, 55424, 56314, 57204, 58094, 58983, 59873, 60762, 61651, 62541, 63430, 64320, 65210]]
    攻击次数4 = 1
    # 第5击攻击力：<data4>%
    data4 = [(i*1.048) for i in [0, 4384, 5400, 6416, 7433, 8449, 9465, 10482, 11498, 12515, 13532, 14548, 15564, 16581, 17598, 18615, 19631, 20647, 21665, 22681, 23697, 24714, 25730, 26747, 27764, 28780, 29797, 30813, 31828, 32845, 33862, 34878, 35895, 36912, 37928,
                               38945, 39961, 40977, 41995, 43011, 44027, 45044, 46060, 47078, 48094, 49110, 50127, 51143, 52160, 53177, 54193, 55209, 56227, 57243, 58258, 59275, 60291, 61307, 62325, 63341, 64358, 65374, 66390, 67408, 68424, 69440, 70457, 71474, 72490, 73507, 74523]]
    攻击次数5 = 1
    # 第6击攻击力：<data5>%
    data5 = [(i*1.048) for i in [0, 1644, 2025, 2406, 2786, 3168, 3549, 3930, 4312, 4694, 5074, 5456, 5835, 6217, 6599, 6980, 7361, 7742, 8124, 8506, 8886, 9267, 9647, 10029, 10411, 10792, 11173, 11555, 11936, 12318, 12697, 13079, 13461, 13841, 14223, 14604,
                               14985, 15367, 15747, 16128, 16509, 16891, 17273, 17653, 18035, 18416, 18797, 19178, 19559, 19941, 20322, 20703, 21085, 21465, 21847, 22229, 22608, 22990, 23371, 23753, 24134, 24515, 24897, 25276, 25658, 26040, 26420, 26802, 27184, 27565, 27946]]
    攻击次数6 = 3
    # 第7击攻击力：<data6>%
    data6 = [(i*1.048) for i in [0, 4932, 6075, 7219, 8361, 9505, 10649, 11792, 12936, 14081, 15224, 16367, 17511, 18654, 19798, 20942, 22085, 23228, 24372, 25516, 26660, 27804, 28947, 30090, 31233, 32377, 33521, 34665, 35809, 36952, 38095, 39239, 40383, 41526, 42670,
                               43813, 44956, 46100, 47245, 48388, 49532, 50676, 51818, 52962, 54106, 55249, 56393, 57538, 58680, 59824, 60967, 62111, 63255, 64398, 65541, 66685, 67828, 68973, 70117, 71260, 72403, 73547, 74690, 75834, 76978, 78121, 79265, 80408, 81552, 82696, 83839]]
    攻击次数7 = 1
    # 第8击攻击力：<data7>%
    data7 = [(i*1.048) for i in [0, 5478, 6749, 8020, 9290, 10561, 11832, 13103, 14373, 15644, 16915, 18185, 19456, 20727, 21998, 23268, 24539, 25810, 27080, 28351, 29621, 30892, 32162, 33433, 34704, 35974, 37245, 38516, 39788, 41057, 42329, 43600, 44869, 46141,
                               47412, 48683, 49953, 51224, 52495, 53763, 55035, 56306, 57577, 58847, 60118, 61389, 62659, 63930, 65201, 66472, 67742, 69013, 70284, 71555, 72825, 74096, 75367, 76636, 77907, 79178, 80449, 81719, 82990, 84261, 85531, 86802, 88073, 89344, 90614, 91885, 93156]]
    攻击次数8 = 1
    # 斗气长枪攻击力：<data8>%
    data8 = [(i*1.191) for i in [0, 24110, 29702, 38820, 44971, 51121, 57271, 63421, 69571, 75721, 81871, 88022, 94171, 100321, 106472, 112621, 118773, 124922, 131070, 137222, 143371, 149520, 155672, 161821, 167971, 174122, 180271, 186422, 192572, 198722, 204872, 211023, 217172, 223322, 229473,
                               235622, 241773, 247923, 254072, 260223, 266373, 272524, 278673, 284823, 290974, 297123, 303272, 309424, 315572, 321723, 327873, 334022, 340173, 346323, 352473, 358624, 364774, 370923, 377074, 383224, 389373, 395525, 401674, 407823, 413975, 420124, 426273, 432425, 438574, 444725, 450875]]
    攻击次数9 = 1
    CD = 145

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        等效倍率 += self.data0[self.等级] * self.攻击次数
        等效倍率 += self.data1[self.等级] * self.攻击次数2
        等效倍率 += self.data2[self.等级] * self.攻击次数3
        等效倍率 += self.data3[self.等级] * self.攻击次数4
        等效倍率 += self.data4[self.等级] * self.攻击次数5
        等效倍率 += self.data5[self.等级] * self.攻击次数6
        等效倍率 += self.data6[self.等级] * self.攻击次数7
        等效倍率 += self.data7[self.等级] * self.攻击次数8
        等效倍率 += self.data8[self.等级] * self.攻击次数9
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(职业主动技能):
    名称 = '风火燎原'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [(i*1.1489) for i in [0, 1283, 1413, 1545, 1675, 1805, 1935, 2065, 2196, 2326, 2456, 2585, 2715, 2846, 2976, 3106, 3236, 3366, 3498, 3628, 3758, 3888, 4018, 4149, 4279, 4409, 4539, 4669, 4800, 4930, 5060, 5190, 5320, 5451, 5582, 5712, 5842, 5972, 6103, 6233, 6363, 6493, 6623, 6754, 6884, 7014, 7144, 7274, 7405, 7535, 7666, 7796, 7926, 8057, 8187, 8317, 8447, 8576, 8707, 8837, 8967, 9097, 9227, 9358, 9488, 9619, 9749, 9879, 10010, 10140, 10270]]
    攻击次数 = 20
    # 基础 = 21959.0909090909
    # 成长 = 2480.90909090909
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.275
        if x == 1:
            self.倍率 *= 1.365


class 技能15(职业主动技能):
    名称 = '三一斩月'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 枪身攻击力：<data0>%
    data0 = [(i*1.1707) for i in [0, 667, 734, 801, 868, 936, 1004, 1072, 1139, 1208, 1275, 1342, 1409, 1476, 1546, 1613, 1680, 1748, 1815, 1883, 1950, 2018, 2086, 2154, 2221, 2289, 2356, 2423, 2491, 2560, 2627, 2694, 2762, 2830, 2897, 2964, 3033, 3101, 3168, 3235, 3302, 3371, 3438, 3506, 3574, 3641, 3709, 3776, 3843, 3911, 3980, 4047, 4115, 4182, 4249, 4317, 4385, 4452, 4520, 4587, 4656, 4723, 4790, 4857, 4926, 4994, 5061, 5128, 5196, 5264, 5331]]
    # [三一斩月]攻击力：<data1>%
    data1 = [(i*1.1707) for i in [0, 4081, 4495, 4910, 5324, 5738, 6152, 6567, 6980, 7395, 7809, 8224, 8637, 9051, 9466, 9879, 10294, 10708, 11123, 11536, 11951, 12365, 12779, 13193, 13607, 14022, 14435, 14850, 15264, 15677, 16091, 16505, 16920, 17333, 17748, 18162, 18577, 18990, 19405, 19819, 20232, 20647, 21061, 21476, 21889, 22304, 22718, 23133, 23546, 23960, 24375, 24788, 25203, 25617, 26032, 26445, 26860, 27274, 27689, 28102, 28516, 28931, 29344, 29759, 30173, 30588, 31001, 31414, 31829, 32242, 32657]]
    攻击次数2 = 8
    # 基础 = 28510.88235
    # 成长 = 3220.117647
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        if x == 1:
            self.倍率 *= 1.31


class 技能16(职业主动技能):
    名称 = '无双突刺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 第1~2击攻击力：<data0>%
    data0 = [(i*1.1236) for i in [0, 3398, 3743, 4088, 4433, 4779, 5122, 5467, 5813, 6157, 6502, 6846, 7191, 7537, 7880, 8226, 8571, 8916, 9261, 9604, 9950, 10295, 10640, 10985, 11330, 11674, 12019, 12364, 12708, 13054, 13398, 13743, 14089, 14432, 14778, 15122, 15468, 15813, 16156, 16502, 16847, 17192, 17536, 17880, 18226, 18571, 18915, 19260, 19606, 19950, 20295, 20639, 20984, 21330, 21674, 22020, 22364, 22708, 23054, 23398, 23743, 24088, 24432, 24778, 25123, 25467, 25812, 26157, 26502, 26847, 27191]]
    攻击次数 = 2
    # 第3~4击攻击力：<data1>%
    # data1 = [0, 20418, 22489, 24562, 26633, 28704, 30776, 32847, 34918, 36991, 39062, 41133, 43204, 45276, 47347, 49419, 51491, 53562, 55633, 57705, 59776, 61848, 63920, 65991, 68062, 70133, 72205, 74277, 76348, 78420, 80491, 82562, 84634, 86706, 88777, 90849, 92920, 94991, 97062, 99135, 101206, 103277, 105349, 107420, 109491, 111564, 113635, 115706, 117778, 119849, 121920, 123993, 126064, 128135, 130207, 132278, 134349, 136422, 138493, 140564, 142635, 144707, 146778, 148850, 150922, 152993, 155064, 157136, 159207, 161279, 163351]
    # 第3~4击枪尾攻击力：<data2>%
    data1 = [(i*1.1238) for i in [0, 24053, 26495, 28934, 31375, 33815, 36255, 38696, 41136, 43577, 46016, 48456, 50898, 53338, 55777, 58218, 60659, 63100, 65539, 67979, 70420, 72860, 75300, 77741, 80181, 82620, 85062, 87502, 89942, 92382, 94822, 97264, 99703, 102143, 104584, 107024, 109465, 111905, 114345, 116785, 119225, 121666, 124107, 126546, 128987, 131427, 133868, 136308, 138748, 141188, 143628, 146069, 148510, 150950, 153389, 155831, 158271, 160710, 163151, 165591, 168033, 170472, 172912, 175353, 177793, 180233, 182674, 185114, 187553, 189994, 192435]]
    攻击次数2 = 2
    # 基础 = 46982.8
    # 成长 = 5305.2
    CD = 33.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.data1 = [(i*1.45) for i in self.data1]
            self.CD *= 0.9
            # self.倍率 *= 1.27049


class 技能17(被动技能):
    名称 = '行云：冥'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '流光无影闪'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 52609.8333333333
    # 成长 = 5940.16666666667
    # 突进攻击力：<data0>%
    data0 = [(i*1.1341) for i in [0, 5532, 6094, 6655, 7216, 7778, 8339, 8900, 9462, 10023, 10585, 11146, 11706, 12269, 12830, 13391, 13952, 14514, 15075, 15637, 16197, 16760, 17321, 17882, 18443, 19005, 19566, 20127, 20688, 21250, 21812, 22372, 22933, 23496, 24057, 24618, 25179, 25741, 26303, 26863, 27424, 27987, 28547, 29108, 29670, 30231, 30793, 31354, 31915, 32478, 33038, 33599, 34161, 34721, 35283, 35845, 36406, 36967, 37529, 38090, 38652, 39212, 39774, 40336, 40896, 41457, 42020, 42581, 43141, 43703, 44265]]
    攻击次数 = 1
    # 终结攻击力：<data1>%
    data1 = [(i*1.1341) for i in [0, 55945, 61621, 67297, 72973, 78649, 84324, 90000, 95676, 101351, 107027, 112702, 118379, 124054, 129730, 135406, 141081, 146756, 152434, 158109, 163784, 169461, 175136, 180811, 186486, 192163, 197838, 203514, 209190, 214866, 220541, 226217, 231893, 237568, 243245, 248920, 254596, 260271, 265947, 271622, 277298, 282975, 288650, 294326, 300002, 305677, 311352, 317029, 322704, 328380, 334055, 339732, 345407, 351082, 356759, 362434, 368109, 373786, 379462, 385137, 390813, 396488, 402164, 407839, 413516, 419192, 424867, 430543, 436218, 441894, 447570]]
    攻击次数2 = 1
    CD = 44
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            # 算法待定,加还是乘
            self.倍率 *= 1.2*1.14
            self.CD *= 0.88


class 技能19(职业主动技能):
    名称 = '极影无形杀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 第1次刺击攻击力：<data0>%
    data0 = [(i*1.1231) for i in [0, 13262, 16337, 19411, 22487, 25562, 28639, 31714, 34790, 37864, 40940, 44015, 47090, 50166, 53240, 56316, 59391, 62467, 65542, 68616, 71692, 74767, 77843, 80918, 83994, 87068, 90144, 93220, 96296, 99371, 102445, 105521, 108596, 111672, 114747, 117822, 120897, 123972, 127048, 130123, 133198, 136273, 139349, 142424, 145500, 148575, 151649, 154726, 157801, 160877, 163952, 167027, 170102, 173178, 176253, 179328, 182403, 185478, 188554, 191629, 194705, 197780, 200855, 203930, 207005, 210081, 213157, 216231, 219307, 222383, 225458]]
    # 乱舞斩击攻击力：<data1>%
    data1 = [(i*1.1231) for i in [0, 7368, 9076, 10784, 12493, 14201, 15911, 17619, 19326, 21036, 22744, 24452, 26161, 27869, 29577, 31287, 32995, 34703, 36412, 38120, 39830, 41537, 43245, 44955, 46663, 48371, 50080, 51788, 53496, 55206, 56914, 58622, 60331, 62039, 63749, 65456, 67164, 68874, 70582, 72290, 73999, 75707, 77415, 79125, 80833, 82542, 84250, 85958, 87668, 89375, 91083, 92793, 94501, 96209, 97918, 99626, 101336, 103044, 104751, 106461, 108169, 109877, 111587, 113294, 115002, 116712, 118420, 120129, 121837, 123545, 125255]]
    攻击次数2 = 7
    # 乱舞刺击攻击力：<data2>%
    data2 = [(i*1.1231) for i in [0, 2946, 3631, 4313, 4997, 5681, 6364, 7047, 7731, 8414, 9097, 9781, 10464, 11147, 11831, 12514, 13197, 13881, 14565, 15247, 15932, 16614, 17298, 17981, 18665, 19347, 20032, 20714, 21399, 22082, 22765, 23449, 24132, 24815, 25499, 26182, 26865, 27550, 28232, 28916, 29600, 30283, 30966, 31650, 32333, 33016, 33700, 34383, 35066, 35750, 36433, 37116, 37800, 38484, 39166, 39851, 40533, 41218, 41900, 42584, 43267, 43951, 44633, 45318, 46001, 46684, 47368, 48051, 48734, 49418, 50101]]
    攻击次数3 = 17
    # 最后一击攻击力：<data3>%
    data3 = [(i*1.1231) for i in [0, 32418, 39936, 47454, 54971, 62488, 70006, 77523, 85041, 92556, 100074, 107592, 115109, 122627, 130144, 137661, 145179, 152697, 160214, 167731, 175249, 182766, 190284, 197802, 205318, 212836, 220353, 227871, 235388, 242905, 250423, 257941, 265458, 272975, 280493, 288010, 295528, 303046, 310562, 318080, 325598, 333115, 340632, 348149, 355667, 363185, 370701, 378218, 385736, 393253, 400771, 408289, 415805, 423323, 430841, 438358, 445875, 453393, 460910, 468428, 475946, 483462, 490980, 498497, 506015, 513533, 521049, 528567, 536085, 543602, 551119]]
    攻击次数4 = 1

    # 基础 = 107737
    # 成长 = 32553
    CD = 180


class 技能20(被动技能):
    名称 = '一身是胆'
    所在等级 = 95
    等级上限 = 40
    等级精通 = 30
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(职业主动技能):
    名称 = '双龙流云灭'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.1533) for i in [0, 34351, 37836, 41321, 44806, 48291, 51776, 55261, 58746, 62231, 65716, 69201, 72686, 76171, 79655, 83140, 86625, 90110, 93595, 97080, 100565, 104050, 107535, 111020, 114505, 117990, 121474, 124959, 128444, 131929, 135414, 138899, 142384, 145869, 149354, 152839, 156324, 159809, 163293, 166778, 170263, 173748, 177233, 180718, 184203, 187688, 191173, 194658, 198143, 201628, 205112, 208597, 212082, 215567, 219053, 222538, 226023, 229508, 232993, 236478, 239963, 243448, 246932, 250417, 253902, 257387, 260872, 264357, 267842, 271327, 274812]]
    攻击次数 = 3
    data1 =[int(i*1.1533) for i in [0, 5725, 6306, 6887, 7468, 8048, 8629, 9210, 9791, 10372, 10953, 11533, 12114, 12695, 13276, 13857, 14437, 15018, 15599, 16180, 16761, 17342, 17922, 18503, 19084, 19665, 20246, 20826, 21407, 21988, 22569, 23150, 23731, 24312, 24892, 25473, 26054, 26635, 27216, 27796, 28377, 28958, 29539, 30120, 30701, 31281, 31862, 32443, 33024, 33605, 34185, 34766, 35347, 35928, 36509, 37090, 37670, 38251, 38832, 39413, 39994, 40575, 41155, 41736, 42317, 42898, 43479, 44059, 44640, 45221, 45802]]
    攻击次数2 = 1
    CD = 60.0



class 技能22(职业主动技能):
    名称 = '问鼎·千军破云'
    所在等级 = 100
    等级上限 = 40
    等级精通 = 30
    基础等级 = 2

    data0 =[int(i*1.1486) for i in [0, 44586, 54924, 65263, 75602, 85941, 96279, 106618, 116957, 127296, 137634, 147973, 158312, 168651, 178989, 189328, 199666, 210005, 220344, 230683, 241021, 251360, 261699, 272038, 282376, 292715, 303054, 313393, 323731, 334070, 344409, 354748, 365086, 375425, 385764, 396103, 406441, 416780, 427119, 437458, 447796, 458135, 468474, 478812, 489151, 499490, 509828, 520167, 530506, 540845, 551183, 561522, 571861, 582200, 592538, 602877, 613216, 623555, 633893, 644232, 654571, 664910, 675248, 685587, 695926, 706265, 716603, 726942, 737280, 747619, 757958]]
    攻击次数 = 1
    data1 = [int(i*1.1486) for i in [0, 26751, 32955, 39158, 45361, 51564, 57768, 63971, 70174, 76377, 82581, 88784, 94987, 101190, 107394, 113597, 119800, 126003, 132206, 138410, 144613, 150816, 157019, 163223, 169426, 175629, 181832, 188036, 194239, 200442, 206645, 212849, 219052, 225255, 231458, 237662, 243865, 250068, 256271, 262475, 268678, 274881, 281084, 287287, 293491, 299694, 305897, 312100, 318304, 324507, 330710, 336913, 343117, 349320, 355523, 361726, 367930, 374133, 380336, 386539, 392743, 398946, 405149, 411352, 417555, 423759, 429962, 436165, 442368, 448572, 454775]]
    攻击次数2 = 5
    data2 = [int(i*1.1486) for i in [0, 66878, 82387, 97895, 113403, 128911, 144419, 159927, 175435, 190943, 206451, 221960, 237468, 252976, 268484, 283991, 299500, 315008, 330516, 346024, 361532, 377040, 392548, 408056, 423565, 439073, 454581, 470089, 485597, 501105, 516613, 532121, 547629, 563138, 578646, 594154, 609662, 625170, 640678, 656186, 671694, 687203, 702711, 718218, 733726, 749234, 764743, 780251, 795759, 811267, 826775, 842283, 857791, 873299, 888808, 904316, 919824, 935332, 950840, 966348, 981856, 997364, 1012872, 1028381, 1043889, 1059397, 1074905, 1090413, 1105921, 1121429, 1136937]]
    攻击次数3 = 4

    关联技能 = ['无']
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业属性(角色属性):
    实际名称 = '千魂·决战者'
    角色 = '魔枪士'
    职业 = '决战者'

    武器选项 = ['长枪']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()

        x = self.技能栏[12].加成倍率(self.武器类型)
        self.技能栏[2].被动倍率 *= (0.025 + x) / x
        self.技能栏[3].被动倍率 *= (0.020 + x) / x
        self.技能栏[4].被动倍率 *= (0.015 + x) / x

        y = self.技能栏[17].加成倍率(self.武器类型)
        for i in [1, 2, 3, 4]:
            self.技能栏[i].被动倍率 *= (0.01 + y) / y


class 千魂·决战者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)
