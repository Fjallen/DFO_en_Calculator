from PublicReference.carry.base import *


class 主动技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        # 重火器精通取消除觉醒之外的技能惩罚
        if self.所在等级 not in [50,85,100]:
            return round(self.CD / self.恢复, 1)
        else:
            return super().等效CD(武器类型, 输出类型)


class 技能0(主动技能):
    名称 = 'M137格林机枪'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 51
    data0 = [0,56, 62, 67, 73, 79, 84, 90, 96, 102, 107, 113, 119, 124, 130, 136, 141, 148, 153, 158, 165, 170, 175, 182, 187, 194, 199, 204, 211, 216, 221, 228, 233, 239, 245, 250, 256, 262, 267, 273, 279, 285, 290, 296, 302, 307, 313, 319, 324, 331, 336, 341, 348, 353, 358, 365, 370, 376, 382, 387, 393, 399, 405, 410, 416, 422, 428, 433, 439, 445, 451]
    攻击次数 = 30
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能1(被动技能):
    名称 = '重火器精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能2 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率2(武器类型)


class 技能2(主动技能):
    名称 = '加农炮'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 44
    data0 = [0,1277, 1406, 1536, 1665, 1795, 1924, 2054, 2185, 2313, 2442, 2572, 2703, 2831, 2960, 3091, 3221, 3349, 3480, 3609, 3739, 3867, 3998, 4127, 4257, 4386, 4516, 4645, 4775, 4904, 5034, 5163, 5294, 5424, 5552, 5683, 5812, 5942, 6070, 6201, 6330, 6460, 6589, 6719, 6848, 6978, 7107, 7237, 7366, 7497, 7625, 7755, 7885, 8015, 8143, 8273, 8403, 8533, 8661, 8792, 8921, 9051, 9180, 9310, 9439, 9569, 9700, 9828, 9957, 10088, 10218]
    攻击次数 = 2
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '反坦克炮'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 44
    data1 = [0,587, 646, 706, 766, 825, 885, 944, 1004, 1063, 1123, 1183, 1242, 1301, 1361, 1421, 1481, 1539, 1599, 1659, 1719, 1777, 1837, 1897, 1957, 2017, 2077, 2137, 2196, 2256, 2315, 2375, 2435, 2494, 2553, 2613, 2673, 2733, 2791, 2851, 2911, 2971, 3029, 3089, 3149, 3209, 3268, 3328, 3387, 3447, 3506, 3566, 3626, 3685, 3744, 3804, 3864, 3924, 3983, 4042, 4102, 4162, 4222, 4280, 4340, 4400, 4460, 4519, 4578, 4638, 4698]
    data2 = [0,2350, 2588, 2826, 3064, 3302, 3541, 3779, 4017, 4255, 4495, 4733, 4971, 5209, 5447, 5686, 5924, 6162, 6400, 6638, 6877, 7116, 7354, 7592, 7830, 8069, 8307, 8546, 8784, 9023, 9261, 9499, 9737, 9977, 10215, 10453, 10691, 10929, 11168, 11406, 11644, 11882, 12120, 12359, 12598, 12836, 13074, 13313, 13551, 13789, 14027, 14265, 14504, 14742, 14980, 15219, 15459, 15697, 15935, 16173, 16411, 16650, 16888, 17126, 17364, 17602, 17841, 18080, 18318, 18556, 18795]

    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] + self.data2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(被动技能):
    名称 = '超动力补给包'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.01 * self.等级, 5)


class 技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 42
    data0 = [0,3036, 3345, 3653, 3961, 4269, 4577, 4885, 5194, 5502, 5810, 6118, 6426, 6733, 7043, 7350, 7658, 7966, 8274, 8582, 8891, 9199, 9507, 9815, 10123, 10431, 10739, 11048, 11356, 11664, 11972, 12280, 12587, 12897, 13205, 13512, 13820, 14128, 14436, 14745, 15053, 15361, 15669, 15977, 16285, 16594, 16902, 17210, 17518, 17826, 18134, 18443, 18751, 19059, 19366, 19674, 19982, 20291, 20599, 20907, 21215, 21523, 21831, 22140, 22448, 22756, 23064, 23372, 23680, 23989, 24297]

    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(被动技能):
    名称 = '蓄电激光炮'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['激光炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.45 + 0.05 * self.等级, 5)


class 技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 39
    data0 = [0,280, 307, 336, 365, 393, 422, 451, 480, 507, 536, 565, 593, 621, 650, 678, 706, 735, 763, 792, 819, 848, 877, 906, 933, 962, 991, 1018, 1047, 1076, 1104, 1132, 1162, 1190, 1218, 1247, 1275, 1304, 1332, 1360, 1389, 1418, 1445, 1474, 1503, 1530, 1559, 1588, 1616, 1644, 1673, 1701, 1730, 1758, 1786, 1815, 1843, 1871, 1901, 1930, 1957, 1986, 2015, 2042, 2071, 2100, 2129, 2156, 2185, 2214, 2242]

    攻击次数 = 29
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = 'FM31榴弹发射器'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    data0 = [0,2205, 2429, 2652, 2876, 3100, 3324, 3547, 3771, 3995, 4219, 4442, 4666, 4890, 5114, 5338, 5561, 5785, 6009, 6233, 6456, 6680, 6904, 7128, 7351, 7574, 7798, 8021, 8245, 8469, 8693, 8917, 9140, 9364, 9588, 9812, 10035, 10259, 10483, 10707, 10930, 11154, 11378, 11602, 11825, 12049, 12273, 12497, 12721, 12944, 13168, 13392, 13616, 13839, 14063, 14287, 14511, 14734, 14958, 15182, 15406, 15629, 15853, 16077, 16301, 16524, 16748, 16972, 17196, 17420, 17643]

    攻击次数 = 4
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.6 * 2
        elif x == 1:
            self.倍率 *= 0.64 * 2


class 技能9(主动技能):
    名称 = 'FM92刺弹炮'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 37
    data0 = [0,2213, 2437, 2661, 2887, 3111, 3336, 3560, 3784, 4009, 4234, 4459, 4683, 4907, 5132, 5356, 5582, 5806, 6030, 6255, 6479, 6703, 6929, 7153, 7378, 7602, 7826, 8051, 8276, 8501, 8725, 8949, 9174, 9398, 9624, 9848, 10072, 10297, 10521, 10745, 10971, 11195, 11420, 11644, 11868, 12093, 12318, 12543, 12767, 12991, 13216, 13440, 13664, 13890, 14114, 14339, 14563, 14787, 15012, 15237, 15462, 15686, 15910, 16135, 16359, 16585, 16809, 17033, 17258, 17482, 17707]

    攻击次数 = 5
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '量子爆弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 34
    data1 = [0,2697, 2971, 3244, 3518, 3792, 4066, 4339, 4613, 4886, 5161, 5434, 5708, 5981, 6255, 6528, 6803, 7076, 7350, 7623, 7897, 8171, 8445, 8718, 8992, 9265, 9540, 9813, 10087, 10360, 10634, 10907, 11182, 11455, 11729, 12002, 12276, 12550, 12824, 13097, 13371, 13644, 13919, 14192, 14466, 14739, 15013, 15286, 15561, 15834, 16108, 16381, 16655, 16929, 17203, 17476, 17750, 18023, 18298, 18571, 18845, 19118, 19392, 19665, 19940, 20213, 20487, 20760, 21034, 21308, 21582]
    攻击次数1 = 1
    data2 = [0,8542, 9409, 10275, 11143, 12009, 12876, 13743, 14609, 15476, 16342, 17209, 18075, 18942, 19809, 20675, 21543, 22410, 23276, 24143, 25009, 25876, 26742, 27609, 28476, 29342, 30209, 31077, 31943, 32810, 33676, 34543, 35409, 36276, 37143, 38009, 38876, 39742, 40609, 41477, 42343, 43210, 44076, 44943, 45809, 46676, 47543, 48409, 49276, 50142, 51009, 51877, 52743, 53610, 54476, 55343, 56210, 57076, 57943, 58809, 59676, 60542, 61409, 62277, 63143, 64010, 64877, 65743, 66610, 67476, 68343]
    攻击次数2 = 1

    # 感电
    data3 = [0,12, 12, 13, 15, 15, 16, 17, 18, 19, 21, 22, 23, 24, 24, 25, 27, 28, 29, 30, 32, 33, 34, 35, 35, 36, 38, 39, 40, 41, 42, 44, 45, 45, 46, 47, 49, 50, 51, 52, 53, 55, 56, 56, 57, 58, 59, 61, 62, 63, 64, 66, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 76, 78, 79, 80, 81, 83, 84, 85, 86]
    攻击次数3 = 1

    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数1 + self.data2[self.等级] * self.攻击次数2 + self.data3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 *= 0.21 * 8
            self.攻击次数3 *= 0.21
        elif x == 1:
            self.攻击次数1 = 0
            self.攻击次数2 *= 0.20 * 9
            self.攻击次数3 *= 0.20


class 技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 32
    data0 = [0, 25287, 27852, 30418, 32983, 35549, 38115, 40679, 43245, 45810, 48376, 50941, 53507, 56072, 58638, 61203, 63768, 66334, 68899, 71465, 74030, 76596, 79160, 81726, 84292, 86857, 89423, 91988, 94554, 97118, 99684, 102250, 104815, 107381, 109946, 112512, 115076, 117642, 120207, 122773, 125339, 127904, 130470, 133034, 135600, 138165, 140731, 143296, 145862, 148428, 150992, 153558, 156123, 158689, 161254, 163820, 166386, 168950, 171516, 174081, 176647, 179212, 181778, 184343, 186908, 189474, 192039, 194605, 197170, 199736, 202301]

    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1984
        elif x == 1:
            self.倍率 *= 1.2768


class 技能12(被动技能):
    名称 = '卫星定位'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


class 技能13(主动技能):
    名称 = '卫星射线'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data1 = [0, 4273, 5263, 6255, 7245, 8237, 9227, 10219, 11209, 12201, 13191, 14181, 15173, 16163, 17154, 18145, 19136, 20127, 21118, 22108, 23100, 24090, 25082, 26072, 27064, 28054, 29046, 30036, 31027, 32018, 33009, 34000, 34991, 35981, 36973, 37963, 38955, 39945, 40937, 41927, 42918, 43909, 44900, 45891, 46882, 47872, 48864, 49854, 50846, 51836, 52826, 53818, 54808, 55800, 56790, 57782, 58772, 59763, 60754, 61745, 62736, 63727, 64717, 65709, 66699, 67691, 68681, 69673, 70663, 71654, 72645]
    攻击次数1 = 1
    data2 = [0, 1593, 1962, 2333, 2703, 3072, 3442, 3811, 4181, 4550, 4920, 5290, 5659, 6029, 6398, 6768, 7137, 7507, 7876, 8247, 8617, 8986, 9356, 9725, 10095, 10464, 10834, 11204, 11573, 11943, 12312, 12682, 13051, 13421, 13790, 14160, 14531, 14900, 15270, 15639, 16009, 16378, 16748, 17118, 17487, 17857, 18226, 18596, 18965, 19335, 19706, 20074, 20445, 20814, 21184, 21553, 21923, 22292, 22662, 23032, 23401, 23771, 24140, 24510, 24879, 25249, 25619, 25988, 26359, 26728, 27098]
    攻击次数2 = 8.4 / 0.2
    CD = 145

    def 等效百分比(self, 武器类型):
        if self.等级 >=9: self.倍率 *= 1.1
        return (self.data1[self.等级] * self.攻击次数1 + self.data2[self.等级] * self.攻击次数2) * self.倍率


class 技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 24
    data0 = [0, 1707, 1881, 2053, 2227, 2401, 2573, 2747, 2920, 3094, 3266, 3440, 3613, 3787, 3959, 4133, 4306, 4480, 4652, 4826, 4999, 5172, 5346, 5519, 5693, 5865, 6039, 6212, 6386, 6558, 6732, 6905, 7079, 7251, 7425, 7598, 7771, 7944, 8118, 8291, 8464, 8638, 8811, 8985, 9157, 9331, 9504, 9678, 9850, 10024, 10197, 10371, 10543, 10717, 10890, 11063, 11236, 11410, 11584, 11756, 11930, 12103, 12277, 12449, 12623, 12796, 12970, 13142, 13316, 13489, 13662]
    攻击次数 = 12

    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.16
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.25
            self.CD *= 0.88


class 技能15(主动技能):
    名称 = 'FM92SW刺弹炮'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 19

    data0 = [0, 29776, 32788, 35804, 38832, 41852, 44880, 47892, 50920, 53936, 56964, 59980, 63004, 66020, 69040, 72068, 75084, 78108, 81124, 84152, 87168, 90192, 93208, 96240, 99256, 102272, 105296, 108312, 111340, 114356, 117384, 120396, 123428, 126444, 129472, 132488, 135500, 138528, 141544, 144572, 147588, 150616, 153632, 156660, 159676, 162704, 165716, 168732,
          171760, 174776, 177804, 180820, 183848, 186864, 189892, 192904, 195932, 198948, 201964, 204992, 208008, 211036, 214052, 217080, 220096, 223120, 226136, 229164, 232180, 235200, 238224]

    data0 = [(i*1.0) for i in [0, 7194, 7923, 8654, 9384, 10113, 10844, 11573, 12303, 13034, 13763, 14493, 15222, 15953, 16683, 17412, 18143, 18873, 19602, 20332, 21062, 21792, 22522, 23252, 23982, 24711, 25441, 26172, 26901, 27631, 28361, 29091, 29821, 30550, 31281, 32010, 32740, 33471, 34200, 34930, 35659, 36390, 37120, 37849, 38580, 39309, 40039, 40770, 41499, 42229, 42958, 43689, 44419, 45148, 45879, 46608, 47338, 48069, 48798, 49528, 50257, 50988, 51718, 52447, 53178, 53907, 54637, 55367, 56097, 56827, 57556]]
    攻击次数 = 4
    data1 =[(i*1.0) for i in [0,842, 928, 1013, 1098, 1184, 1270, 1355, 1440, 1525, 1612, 1697, 1782, 1867, 1954, 2039, 2124, 2209, 2296, 2381, 2466, 2551, 2637, 2723, 2808, 2894, 2979, 3065, 3150, 3236, 3321, 3406, 3492, 3578, 3663, 3748, 3834, 3920, 4005, 4090, 4175, 4262, 4347, 4432, 4517, 4604, 4689, 4774, 4859, 4945, 5031, 5116, 5202, 5287, 5373, 5458, 5544, 5629, 5714, 5800, 5886, 5971, 6056, 6142, 6228, 6313, 6398, 6483, 6570, 6655, 6740]]
    攻击次数2 = 12
    # 灼烧攻击力,在点TP之后删除
    data2 = [(i*1.0 for i in [0,28, 31, 34, 36, 39, 42, 45, 48, 51, 53, 56, 59, 62, 65, 68, 70, 73, 76, 79, 82, 85, 87, 90, 93, 96, 99, 102, 104, 107, 110, 113, 116, 119, 121, 124, 127, 130, 133, 136, 138, 141, 144, 147, 150, 153, 155, 158, 161, 164, 167, 170, 172, 175, 178, 181, 184, 187, 189, 192, 195, 198, 201, 204, 206, 209, 212, 215, 218, 221, 223])]
    攻击次数3 = 0

    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级]*self.攻击次数 + self.data1[self.等级]*self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.305


class 技能16(被动技能):
    名称 = '重火器改良'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 技能17(主动技能):
    名称 = '地脉震荡器'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 17

    data1 = [int(i*1.0) for i in [0,2376, 2617, 2858, 3099, 3341, 3581, 3822, 4063, 4304, 4546, 4787, 5028, 5268, 5510, 5751, 5992, 6233, 6475, 6716, 6956, 7197, 7438, 7680, 7921, 8162, 8403, 8645, 8885, 9126, 9367, 9608, 9850, 10091, 10332, 10572, 10813, 11055, 11296, 11537, 11778, 12020, 12260, 12501, 12742, 12984, 13225, 13466, 13707, 13947, 14189, 14430, 14671, 14912, 15154, 15395, 15636, 15876, 16117, 16359, 16600, 16841, 17082, 17324, 17564, 17805, 18046, 18287, 18529, 18770, 19011]]
    data2 = [int(i*1.0) for i in [0,8317, 9160, 10005, 10848, 11692, 12535, 13380, 14223, 15067, 15911, 16755, 17598, 18443, 19286, 20130, 20973, 21818, 22661, 23505, 24348, 25193, 26037, 26880, 27725, 28568, 29412, 30256, 31100, 31943, 32787, 33631, 34475, 35318, 36163, 37006, 37850, 38693, 39538, 40381, 41225, 42068, 42913, 43756, 44600, 45444, 46288, 47131, 47976, 48819, 49663, 50506, 51351, 52194, 53038, 53883, 54726, 55570, 56413, 57258, 58101, 58945, 59788, 60633, 61476, 62320, 63164, 64008, 64851, 65696, 66539]]
    data3 = [int(i*1.0) for i in [0,1781, 1962, 2143, 2324, 2505, 2686, 2867, 3048, 3229, 3410, 3589, 3770, 3951, 4132, 4313, 4494, 4675, 4856, 5037, 5217, 5397, 5578, 5759, 5940, 6121, 6302, 6483, 6664, 6845, 7025, 7206, 7387, 7568, 7749, 7929, 8110, 8291, 8472, 8653, 8833, 9014, 9195, 9376, 9557, 9738, 9919, 10100, 10280, 10460, 10641, 10822, 11003, 11184, 11365, 11546, 11727, 11908, 12089, 12268, 12449, 12630, 12811, 12992, 13173, 13354, 13535, 13716, 13897, 14077, 14258]]
    data4 = [int(i*1.0) for i in [0,4158, 4580, 5002, 5423, 5846, 6268, 6690, 7111, 7533, 7955, 8378, 8798, 9221, 9643, 10065, 10486, 10908, 11330, 11753, 12174, 12596, 13018, 13440, 13862, 14283, 14706, 15128, 15550, 15971, 16393, 16815, 17238, 17658, 18081, 18503, 18925, 19346, 19768, 20190, 20613, 21034, 21456, 21878, 22300, 22721, 23143, 23566, 23988, 24409, 24831, 25253, 25675, 26096, 26519, 26941, 27363, 27785, 28206, 28628, 29050, 29473, 29894, 30316, 30738, 31160, 31581, 32003, 32426, 32848, 33269]]
    data5 = [int(i*1.0) for i in [0,21981, 24212, 26441, 28671, 30902, 33131, 35361, 37592, 39822, 42051, 44282, 46512, 48741, 50972, 53202, 55432, 57662, 59892, 62122, 64351, 66582, 68812, 71043, 73272, 75502, 77733, 79963, 82192, 84422, 86653, 88882, 91112, 93343, 95573, 97802, 100033, 102263, 104492, 106723, 108953, 111183, 113413, 115643, 117873, 120103, 122333, 124563, 126794, 129023, 131253, 133484, 135713, 137943, 140174, 142404, 144633, 146864, 149094, 151323, 153554, 155784, 158014, 160243, 162474, 164704, 166933, 169164, 171394, 173625, 175854]]

    data0 = [data1, data2, data3, data4,data5]
    次数 = [1,1,1,6,1]

    CD = 40.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
           sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3324


class 技能18(主动技能):
    名称 = 'MSC7'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 14

    data1 = [int(i*1.0) for i in [0,5989, 6597, 7204, 7813, 8420, 9028, 9636, 10243, 10851, 11458, 12066, 12673, 13281, 13890, 14497, 15105, 15712, 16320, 16928, 17535, 18143, 18750, 19358, 19965, 20574, 21182, 21789, 22397, 23004, 23612, 24220, 24827, 25435, 26042, 26651, 27258, 27866, 28474, 29081, 29689, 30296, 30904, 31511, 32119, 32728, 33335, 33943, 34550, 35158, 35766, 36373, 36981, 37588, 38196, 38803, 39412, 40020, 40627, 41235, 41842, 42450, 43058, 43665, 44273, 44880, 45489, 46096, 46704, 47312, 47919]]
    data2 = [int(i*1.0) for i in [0,53909, 59378, 64847, 70316, 75786, 81255, 86723, 92192, 97662, 103131, 108600, 114069, 119538, 125008, 130476, 135945, 141414, 146884, 152353, 157822, 163291, 168761, 174229, 179698, 185167, 190636, 196106, 201575, 207044, 212512, 217982, 223451, 228920, 234389, 239859, 245328, 250797, 256265, 261734, 267204, 272673, 278142, 283611, 289081, 294549, 300018, 305487, 310956, 316426, 321895, 327364, 332832, 338302, 343771, 349240, 354709, 360179, 365648, 371117, 376585, 382054, 387524, 392993, 398462, 403931, 409401, 414870, 420338, 425807, 431277]]


    data0 = [data1,data2]
    次数 = [1,1]

    CD = 45.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
           sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3320


class 技能19(主动技能):
    名称 = '毁灭射线'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5

    data1 = [int(i*1.0) for i in [0,6677, 8226, 9774, 11323, 12871, 14420, 15968, 17517, 19066, 20614, 22163, 23711, 25260, 26808, 28357, 29905, 31454, 33003, 34551, 36100, 37648, 39197, 40745, 42294, 43842, 45391, 46939, 48488, 50037, 51585, 53134, 54682, 56231, 57779, 59328, 60876, 62425, 63974, 65522, 67071, 68618, 70166, 71715, 73264, 74812, 76361, 77909, 79458, 81006, 82555, 84103, 85652, 87201, 88749, 90298, 91846, 93395, 94943, 96492, 98040, 99589, 101137, 102686, 104235, 105783, 107332, 108880, 110429, 111977, 113526]]
    data2 = [int(i*1.0) for i in [0,100170, 123397, 146625, 169854, 193082, 216309, 239537, 262765, 285994, 309221, 332449, 355677, 378905, 402132, 425361, 448589, 471817, 495044, 518272, 541501, 564728, 587956, 611184, 634412, 657639, 680868, 704096, 727324, 750551, 773779, 797007, 820236, 843463, 866691, 889919, 913147, 936374, 959603, 982831, 1006059, 1029286, 1052514, 1075743, 1098971, 1122198, 1145426, 1168654, 1191881, 1215110, 1238338, 1261566, 1284793, 1308021, 1331249, 1354478, 1377705, 1400933, 1424161, 1447389, 1470616, 1493845, 1517073, 1540301, 1563528, 1586756, 1609985, 1633213, 1656440, 1679668, 1702896]]
    data0 = [data1,data2]
    次数 = [10,1]

    CD = 180.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
           sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率


class 技能20(被动技能):
    名称 = '连锁卫星'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = 'MLDRS95发射器'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 7

    data1 = [int(i*1.0) for i in [0,1971, 2170, 2370, 2570, 2771, 2971, 3170, 3370, 3570, 3770, 3971, 4171, 4370, 4570, 4770, 4970, 5171, 5370, 5570, 5770, 5970, 6169, 6370, 6570, 6770, 6970, 7170, 7369, 7570, 7770, 7970, 8170, 8369, 8569, 8770, 8970, 9170, 9369, 9569, 9769, 9970, 10170, 10370, 10569, 10769, 10969, 11170, 11370, 11569, 11769, 11969, 12169, 12370, 12569, 12769, 12969, 13169, 13369, 13570, 13769, 13969, 14169, 14369, 14568, 14769, 14969, 15169, 15369, 15568, 15768]]
    data2 = [int(i*1.0) for i in [0,88702, 97701, 106699, 115698, 124697, 133695, 142695, 151693, 160692, 169691, 178689, 187689, 196687, 205687, 214685, 223683, 232683, 241681, 250680, 259679, 268677, 277677, 286675, 295674, 304673, 313672, 322670, 331669, 340668, 349666, 358666, 367664, 376663, 385662, 394660, 403660, 412658, 421658, 430656, 439654, 448654, 457652, 466652, 475650, 484648, 493648, 502646, 511645, 520644, 529643, 538641, 547640, 556639, 565638, 574637, 583635, 592634, 601633, 610631, 619631, 628629, 637629, 646627, 655625, 664625, 673623, 682623, 691621, 700619, 709619]]
    data0 = [data1,data2]
    次数 = [15,1]

    CD = 60.0
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
           sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率


class 技能22(主动技能):
    名称 = '裂核轨道炮'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    # 基础 = 308971.0
    # 成长 = 93275.0
    # 倍率 = 1.201

    data1 = [int(i*1.0) for i in [0,9662, 11902, 14143, 16383, 18624, 20864, 23105, 25345, 27586, 29826, 32067, 34307, 36548, 38787, 41029, 43268, 45509, 47749, 49990, 52230, 54471, 56712, 58952, 61193, 63433, 65674, 67914, 70155, 72395, 74636, 76876, 79117, 81357, 83598, 85838, 88079, 90319, 92560, 94800, 97041, 99281, 101522, 103762, 106003, 108244, 110484, 112725, 114965, 117206, 119445, 121687, 123926, 126167, 128407, 130648, 132888, 135129, 137369, 139610, 141850, 144091, 146331, 148572, 150812, 153053, 155293, 157534, 159775, 162015, 164256]]
    data2 = [int(i*1.0) for i in [0,193242, 238051, 282862, 327671, 372482, 417291, 462100, 506911, 551720, 596531, 641340, 686151, 730960, 775770, 820580, 865389, 910199, 955009, 999819, 1044629, 1089439, 1134248, 1179058, 1223868, 1268678, 1313488, 1358297, 1403108, 1447917, 1492728, 1537537, 1582346, 1627157, 1671966, 1716777, 1761586, 1806396, 1851206, 1896016, 1940826, 1985635, 2030445, 2075255, 2120065, 2164875, 2209685, 2254494, 2299304, 2344114, 2388924, 2433734, 2478543, 2523354, 2568163, 2612974, 2657783, 2702592, 2747403, 2792212, 2837023, 2881832, 2926642, 2971452, 3016262, 3061072, 3105881, 3150691, 3195501, 3240311, 3285121]]
    data3 = [int(i*1.0) for i in [0,24155, 29756, 35357, 40959, 46559, 52161, 57762, 63364, 68965, 74565, 80167, 85768, 91370, 96971, 102571, 108173, 113774, 119376, 124977, 130578, 136179, 141780, 147382, 152983, 158584, 164185, 169787, 175388, 180989, 186591, 192191, 197793, 203394, 208996, 214597, 220197, 225799, 231400, 237002, 242603, 248203, 253805, 259406, 265008, 270609, 276210, 281811, 287413, 293014, 298615, 304216, 309817, 315419, 321020, 326622, 332222, 337823, 343425, 349026, 354628, 360228, 365829, 371431, 377032, 382634, 388234, 393836, 399437, 405038, 410640]]

    data0=[data1,data2,data3]

    次数 = [5,1,10]

    CD = 290.0
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
           sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率

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

重霄·枪炮师·男一觉序号 = 0
重霄·枪炮师·男二觉序号 = 0
重霄·枪炮师·男三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        重霄·枪炮师·男一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        重霄·枪炮师·男二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        重霄·枪炮师·男三觉序号 = 技能序号[i.名称]

重霄·枪炮师·男护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        重霄·枪炮师·男护石选项.append(i.名称)

重霄·枪炮师·男符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        重霄·枪炮师·男符文选项.append(i.名称)


class 重霄·枪炮师·男角色属性(角色属性):

    实际名称 = '重霄·枪炮师·男'
    角色 = '神枪手(男)'
    职业 = '枪炮师'

    武器选项 = ['手炮']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.957

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 重霄·枪炮师·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 重霄·枪炮师·男角色属性()
        self.角色属性A = 重霄·枪炮师·男角色属性()
        self.角色属性B = 重霄·枪炮师·男角色属性()
        self.一觉序号 = 重霄·枪炮师·男一觉序号
        self.二觉序号 = 重霄·枪炮师·男二觉序号
        self.三觉序号 = 重霄·枪炮师·男三觉序号
        self.护石选项 = deepcopy(重霄·枪炮师·男护石选项)
        self.符文选项 = deepcopy(重霄·枪炮师·男符文选项)
