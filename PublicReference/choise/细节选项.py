# 第三页选项文本
# 行1行2条目必须相等
# 列1(选项) 列2(选项，技能) 不能修改删除
from PublicReference.equipment.基础函数 import *

表头名称1 = "基础细节"

列名称1 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "选项"]

# 1显示黄色字体(进图属性)
行名称1 = {
    "工会属性": 0,
    "训练官BUFF": 1,
    "戒指": 0,
    "婚房": 0,
    "冒险团": 0,
    "晶体契约": 1,
    "收集箱": 0,
    "勋章": 0,
    "名称装饰卡": 0,
    "副武器/盾牌": 0,
    "快捷栏纹章": 1,
    "宠物装备-红": 0,
    "宠物装备-蓝": 0,
    "宠物装备-绿": 0,
    "宠物附魔": 0,
    "站街修正": 0,
    "进图修正": 1,
}

表头名称2 = "附魔&徽章"

列名称2 = ["力智", "三攻", "属强", "徽力智", "徽三攻", "选项", "技能"]

行名称2 = {
    "上衣": 0,
    "下装": 0,
    "头肩": 0,
    "腰带": 0,
    "鞋": 0,
    "手镯": 0,
    "项链": 0,
    "戒指": 0,
    "左槽": 0,
    "右槽": 0,
    "耳环": 0,
    "武器": 0,
    "称号": 0,
    "光环": 0,
    "武器装扮": 0,
    "皮肤": 0,
    "时装": 0,
}

# 对应细节选项列表, -1表示没有
行1选项 = {
    "工会属性": [-1],
    "训练官BUFF": [-1],
    "戒指": [-1],
    "婚房": [-1],
    "冒险团": [-1],
    "晶体契约": [-1],
    "收集箱": [-1],
    "勋章": [x for x in range(17, 37)],
    "名称装饰卡": [-1],
    "副武器/盾牌": [-1],
    "快捷栏纹章": [8],
    "宠物装备-红": [8, 40, 42, 43, 9, 11, 12, 10, 38],
    "宠物装备-蓝": [-1],
    "宠物装备-绿": [-1],
    "宠物附魔": [-1],
    "站街修正": [-1],
    "进图修正": [37],
}

行2选项 = {
    "上衣": [-1],
    "下装": [-1],
    "头肩": [39, 41],
    "腰带": [39],
    "鞋": [39],
    "手镯": [-1],
    "项链": [-1],
    "戒指": [-1],
    "左槽": [16],
    "右槽": [-1],
    "耳环": [-1],
    "武器": [-1],
    "称号": [39],
    "光环": [13, 14, 15],
    "武器装扮": [-1],
    "皮肤": [-1],
    "时装": [-1],
}

# 对应细节选项列表, -1表示没有, 999表示读取技能栏
行2技能 = {
    "上衣": [-1],
    "下装": [-1],
    "头肩": [0, 2, 1],
    "腰带": [0, 2],
    "鞋": [0, 2],
    "手镯": [-1],
    "项链": [-1],
    "戒指": [-1],
    "左槽": [100],
    "右槽": [100],
    "耳环": [-1],
    "武器": [-1],
    "称号": [2, 1],
    "光环": [4, 6, 3, 5, 7],
    "武器装扮": [-1],
    "皮肤": [-1],
    "时装": [999],
}

文本框宽度 = 45
文本框间隔 = 10


#选项条目################################################################
class 细节选项条目0():
    描述 = 'Lv1-30(主动)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('主动', 1, 30, 1)


class 细节选项条目1():
    描述 = 'Lv1-35(主动)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('主动', 1, 35, 1)


class 细节选项条目2():
    描述 = 'Lv1-50(主动)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('主动', 1, 50, 1)


class 细节选项条目3():
    描述 = 'Lv1-20(所有)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('所有', 1, 20, 1)


class 细节选项条目4():
    描述 = 'Lv1-30(所有)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('所有', 1, 30, 1)


class 细节选项条目5():
    描述 = 'Lv20-30(所有)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('所有', 20, 30, 1)


class 细节选项条目6():
    描述 = 'Lv1-50(所有)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('所有', 1, 50, 1)


class 细节选项条目7():
    描述 = 'Lv1-80(所有)Lv+1'

    def 效果(self, 属性):
        属性.技能等级加成('所有', 1, 80, 1)


class 细节选项条目8():
    描述 = '白字 +8%'

    def 效果(self, 属性):
        属性.附加伤害加成(0.08)


class 细节选项条目9():
    描述 = '白字 +7%'

    def 效果(self, 属性):
        属性.附加伤害加成(0.07)


class 细节选项条目10():
    描述 = '白字 +6%'

    def 效果(self, 属性):
        属性.附加伤害加成(0.06)


class 细节选项条目11():
    描述 = '黄字 +7%'

    def 效果(self, 属性):
        属性.伤害增加加成(0.07)


class 细节选项条目12():
    描述 = '力智 +7%'

    def 效果(self, 属性):
        属性.百分比力智加成(0.07)


class 细节选项条目13():
    描述 = '三攻 +5%'

    def 效果(self, 属性):
        属性.百分比三攻加成(0.05)


class 细节选项条目14():
    描述 = '黄字 +5%'

    def 效果(self, 属性):
        属性.伤害增加加成(0.05)


class 细节选项条目15():
    描述 = '暴伤 +5%'

    def 效果(self, 属性):
        属性.暴击伤害加成(0.05)


class 细节选项条目16():
    描述 = '终伤 +3%'

    def 效果(self, 属性):
        属性.最终伤害加成(0.03)


class 勋章强化选项():
    def __init__(self, x=0):
        self.y = 勋章计算(50, '传说', x)
        self.描述 = '+{}(+{})'.format(x, self.y)

    def 效果(self, 属性):
        属性.力量 += self.y
        属性.智力 += self.y
        属性.体力 += self.y
        属性.精神 += self.y


class 细节选项条目17(勋章强化选项):
    def __init__(self):
        super().__init__(1)


class 细节选项条目18(勋章强化选项):
    def __init__(self):
        super().__init__(2)


class 细节选项条目19(勋章强化选项):
    def __init__(self):
        super().__init__(3)


class 细节选项条目20(勋章强化选项):
    def __init__(self):
        super().__init__(4)


class 细节选项条目21(勋章强化选项):
    def __init__(self):
        super().__init__(5)


class 细节选项条目22(勋章强化选项):
    def __init__(self):
        super().__init__(6)


class 细节选项条目23(勋章强化选项):
    def __init__(self):
        super().__init__(7)


class 细节选项条目24(勋章强化选项):
    def __init__(self):
        super().__init__(8)


class 细节选项条目25(勋章强化选项):
    def __init__(self):
        super().__init__(9)


class 细节选项条目26(勋章强化选项):
    def __init__(self):
        super().__init__(10)


class 细节选项条目27(勋章强化选项):
    def __init__(self):
        super().__init__(11)


class 细节选项条目28(勋章强化选项):
    def __init__(self):
        super().__init__(12)


class 细节选项条目29(勋章强化选项):
    def __init__(self):
        super().__init__(13)


class 细节选项条目30(勋章强化选项):
    def __init__(self):
        super().__init__(14)


class 细节选项条目31(勋章强化选项):
    def __init__(self):
        super().__init__(15)


class 细节选项条目32(勋章强化选项):
    def __init__(self):
        super().__init__(16)


class 细节选项条目33(勋章强化选项):
    def __init__(self):
        super().__init__(17)


class 细节选项条目34(勋章强化选项):
    def __init__(self):
        super().__init__(18)


class 细节选项条目35(勋章强化选项):
    def __init__(self):
        super().__init__(19)


class 细节选项条目36(勋章强化选项):
    def __init__(self):
        super().__init__(20)


class 细节选项条目37():
    描述 = '队友 +34%'

    def 效果(self, 属性):
        属性.队友增幅系数 *= 1.34


class 细节选项条目38():
    描述 = '白字 +4%'

    def 效果(self, 属性):
        属性.附加伤害加成(0.04)


class 细节选项条目39():
    描述 = '技攻 +3%'

    def 效果(self, 属性):
        属性.技能攻击力加成(0.03)


class 细节选项条目40():
    描述 = '三攻 +8%'

    def 效果(self, 属性):
        属性.百分比三攻加成(0.08)


class 细节选项条目41():
    描述 = '技攻 +2%'

    def 效果(self, 属性):
        属性.技能攻击力加成(0.02)


class 细节选项条目42():
    描述 = '力智 +8%'

    def 效果(self, 属性):
        属性.百分比力智加成(0.08)


class 细节选项条目43():
    描述 = '终伤 +8%'

    def 效果(self, 属性):
        属性.最终伤害加成(0.08)


细节选项列表 = ()
i = 0
while i >= 0:
    try:
        exec('细节选项列表 += (细节选项条目' + str(i) + '(),)')
        i += 1
    except:
        i = -1

细节选项序号 = dict()
for i in range(len(细节选项列表)):
    细节选项序号[细节选项列表[i].描述] = i
