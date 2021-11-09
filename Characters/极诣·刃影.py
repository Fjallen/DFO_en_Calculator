from PublicReference.carry.base import *

极诣·刃影等级 = 100 + 5

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
    名称 = '双重斩'
    所在等级 = 1
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,666, 733, 801, 869, 936, 1004, 1071, 1139, 1207, 1274, 1342, 1409, 1477, 1545, 1612, 1680, 1747, 1815, 1883, 1950, 2018, 2085, 2153, 2221, 2288, 2356, 2423, 2491, 2559, 2626, 2694, 2761, 2829, 2897, 2964, 3032, 3099, 3167, 3235, 3302, 3370, 3437, 3505, 3573, 3640, 3708, 3775, 3843, 3911, 3978, 4046, 4113, 4181, 4249, 4316, 4384, 4451, 4519, 4587, 4654, 4722, 4789, 4857, 4925, 4992, 5060, 5127, 5195, 5263, 5330]
    攻击次数 = 2
    # 基础 = 659.24 *2
    # 成长 = 6.75910912 *2
    CD = 4
    TP成长 = 0.08
    TP上限 = 5


class 技能1(职业主动技能):
    名称 = '鬼缚钉'
    备注 = '(TP为基础精通)'
    所在等级 = 5
    等级上限 = 1
    等级精通 = 1
    基础等级 = 1
    # 与基础精通关联
    data0 = [0,431]
    攻击次数 = 1
    data1 = [0,1006]
    攻击次数2 = 1
    # 基础 = 431 + 1005.98
    # 成长 = 0
    CD = 7
    TP成长 = 0.10
    TP上限 = 3

class 技能2(被动技能):
    名称 = '孤勇之志'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.02 * self.等级, 5)

    def 独立攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.02 * self.等级, 5)

class 技能3(职业主动技能):
    名称 = '冲击斩'
    所在等级 = 10
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 2357.721674
    # 成长 = 266.2974651
    data0 = [0,2624, 2891, 3157, 3423, 3689, 3956, 4222, 4488, 4755, 5021, 5287, 5554, 5820, 6086, 6352, 6619, 6885, 7151, 7418, 7684, 7950, 8216, 8483, 8749, 9015, 9282, 9548, 9814, 10080, 10347, 10613, 10879, 11146, 11412, 11678, 11944, 12211, 12477, 12743, 13010, 13276, 13542, 13808, 14075, 14341, 14607, 14874, 15140, 15406, 15672, 15939, 16205, 16471, 16738, 17004, 17270, 17536, 17803, 18069, 18335, 18602, 18868, 19134, 19401, 19667, 19933, 20199, 20466, 20732, 20998]
    攻击次数 = 1
    CD = 5
    TP成长 = 0.08
    TP上限 = 5


class 技能4(职业主动技能):
    名称 = '回旋勾斩'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,1075, 1185, 1294, 1403, 1512, 1621, 1730, 1839, 1949, 2058, 2167, 2276, 2385, 2494, 2604, 2713, 2822, 2931, 3040, 3149, 3258, 3368, 3477, 3586, 3695, 3804, 3913, 4022, 4132, 4241, 4350, 4459, 4568, 4677, 4787, 4896, 5005, 5114, 5223, 5332, 5441, 5551, 5660, 5769, 5878, 5987, 6096, 6205, 6315, 6424, 6533, 6642, 6751, 6860, 6970, 7079, 7188, 7297, 7406, 7515, 7624, 7734, 7843, 7952, 8061, 8170, 8279, 8389, 8498, 8607]
    data1 = [0,2659, 2929, 3198, 3468, 3738, 4008, 4278, 4547, 4817, 5087, 5357, 5627, 5896, 6166, 6436, 6706, 6976, 7245, 7515, 7785, 8055, 8324, 8594, 8864, 9134, 9404, 9673, 9943, 10213, 10483, 10753, 11022, 11292, 11562, 11832, 12102, 12371, 12641, 12911, 13181, 13451, 13720, 13990, 14260, 14530, 14799, 15069, 15339, 15609, 15879, 16148, 16418, 16688, 16958, 17228, 17497, 17767, 18037, 18307, 18577, 18846, 19116, 19386, 19656, 19925, 20195, 20465, 20735, 21005, 21274]
    # 基础 = 965.8692185 + 2389.265284
    # 成长 = 109.1547049 + 269.7777778
    攻击次数2 = 1
    CD = 8
    TP成长 = 0.08
    TP上限 = 5
class 技能5(职业主动技能):
    名称 = '封喉丝'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 801.4126225 + 4009.318751 + 5128.008658
    # 成长 = 90.54910002 + 452.690818 + 578.9769879
    # 可抓取伤害
    # "0": "[0,892, 982, 1073, 1164, 1254, 1345, 1435, 1526, 1616, 1707, 1797, 1888, 1978, 2069, 2159, 2250, 2341, 2431, 2522, 2612, 2703, 2793, 2884, 2974, 3065, 3155, 3246, 3336, 3427, 3518, 3608, 3699, 3789, 3880, 3970, 4061, 4151, 4242, 4332, 4423, 4513, 4604, 4695, 4785, 4876, 4966, 5057, 5147, 5238, 5328, 5419, 5509, 5600, 5690, 5781, 5872, 5962, 6053, 6143, 6234, 6324, 6415, 6505, 6596, 6686, 6777, 6867, 6958, 7049, 7139]
    # "1": "[0,4462, 4914, 5367, 5820, 6273, 6725, 7178, 7631, 8083, 8536, 8989, 9441, 9894, 10347, 10799, 11252, 11705, 12158, 12610, 13063, 13516, 13968, 14421, 14874, 15326, 15779, 16232, 16684, 17137, 17590, 18043, 18495, 18948, 19401, 19853, 20306, 20759, 21211, 21664, 22117, 22569, 23022, 23475, 23928, 24380, 24833, 25286, 25738, 26191, 26644, 27096, 27549, 28002, 28454, 28907, 29360, 29813, 30265, 30718, 31171, 31623, 32076, 32529, 32981, 33434, 33887, 34339, 34792, 35245, 35698]
    # "2": "[0,4462, 4914, 5367, 5820, 6273, 6725, 7178, 7631, 8083, 8536, 8989, 9441, 9894, 10347, 10799, 11252, 11705, 12158, 12610, 13063, 13516, 13968, 14421, 14874, 15326, 15779, 16232, 16684, 17137, 17590, 18043, 18495, 18948, 19401, 19853, 20306, 20759, 21211, 21664, 22117, 22569, 23022, 23475, 23928, 24380, 24833, 25286, 25738, 26191, 26644, 27096, 27549, 28002, 28454, 28907, 29360, 29813, 30265, 30718, 31171, 31623, 32076, 32529, 32981, 33434, 33887, 34339, 34792, 35245, 35698]
    # 无法抓取伤害
    data0 = [0,5707, 6286, 6865, 7444, 8023, 8602, 9181, 9760, 10339, 10918, 11497, 12076, 12655, 13234, 13813, 14392, 14971, 15549, 16128, 16707, 17286, 17865, 18444, 19023, 19602, 20181, 20760, 21339, 21918, 22497, 23076, 23655, 24234, 24813, 25392, 25971, 26550, 27129, 27708, 28287, 28866, 29445, 30024, 30603, 31182, 31761, 32340, 32919, 33498, 34077, 34656, 35235, 35814, 36393, 36972, 37551, 38130, 38709, 39288, 39867, 40446, 41025, 41604, 42183, 42762, 43341, 43920, 44499, 45078, 45657]
    # 无法抓取
    # 基础 = 5128.0164
    # 成长 = 578.9769879
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class 技能6(职业主动技能):
    名称 = '利刃旋风'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 772.7248804 + 1132.980861 + 371.9449761*5
    # 成长 = 87.27511962 + 127.9760766+ 42.02631579*5
    data0 = [0,860, 947, 1034, 1122, 1209, 1296, 1383, 1471, 1558, 1645, 1732, 1820, 1907, 1994, 2082, 2169, 2256, 2343, 2431, 2518, 2605, 2692, 2780, 2867, 2954, 3042, 3129, 3216, 3303, 3391, 3478, 3565, 3652, 3740, 3827, 3914, 4002, 4089, 4176, 4263, 4351, 4438, 4525, 4612, 4700, 4787, 4874, 4962, 5049, 5136, 5223, 5311, 5398, 5485, 5572, 5660, 5747, 5834, 5922, 6009, 6096, 6183, 6271, 6358, 6445, 6532, 6620, 6707, 6794, 6882]
    攻击次数 = 1
    data1 = [0,1261, 1389, 1517, 1645, 1773, 1901, 2029, 2157, 2285, 2413, 2541, 2669, 2797, 2925, 3053, 3180, 3308, 3436, 3564, 3692, 3820, 3948, 4076, 4204, 4332, 4460, 4588, 4716, 4844, 4972, 5100, 5228, 5356, 5484, 5612, 5740, 5868, 5996, 6124, 6252, 6380, 6508, 6636, 6764, 6892, 7020, 7148, 7276, 7403, 7531, 7659, 7787, 7915, 8043, 8171, 8299, 8427, 8555, 8683, 8811, 8939, 9067, 9195, 9323, 9451, 9579, 9707, 9835, 9963, 10091]
    攻击次数2 = 1
    data2 = [0,414, 456, 498, 540, 582, 624, 666, 708, 750, 792, 834, 876, 918, 960, 1002, 1044, 1086, 1128, 1170, 1212, 1254, 1296, 1339, 1381, 1423, 1465, 1507, 1549, 1591, 1633, 1675, 1717, 1759, 1801, 1843, 1885, 1927, 1969, 2011, 2053, 2095, 2137, 2179, 2221, 2263, 2305, 2347, 2389, 2431, 2473, 2515, 2557, 2600, 2642, 2684, 2726, 2768, 2810, 2852, 2894, 2936, 2978, 3020, 3062, 3104, 3146, 3188, 3230, 3272, 3314]
    攻击次数3 = 5
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


class 技能7(职业主动技能):
    名称 = '白牙落斩'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,6204, 6834, 7463, 8093, 8722, 9351, 9981, 10610, 11240, 11869, 12499, 13128, 13758, 14387, 15017, 15646, 16275, 16905, 17534, 18164, 18793, 19423, 20052, 20682, 21311, 21941, 22570, 23199, 23829, 24458, 25088, 25717, 26347, 26976, 27606, 28235, 28865, 29494, 30124, 30753, 31382, 32012, 32641, 33271, 33900, 34530, 35159, 35789, 36418, 37048, 37677, 38306, 38936, 39565, 40195, 40824, 41454, 42083, 42713, 43342, 43972, 44601, 45230, 45860, 46489, 47119, 47748, 48378, 49007, 49637]
    # 基础 = 5574.569378
    # 成长 = 629.4497608
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '疾刃之影'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,5412, 5961, 6510, 7059, 7608, 8157, 8706, 9255, 9804, 10353, 10902, 11451, 12001, 12550, 13099, 13648, 14197, 14746, 15295, 15844, 16393, 16942, 17491, 18040, 18589, 19138, 19688, 20237, 20786, 21335, 21884, 22433, 22982, 23531, 24080, 24629, 25178, 25727, 26276, 26825, 27374, 27924, 28473, 29022, 29571, 30120, 30669, 31218, 31767, 32316, 32865, 33414, 33963, 34512, 35061, 35610, 36160, 36709, 37258, 37807, 38356, 38905, 39454, 40003, 40552, 41101, 41650, 42199, 42748, 43297]
    # 基础 = 4862.907022
    # 成长 = 549.0547006
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = '薄暮利刃'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 5674.294582
    # 成长 = 640.7293418
    data0 = [0,6315, 6956, 7597, 8237, 8878, 9519, 10160, 10800, 11441, 12082, 12723, 13363, 14004, 14645, 15286, 15926, 16567, 17208, 17848, 18489, 19130, 19771, 20411, 21052, 21693, 22334, 22974, 23615, 24256, 24897, 25537, 26178, 26819, 27459, 28100, 28741, 29382, 30022, 30663, 31304, 31945, 32585, 33226, 33867, 34508, 35148, 35789, 36430, 37070, 37711, 38352, 38993, 39633, 40274, 40915, 41556, 42196, 42837, 43478, 44119, 44759, 45400, 46041, 46681, 47322, 47963, 48604, 49244, 49885, 50526]
    CD = 10
    TP成长 = 0.10
    TP上限 = 5



class 技能10(职业主动技能):
    名称 = '黑夜之花'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 1324.369105 + 620.8339029*5 + 4438.772386
    # 成长 = 149.6021873 + 70.17088175*5 + 501.2276145
    data0 = [0,691, 761, 832, 902, 972, 1042, 1112, 1182, 1253, 1323, 1393, 1463, 1533, 1603, 1674, 1744, 1814, 1884, 1954, 2024, 2095, 2165, 2235, 2305, 2375, 2445, 2516, 2586, 2656, 2726, 2796, 2866, 2937, 3007, 3077, 3147, 3217, 3287, 3358, 3428, 3498, 3568, 3638, 3709, 3779, 3849, 3919, 3989, 4059, 4130, 4200, 4270, 4340, 4410, 4480, 4551, 4621, 4691, 4761, 4831, 4901, 4972, 5042, 5112, 5182, 5252, 5322, 5393, 5463, 5533]
    攻击次数 = 5
    data1 = [0,1474, 1624, 1773, 1923, 2072, 2222, 2372, 2521, 2671, 2820, 2970, 3120, 3269, 3419, 3568, 3718, 3868, 4017, 4167, 4316, 4466, 4616, 4765, 4915, 5064, 5214, 5364, 5513, 5663, 5812, 5962, 6111, 6261, 6411, 6560, 6710, 6859, 7009, 7159, 7308, 7458, 7607, 7757, 7907, 8056, 8206, 8355, 8505, 8655, 8804, 8954, 9103, 9253, 9403, 9552, 9702, 9851, 10001, 10150, 10300, 10450, 10599, 10749, 10898, 11048, 11198, 11347, 11497, 11646, 11796]
    攻击次数2 = 1
    data2 = [0,4940, 5441, 5942, 6444, 6945, 7446, 7947, 8449, 8950, 9451, 9952, 10453, 10955, 11456, 11957, 12458, 12960, 13461, 13962, 14463, 14964, 15466, 15967, 16468, 16969, 17470, 17972, 18473, 18974, 19475, 19977, 20478, 20979, 21480, 21981, 22483, 22984, 23485, 23986, 24488, 24989, 25490, 25991, 26492, 26994, 27495, 27996, 28497, 28998, 29500, 30001, 30502, 31003, 31505, 32006, 32507, 33008, 33509, 34011, 34512, 35013, 35514, 36016, 36517, 37018, 37519, 38020, 38522, 39023, 39524]
    攻击次数3 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5


class 技能11(职业主动技能):
    名称 = '回旋十字斩'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 60
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 1035.089542/1.5
    # 成长 = 116.8721805/1.5
    # 基础2 = 8745.892003/1.5
    # 成长2 = 987.6008202/1.5
    data0 = [0,768, 846, 924, 1001, 1079, 1157, 1235, 1313, 1391, 1469, 1547, 1625, 1703, 1781, 1859, 1937, 2015, 2093, 2170, 2248, 2326, 2404, 2482, 2560, 2638, 2716, 2794, 2872, 2950, 3028, 3106, 3184, 3262, 3339, 3417, 3495, 3573, 3651, 3729, 3807, 3885, 3963, 4041, 4119, 4197, 4275, 4353, 4431, 4508, 4586, 4664, 4742, 4820, 4898, 4976, 5054, 5132, 5210, 5288, 5366, 5444, 5522, 5600, 5677, 5755, 5833, 5911, 5989, 6067, 6145]
    data1 = [0,6489, 7148, 7806, 8465, 9123, 9781, 10440, 11098, 11756, 12415, 13073, 13732, 14390, 15048, 15707, 16365, 17024, 17682, 18340, 18999, 19657, 20316, 20974, 21632, 22291, 22949, 23607, 24266, 24924, 25583, 26241, 26899, 27558, 28216, 28875, 29533, 30191, 30850, 31508, 32167, 32825, 33483, 34142, 34800, 35459, 36117, 36775, 37434, 38092, 38750, 39409, 40067, 40726, 41384, 42042, 42701, 43359, 44018, 44676, 45334, 45993, 46651, 47310, 47968, 48626, 49285, 49943, 50601, 51260, 51918]
    攻击次数 = 5
    攻击次数2 = 1
    CD = 18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    是否装备护石 = 0

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i*3.51) for i in self.data0]
            self.data1 = [int(i*2.21) for i in self.data1]
            # self.攻击次数 *= 3.51
            # self.攻击次数2 *= 2.21
            self.是否装备护石 = 1

class 技能12(被动技能):
    名称 = '刃之决意'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)


class 技能13(职业主动技能):
    名称 = '夜之风'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,4172, 4596, 5019, 5442, 5866, 6289, 6712, 7135, 7559, 7982, 8405, 8829, 9252, 9675, 10099, 10522, 10945, 11369, 11792, 12215, 12639, 13062, 13485, 13909, 14332, 14755, 15179, 15602, 16025, 16449, 16872, 17295, 17718, 18142, 18565, 18988, 19412, 19835, 20258, 20682, 21105, 21528, 21952, 22375, 22798, 23222, 23645, 24068, 24492, 24915, 25338, 25762, 26185, 26608, 27032, 27455, 27878, 28301, 28725, 29148, 29571, 29995, 30418, 30841, 31265, 31688, 32111, 32535, 32958, 33381]
    # 基础 = 5623.020335/1.5
    # 成长 = 634.9700957/1.5
    攻击次数 = 3
    CD = 20
    是否有护石 = 1
    TP成长 = 0.10
    TP上限 = 5

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i* 4.05) for i in self.data0]
            self.攻击次数 = 1


class 技能14(职业主动技能):
    名称 = '秘术·心斩'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,25243, 27804, 30365, 32926, 35487, 38048, 40609, 43169, 45730, 48291, 50852, 53413, 55974, 58535, 61096, 63657, 66218, 68779, 71340, 73901, 76462, 79022, 81583, 84144, 86705, 89266, 91827, 94388, 96949, 99510, 102071, 104632, 107193, 109754, 112315, 114876, 117436, 119997, 122558, 125119, 127680, 130241, 132802, 135363, 137924, 140485, 143046, 145607, 148168, 150729, 153289, 155850, 158411, 160972, 163533, 166094, 168655, 171216, 173777, 176338, 178899, 181460, 184021, 186582, 189142, 191703, 194264, 196825, 199386, 201947]
    # 基础 = 34147.01343/1.5
    # 成长 = 3717.48418/1.5
    CD = 40
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i* 1.30) for i in self.data0]
            # self.倍率 *= 1.30
            self.CD *= 0.9


class 技能15(被动技能):
    名称 = '收刀秘术'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.015 * self.等级, 5)

class 技能16(职业主动技能):
    名称 = '沉寂之狱'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    data0 = [0,22353, 27536, 32720, 37903, 43087, 48270, 53454, 58637, 63820, 69004, 74187, 79371, 84554, 89737, 94921, 100104, 105288, 110471, 115655, 120838, 126021, 131205, 136388, 141572, 146755, 151938, 157122, 162305, 167489, 172672, 177856, 183039, 188222, 193406, 198589, 203773, 208956, 214139, 219323, 224506, 229690, 234873, 240057, 245240, 250423, 255607, 260790, 265974, 271157, 276340, 281524, 286707, 291891, 297074, 302258, 307441, 312624, 317808, 322991, 328175, 333358, 338542, 343725, 348908, 354092, 359275, 364459, 369642, 374825, 380009]
    data1 = [0,47389, 58378, 69367, 80355, 91344, 102333, 113322, 124311, 135300, 146288, 157277, 168266, 179255, 190244, 201233, 212222, 223210, 234199, 245188, 256177, 267166, 278155, 289144, 300132, 311121, 322110, 333099, 344088, 355077, 366065, 377054, 388043, 399032, 410021, 421010, 431998, 442987, 453976, 464965, 475954, 486943, 497932, 508920, 519909, 530898, 541887, 552876, 563865, 574853, 585842, 596831, 607820, 618809, 629798, 640787, 651775, 662764, 673753, 684742, 695731, 706720, 717708, 728697, 739686, 750675, 761664, 772653, 783641, 794630, 805619]
    攻击次数2 = 1
    # 基础 = 17175.407 + 36398.086
    # 成长 = 5182.9665 + 10988.995
    CD = 145

    def 等效百分比(self, 武器类型):
        if self.等级 >= 9:
            self.data1 = [int(x*1.1) for x in self.data1]
        return super().等效百分比(武器类型)

class 技能17(职业主动技能):
    名称 = '瞬影碎魂击'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    # 基础 = 5573.170944/1.5 + 2609.408438*3/1.5 + 13046.79426/1.5
    # 成长 = 629.3170944/1.5 + 294.6107003*3/1.5 + 1473.205742/1.5
    data0 = [0,4135, 4554, 4974, 5393, 5813, 6233, 6652, 7072, 7491, 7911, 8330, 8750, 9169, 9589, 10008, 10428, 10847, 11267, 11686, 12106, 12525, 12945, 13365, 13784, 14204, 14623, 15043, 15462, 15882, 16301, 16721, 17140, 17560, 17979, 18399, 18818, 19238, 19658, 20077, 20497, 20916, 21336, 21755, 22175, 22594, 23014, 23433, 23853, 24272, 24692, 25111, 25531, 25950, 26370, 26790, 27209, 27629, 28048, 28468, 28887, 29307, 29726, 30146, 30565, 30985, 31404, 31824, 32243, 32663, 33082]
    data1 = [0,1936, 2132, 2328, 2525, 2721, 2918, 3114, 3311, 3507, 3703, 3900, 4096, 4293, 4489, 4686, 4882, 5078, 5275, 5471, 5668, 5864, 6060, 6257, 6453, 6650, 6846, 7043, 7239, 7435, 7632, 7828, 8025, 8221, 8418, 8614, 8810, 9007, 9203, 9400, 9596, 9792, 9989, 10185, 10382, 10578, 10775, 10971, 11167, 11364, 11560, 11757, 11953, 12150, 12346, 12542, 12739, 12935, 13132, 13328, 13525, 13721, 13917, 14114, 14310, 14507, 14703, 14899, 15096, 15292, 15489]
    攻击次数2 = 3
    data2 = [0,9680, 10662, 11644, 12627, 13609, 14591, 15573, 16555, 17537, 18519, 19501, 20483, 21466, 22448, 23430, 24412, 25394, 26376, 27358, 28340, 29322, 30304, 31287, 32269, 33251, 34233, 35215, 36197, 37179, 38161, 39143, 40126, 41108, 42090, 43072, 44054, 45036, 46018, 47000, 47982, 48964, 49947, 50929, 51911, 52893, 53875, 54857, 55839, 56821, 57803, 58786, 59768, 60750, 61732, 62714, 63696, 64678, 65660, 66642, 67625, 68607, 69589, 70571, 71553, 72535, 73517, 74499, 75481, 76463, 77446]
    攻击次数3 = 1
    CD = 25
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
            self.CD *= 0.8


class 技能18(职业主动技能):
    名称 = '追命索魂丝'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,27805, 30626, 33447, 36268, 39089, 41910, 44731, 47552, 50372, 53193, 56014, 58835, 61656, 64477, 67298, 70119, 72939, 75760, 78581, 81402, 84223, 87044, 89865, 92686, 95507, 98327, 101148, 103969, 106790, 109611, 112432, 115253, 118074, 120895, 123715, 126536, 129357, 132178, 134999, 137820, 140641, 143462, 146282, 149103, 151924, 154745, 157566, 160387, 163208, 166029, 168850, 171670, 174491, 177312, 180133, 182954, 185775, 188596, 191417, 194237, 197058, 199879, 202700, 205521, 208342, 211163, 213984, 216805, 219625, 222446]
    data1 = [0,11916, 13125, 14334, 15543, 16752, 17961, 19170, 20379, 21588, 22797, 24006, 25215, 26424, 27633, 28842, 30051, 31259, 32468, 33677, 34886, 36095, 37304, 38513, 39722, 40931, 42140, 43349, 44558, 45767, 46976, 48185, 49394, 50603, 51812, 53021, 54230, 55439, 56647, 57856, 59065, 60274, 61483, 62692, 63901, 65110, 66319, 67528, 68737, 69946, 71155, 72364, 73573, 74782, 75991, 77200, 78409, 79618, 80826, 82035, 83244, 84453, 85662, 86871, 88080, 89289, 90498, 91707, 92916, 94125, 95334]
    攻击次数2 = 1
    # 基础 = 37476.13847/1.5 + 16060.55728/1.5
    # 成长 = 4231.32564/1.5 + 1813.414016/1.5
    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27


class 技能19(被动技能):
    名称 = '无情夜行'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    冷却关联技能 = ['所有']
    非冷却关联技能 = ['沉寂之狱','黑曜真刃·破晓','秘术·雨夜终曲']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9

class 技能20(职业主动技能):
    名称 = '秘术·曜夜斩'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,61301, 67520, 73740, 79959, 86178, 92397, 98616, 104835, 111054, 117273, 123492, 129711, 135930, 142149, 148368, 154587, 160806, 167025, 173244, 179463, 185682, 191901, 198120, 204339, 210558, 216777, 222997, 229216, 235435, 241654, 247873, 254092, 260311, 266530, 272749, 278968, 285187, 291406, 297625, 303844, 310063, 316282, 322501, 328720, 334939, 341158, 347377, 353596, 359815, 366034, 372253, 378472, 384692, 390911, 397130, 403349, 409568, 415787, 422006, 428225, 434444, 440663, 446882, 453101, 459320, 465539, 471758, 477977, 484196, 490415]
    # 基础 = 55081.88836
    # 成长 = 6219.068581
    CD = 40
    是否有护石 = 1
    是否装备护石 = 0

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            self.是否装备护石 = 1



class 技能21(职业主动技能):
    名称 = '悬丝风暴'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔), 等级精通) + 1
    data0 = [0,8451, 9308, 10165, 11023, 11880, 12737, 13595, 14452, 15309, 16167, 17024, 17882, 18739, 19596, 20454, 21311, 22168, 23026, 23883, 24740, 25598, 26455, 27313, 28170, 29027, 29885, 30742, 31599, 32457, 33314, 34171, 35029, 35886, 36743, 37601, 38458, 39316, 40173, 41030, 41888, 42745, 43602, 44460, 45317, 46174, 47032, 47889, 48746, 49604, 50461, 51319, 52176, 53033, 53891, 54748, 55605, 56463, 57320, 58177, 59035, 59892, 60749, 61607, 62464, 63322, 64179, 65036, 65894, 66751, 67608]
    data1 = [0,12676, 13962, 15248, 16534, 17820, 19106, 20392, 21678, 22964, 24251, 25537, 26823, 28109, 29395, 30681, 31967, 33253, 34539, 35825, 37111, 38397, 39683, 40969, 42255, 43541, 44827, 46113, 47399, 48685, 49971, 51257, 52543, 53829, 55115, 56401, 57688, 58974, 60260, 61546, 62832, 64118, 65404, 66690, 67976, 69262, 70548, 71834, 73120, 74406, 75692, 76978, 78264, 79550, 80836, 82122, 83408, 84694, 85980, 87266, 88552, 89838, 91124, 92411, 93697, 94983, 96269, 97555, 98841, 100127, 101413]
    攻击次数2 = 1
    data2 = [0,23335, 25703, 28070, 30438, 32805, 35172, 37540, 39907, 42275, 44642, 47009, 49377, 51744, 54112, 56479, 58846, 61214, 63581, 65949, 68316, 70683, 73051, 75418, 77786, 80153, 82520, 84888, 87255, 89623, 91990, 94358, 96725, 99092, 101460, 103827, 106195, 108562, 110929, 113297, 115664, 118032, 120399, 122766, 125134, 127501, 129869, 132236, 134603, 136971, 139338, 141706, 144073, 146440, 148808, 151175, 153543, 155910, 158277, 160645, 163012, 165380, 167747, 170114, 172482, 174849, 177217, 179584, 181952, 184319, 186686]
    攻击次数3 = 1
    data3 = [0,2428, 2674, 2920, 3167, 3413, 3659, 3906, 4152, 4398, 4645, 4891, 5137, 5384, 5630, 5876, 6123, 6369, 6616, 6862, 7108, 7355, 7601, 7847, 8094, 8340, 8586, 8833, 9079, 9325, 9572, 9818, 10064, 10311, 10557, 10803, 11050, 11296, 11542, 11789, 12035, 12281, 12528, 12774, 13020, 13267, 13513, 13759, 14006, 14252, 14498, 14745, 14991, 15237, 15484, 15730, 15976, 16223, 16469, 16715, 16962, 17208, 17455, 17701, 17947, 18194, 18440, 18686, 18933, 19179, 19425]
    攻击次数4 = 14
    # 基础 = 7593.668262 + 11389.89633 + 20967.60766 + 2181.706539*14
    # 成长 = 857.3365231 + 1286.08453 + 2367.416268 + 246.3317384*14
    CD = 50
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.29
            self.CD *= 0.9


class 技能22(职业主动技能):
    名称 = '黑曜真刃·破晓'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    data0 = [0, 58618, 72210, 85803, 99395, 112988, 126580, 140173, 153766, 167358, 180951, 194543, 208136, 221729, 235321, 248914, 262506, 276099, 289692, 303284, 316877, 330469, 344062, 357654, 371247, 384840, 398432, 412025, 425617, 439210, 452803, 466395, 479988, 493580, 507173, 520765, 534358, 547951, 561543, 575136, 588728, 602321, 615914, 629506, 643099, 656691, 670284, 683877, 697469, 711062, 724654, 738247, 751839, 765432, 779025, 792617, 806210, 819802, 833395, 846988, 860580, 874173, 887765, 901358, 914951, 928543, 942136, 955728, 969321, 982913, 996506]
    # 基础 = 45028.23
    # 成长 = 13591.962
    攻击次数 = 3
    CD = 180


class 技能23(被动技能):
    名称 = '夜色杀意'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能24(职业主动技能):
    名称 = '绚烂之舞'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 基础 = 11663.94258 + 4081.952153*10 + 17495.4067 + 46657.16746
    # 成长 = 1317.014354 + 461.0143541*10 + 1975.598086 + 5267.808612
    data0 = [0, 12981, 14298, 15615, 16932, 18249, 19566, 20882, 22199, 23516, 24833, 26150, 27467, 28784, 30101, 31418, 32735, 34052, 35369, 36686, 38003, 39320, 40637, 41954, 43270, 44587, 45904, 47221, 48538, 49855, 51172, 52489, 53806, 55123, 56440, 57757, 59074, 60391, 61708, 63025, 64342, 65659, 66975, 68292, 69609, 70926, 72243, 73560, 74877, 76194, 77511, 78828, 80145, 81462, 82779, 84096, 85413, 86730, 88047, 89363, 90680, 91997, 93314, 94631, 95948, 97265, 98582, 99899, 101216, 102533, 103850]
    data1 = [0, 4543, 5004, 5465, 5926, 6387, 6848, 7309, 7769, 8230, 8691, 9152, 9613, 10074, 10535, 10996, 11457, 11918, 12379, 12840, 13301, 13762, 14222, 14683, 15144, 15605, 16066, 16527, 16988, 17449, 17910, 18371, 18832, 19293, 19754, 20215, 20676, 21136, 21597, 22058, 22519, 22980, 23441, 23902, 24363, 24824, 25285, 25746, 26207, 26668, 27129, 27589, 28050, 28511, 28972, 29433, 29894, 30355, 30816, 31277, 31738, 32199, 32660, 33121, 33582, 34042, 34503, 34964, 35425, 35886, 36347]
    攻击次数2 = 10
    data2 = [0, 19471, 21447, 23422, 25398, 27373, 29349, 31324, 33299, 35275, 37250, 39226, 41201, 43176, 45152, 47127, 49103, 51078, 53053, 55029, 57004, 58980, 60955, 62931, 64906, 66881, 68857, 70832, 72808, 74783, 76758, 78734, 80709, 82685, 84660, 86636, 88611, 90586, 92562, 94537, 96513, 98488, 100463, 102439, 104414, 106390, 108365, 110341, 112316, 114291, 116267, 118242, 120218, 122193, 124168, 126144, 128119, 130095, 132070, 134045, 136021, 137996, 139972, 141947, 143923, 145898, 147873, 149849, 151824, 153800, 155775]
    攻击次数3 = 1
    data3 = [0, 51925, 57192, 62460, 67728, 72996, 78264, 83531, 88799, 94067, 99335, 104602, 109870, 115138, 120406, 125673, 130941, 136209, 141477, 146745, 152012, 157280, 162548, 167816, 173083, 178351, 183619, 188887, 194155, 199422, 204690, 209958, 215226, 220493, 225761, 231029, 236297, 241565, 246832, 252100, 257368, 262636, 267903, 273171, 278439, 283707, 288974, 294242, 299510, 304778, 310046, 315313, 320581, 325849, 331117, 336384, 341652, 346920, 352188, 357455, 362723, 367991, 373259, 378527, 383794, 389062, 394330, 399598, 404865, 410133, 415401]
    攻击次数4 = 1
    CD = 60.0

class 技能25(职业主动技能):
    名称 = '秘术·雨夜终曲'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((极诣·刃影等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 对白牙
    data0 = [0, 46585, 57387, 68189, 78992, 89794, 100597, 111399, 122201, 133004, 143806, 154608, 165411, 176213, 187015, 197818, 208620, 219423, 230225, 241027, 251830, 262632, 273434, 284237, 295039, 305842, 316644, 327446, 338249, 349051, 359853, 370656, 381458, 392260, 403063, 413865, 424668, 435470, 446272, 457075, 467877, 478679, 489482, 500284, 511086, 521889, 532691, 543494, 554296, 565098, 575901, 586703, 597506, 608308, 619110, 629913, 640715, 651517, 662320, 673122, 683924, 694727, 705529, 716332, 727134, 737936, 748739, 759541, 770343, 781146, 791948]
    data1 = [0, 116463, 143468, 170474, 197480, 224486, 251492, 278498, 305504, 332510, 359516, 386522, 413528, 440534, 467539, 494545, 521551, 548557, 575563, 602569, 629575, 656581, 683587, 710593, 737599, 764605, 791610, 818616, 845622, 872628, 899634, 926640, 953646, 980652, 1007658, 1034664, 1061670, 1088676, 1115681, 1142687, 1169693, 1196699, 1223705, 1250711, 1277717, 1304723, 1331729, 1358735, 1385741, 1412747, 1439752, 1466759, 1493764, 1520770, 1547776, 1574782, 1601788, 1628794, 1655800, 1682806, 1709812, 1736818, 1763824, 1790829, 1817835, 1844841, 1871847, 1898853, 1925859, 1952865, 1979871]
    攻击次数2 = 1
    # "2": "[163048, 200856, 238664, 276473, 314281, 352089, 389897, 427706, 465514, 503322, 541131, 578939, 616747, 654555, 692364, 730172, 767980, 805789, 843597, 881405, 919213, 957022, 994830, 1032638, 1070447, 1108255, 1146063, 1183871, 1221680, 1259488, 1297296, 1335105, 1372913, 1410721, 1448529, 1486338, 1524146, 1561954, 1599763, 1637571, 1675379, 1713188, 1750996, 1788804, 1826612, 1864421, 1902229, 1940037, 1977845, 2015654, 2053462, 2091270, 2129079, 2166887, 2204695, 2242504, 2280312, 2318120, 2355928, 2393737, 2431545, 2469353, 2507161, 2544970, 2582778, 2620586, 2658395, 2696203, 2734011, 2771820]
    data2 = [0, 302803, 373019, 443234, 513449, 583665, 653880, 724096, 794311, 864526, 934742, 1004957, 1075173, 1145388, 1215603, 1285819, 1356034, 1426249, 1496465, 1566680, 1636896, 1707111, 1777326, 1847542, 1917757, 1987972, 2058188, 2128403, 2198619, 2268834, 2339049, 2409265, 2479480, 2549696, 2619911, 2690127, 2760342, 2830557, 2900773, 2970988, 3041203, 3111419, 3181634, 3251849, 3322065, 3392281, 3462496, 3532711, 3602926, 3673142, 3743357, 3813573, 3883788, 3954003, 4024219, 4094434, 4164650, 4234865, 4305080, 4375296, 4445511, 4515726, 4585942, 4656157, 4726372, 4796588, 4866804, 4937019, 5007234, 5077450, 5147665]
    攻击次数3 = 1
    # 对白牙
    # 基础 = 35782.96651 + 89457.89474 + 232587.0813
    # 成长 = 10802.00957 + 27005.07177 + 70215.98086
    攻击次数 = 1
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0

class 技能26(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['鬼缚钉']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

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

技能一觉序号 = 0
技能二觉序号 = 0
技能三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        技能一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        技能二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        技能三觉序号 = 技能序号[i.名称]

技能护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        技能护石选项.append(i.名称)

极诣·刃影符文选项 = ['无', '回旋勾斩', '封喉丝', '利刃旋风', '白牙落斩','疾刃之影', '薄暮利刃', '黑夜之花', '回旋十字斩', '夜之风', '秘术·心斩', '瞬影碎魂击', '追命索魂丝', '秘术·曜夜斩', '悬丝风暴']


class 极诣·刃影角色属性(角色属性):
    实际名称 = '极诣·刃影'
    角色 = '鬼剑士(女)'
    职业 = '刃影'

    武器选项 = ['太刀']

    类型选择 = ['物理固伤']

    类型 = '物理固伤'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2

    回旋十字斩形态开关 = 0
    秘术曜夜斩收刀 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        if self.技能栏[self.技能序号['回旋十字斩']].是否装备护石 == 1:
            if self.回旋十字斩形态开关 == 0:
                self.技能栏[self.技能序号['回旋十字斩']].攻击次数2 = 0
            else:
                self.技能栏[self.技能序号['回旋十字斩']].攻击次数 = 0
        if self.技能栏[self.技能序号['秘术·曜夜斩']].是否装备护石 == 1 and self.秘术曜夜斩收刀 == 1:
            self.技能栏[self.技能序号['秘术·曜夜斩']].倍率 *= 1.05



class 极诣·刃影(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·刃影角色属性()
        self.角色属性A = 极诣·刃影角色属性()
        self.角色属性B = 极诣·刃影角色属性()
        self.一觉序号 = 技能一觉序号
        self.二觉序号 = 技能二觉序号
        self.三觉序号 = 技能三觉序号
        self.护石选项 = deepcopy(技能护石选项)
        self.符文选项 = deepcopy(极诣·刃影符文选项)

    def 界面(self):

        super().界面()
        self.回旋十字斩形态开关 = QCheckBox('回旋十字斩空中施放', self.main_frame2)
        self.回旋十字斩形态开关.resize(150, 20)
        self.回旋十字斩形态开关.move(319, 360)
        self.回旋十字斩形态开关.setStyleSheet(复选框样式)
        self.回旋十字斩形态开关.setChecked(False)

        self.职业存档.append(('回旋十字斩形态开关', self.回旋十字斩形态开关, 0))

        self.秘术曜夜斩收刀 = QCheckBox('秘术·曜夜斩收刀', self.main_frame2)
        self.秘术曜夜斩收刀.resize(150, 20)
        self.秘术曜夜斩收刀.move(319, 380)
        self.秘术曜夜斩收刀.setStyleSheet(复选框样式)
        self.秘术曜夜斩收刀.setChecked(False)

        self.职业存档.append(('秘术·曜夜斩收刀', self.秘术曜夜斩收刀, 0))



    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.回旋十字斩形态开关.isChecked():
            属性.回旋十字斩形态开关 = 1
        if self.秘术曜夜斩收刀.isChecked():
            属性.秘术曜夜斩收刀 = 1
