
#"上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石","武器"

class 奥兹玛属性():
    def 阿斯特罗斯等级加成(self, 属性, k):
        描述 = ''
        if 属性.职业 == '缔造者':
            if k == 0:
                描述 += 属性.技能等级加成('所有', 70, 70, 1)
                描述 += 属性.技能等级加成('所有', 80, 80, 1)
            if k == 1:
                描述 += 属性.技能等级加成('所有', 40, 40, 1)
                描述 += 属性.技能等级加成('所有', 50, 50, 1)
                描述 += 属性.技能等级加成('所有', 60, 60, 1)
            if k == 2:
                描述 += 属性.技能等级加成('所有', 10, 10, 1)
                描述 += 属性.技能等级加成('所有', 30, 30, 1)
        else:
            if k == 0:
                描述 += 属性.技能等级加成('主动', 70, 70, 1)
                描述 += 属性.技能等级加成('主动', 75, 75, 1)
                描述 += 属性.技能等级加成('主动', 80, 80, 1)
            if k == 1:
                描述 += 属性.技能等级加成('主动', 40, 40, 1)
                描述 += 属性.技能等级加成('主动', 45, 45, 1)
                描述 += 属性.技能等级加成('主动', 60, 60, 1)
            if k == 2:
                描述 += 属性.技能等级加成('主动', 20, 20, 1)
                描述 += 属性.技能等级加成('主动', 25, 25, 1)
                描述 += 属性.技能等级加成('主动', 35, 35, 1)
        return 描述

    def 奥兹玛属性_输出(self, 属性, 奥兹玛选择状态, 阿斯特罗斯选项, x = 0):
        选择 = 奥兹玛选择状态
        技能 = 阿斯特罗斯选项
        
        属性.装备描述 = x
        头肩 = ''
        腰带 = ''
        鞋 = ''
        项链 = ''
        魔法石 = ''
        
        # region 阿斯特罗斯
        i = 0 
        if 选择[0] == 1:
            头肩 += 属性.伤害增加加成(0.03)
            头肩 += 属性.暴击伤害加成(0.03)
            头肩 += 属性.附加伤害加成(0.02)
            头肩 += self.阿斯特罗斯等级加成(属性, 技能[i])
            i += 1
        if 选择[1] == 1:
            腰带 += 属性.百分比三攻加成(0.02)
            腰带 += 属性.百分比力智加成(0.03)
            腰带 += 属性.最终伤害加成(0.02)
            腰带 += self.阿斯特罗斯等级加成(属性, 技能[i])
            i += 1
        if 选择[2] == 1:
            鞋 += 属性.伤害增加加成(0.03)
            鞋 += 属性.暴击伤害加成(0.03)
            鞋 += 属性.附加伤害加成(0.01)
            鞋 += self.阿斯特罗斯等级加成(属性, 技能[i])
            i += 1
        if 选择[3] == 1:
            项链 += 属性.百分比三攻加成(0.02)
            项链 += 属性.百分比力智加成(0.03)
            项链 += 属性.最终伤害加成(0.02)
            项链 += self.阿斯特罗斯等级加成(属性, 技能[i])
            i += 1
        if 选择[4] == 1:
            魔法石 += 属性.附加伤害加成(0.03)
            魔法石 += 属性.百分比三攻加成(0.02)
            魔法石 += 属性.最终伤害加成(0.02)
            魔法石 += self.阿斯特罗斯等级加成(属性, 技能[i])
            i += 1
        # endregion
        # region 贝利亚斯
        if 选择[5] == 1:
            头肩 += 属性.伤害增加加成(0.03)
            头肩 += 属性.暴击伤害加成(0.03)
            头肩 += 属性.附加伤害加成(0.02)
        if 选择[6] == 1:
            腰带 += 属性.百分比三攻加成(0.02)
            腰带 += 属性.百分比力智加成(0.03)
            腰带 += 属性.最终伤害加成(0.02)
        if 选择[7] == 1:
            鞋 += 属性.伤害增加加成(0.03)
            鞋 += 属性.暴击伤害加成(0.03)
            鞋 += 属性.附加伤害加成(0.01)
        if 选择[8] == 1:
            项链 += 属性.百分比三攻加成(0.02)
            项链 += 属性.百分比力智加成(0.03)
            项链 += 属性.最终伤害加成(0.02)
        if 选择[9] == 1:
            魔法石 += 属性.附加伤害加成(0.03)
            魔法石 += 属性.百分比三攻加成(0.02)
            魔法石 += 属性.最终伤害加成(0.02)
        # endregion
        # region 雷德梅恩
        if 选择[10] == 1:
            头肩 += 属性.伤害增加加成(0.03)
            头肩 += 属性.暴击伤害加成(0.03)
            头肩 += 属性.附加伤害加成(0.02)
            头肩 += 属性.技能冷却缩减(45, 45, 0.1)
        if 选择[11] == 1:
            腰带 += 属性.百分比三攻加成(0.02)
            腰带 += 属性.百分比力智加成(0.03)
            腰带 += 属性.最终伤害加成(0.02)
            腰带 += 属性.技能冷却缩减(75, 75, 0.1)
        if 选择[12] == 1:
            鞋 += 属性.伤害增加加成(0.03)
            鞋 += 属性.暴击伤害加成(0.03)
            鞋 += 属性.附加伤害加成(0.01)
            鞋 += 属性.技能冷却缩减(70, 70, 0.1)
        if 选择[13] == 1:
            项链 += 属性.百分比三攻加成(0.02)
            项链 += 属性.百分比力智加成(0.03)
            项链 += 属性.最终伤害加成(0.02)
            项链 += 属性.技能冷却缩减(80, 80, 0.1)
        if 选择[14] == 1:
            魔法石 += 属性.附加伤害加成(0.03)
            魔法石 += 属性.百分比三攻加成(0.02)
            魔法石 += 属性.最终伤害加成(0.02)
            魔法石 += 属性.技能冷却缩减(60, 60, 0.1)
        # endregion
        # region 罗什巴赫
        if 选择[15] == 1:
            头肩 += 属性.伤害增加加成(0.03)
            头肩 += 属性.暴击伤害加成(0.03)
            头肩 += 属性.附加伤害加成(0.02)
        if 选择[16] == 1:
            腰带 += 属性.百分比三攻加成(0.02)
            腰带 += 属性.百分比力智加成(0.03)
            腰带 += 属性.最终伤害加成(0.02)
        if 选择[17] == 1:
            鞋 += 属性.伤害增加加成(0.03)
            鞋 += 属性.暴击伤害加成(0.03)
            鞋 += 属性.附加伤害加成(0.01)
        if 选择[18] == 1:
            项链 += 属性.百分比三攻加成(0.02)
            项链 += 属性.百分比力智加成(0.03)
            项链 += 属性.最终伤害加成(0.02)
        if 选择[19] == 1:
            魔法石 += 属性.附加伤害加成(0.03)
            魔法石 += 属性.百分比三攻加成(0.02)
            魔法石 += 属性.最终伤害加成(0.02)
        # endregion
        # region 泰玛特
        if 选择[20] == 1:
            头肩 += 属性.伤害增加加成(0.03)
            头肩 += 属性.暴击伤害加成(0.04)
            头肩 += 属性.附加伤害加成(0.02)
        if 选择[21] == 1:
            腰带 += 属性.百分比三攻加成(0.02)
            腰带 += 属性.百分比力智加成(0.04)
            腰带 += 属性.最终伤害加成(0.02)
        if 选择[22] == 1:
            鞋 += 属性.伤害增加加成(0.04)
            鞋 += 属性.暴击伤害加成(0.03)
            鞋 += 属性.附加伤害加成(0.02)
        if 选择[23] == 1:
            项链 += 属性.百分比三攻加成(0.03)
            项链 += 属性.百分比力智加成(0.03)
            项链 += 属性.最终伤害加成(0.02)
        if 选择[24] == 1:
            魔法石 += 属性.附加伤害加成(0.03)
            魔法石 += 属性.百分比三攻加成(0.02)
            魔法石 += 属性.最终伤害加成(0.03)
        # endregion
        属性.装备描述 = 0
        if x == 1:
            return {1: 头肩, 3: 腰带, 4: 鞋,  6: 项链, 10: 魔法石}

奥兹玛 = 奥兹玛属性()