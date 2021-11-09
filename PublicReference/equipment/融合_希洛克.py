class 希洛克属性():
    def 希洛克属性_输出(self, 属性, 希洛克选择状态, 守门人属强选择, x=0):
        数量 = [0] * 3
        选择 = 希洛克选择状态
        属强 = 守门人属强选择 * 5 + 15
        for i in range(15):
            数量[i % 3] += 选择[i]

        属性.装备描述 = x
        下装 = ''
        戒指 = ''
        辅助装备 = ''

        # 下装属性1
        if 数量[0] == 1:
            下装 += 属性.最终伤害加成(0.05)

        # 戒指属性1
        if 数量[1] == 1:
            戒指 += 属性.百分比三攻加成(0.05)

        # 辅助装备属性1
        if 数量[2] == 1:
            辅助装备 += 属性.技能攻击力加成(0.05)

        i = 0  # 奈克斯属性2
        if (选择[i * 3 + 0] + 选择[i * 3 + 1]) == 2:
            下装 += 属性.伤害增加加成(0.05)  # 下装
        if (选择[i * 3 + 1] + 选择[i * 3 + 2]) == 2:
            戒指 += 属性.暴击伤害加成(0.05)  # 戒指
        if (选择[i * 3 + 2] + 选择[i * 3 + 0]) == 2:
            辅助装备 += 属性.百分比力智加成(0.05)  # 辅助装备

        i = 1  # 暗杀者属性2
        if (选择[i * 3 + 0] + 选择[i * 3 + 1]) == 2:
            下装 += 属性.伤害增加加成(0.02)
            下装 += 属性.技能冷却缩减(1, 45, 0.2)  # 下装
        if (选择[i * 3 + 1] + 选择[i * 3 + 2]) == 2:
            戒指 += 属性.暴击伤害加成(0.03)
            戒指 += 属性.技能冷却缩减(60, 70, 0.2)  # 戒指
        if (选择[i * 3 + 2] + 选择[i * 3 + 0]) == 2:
            辅助装备 += 属性.百分比力智加成(0.03)
            辅助装备 += 属性.技能冷却缩减(75, 80, 0.17)  # 辅助装备

        i = 2  # 卢克西属性2
        if (选择[i * 3 + 0] + 选择[i * 3 + 1]) == 2:
            下装 += 属性.技能倍率加成(50, 0.17)
            下装 += 属性.技能倍率加成(85, 0.17)
            下装 += 属性.技能倍率加成(100, 0.10)  # 下装
        if (选择[i * 3 + 1] + 选择[i * 3 + 2]) == 2:
            戒指 += 属性.技能倍率加成(50, 0.17)
            戒指 += 属性.技能倍率加成(85, 0.17)
            戒指 += 属性.技能倍率加成(100, 0.10)  # 戒指
        if (选择[i * 3 + 2] + 选择[i * 3 + 0]) == 2:
            辅助装备 += 属性.技能倍率加成(50, 0.17)
            辅助装备 += 属性.技能倍率加成(85, 0.17)
            辅助装备 += 属性.技能倍率加成(100, 0.10)  # 辅助装备

        i = 3  # 守门人属性2
        if (选择[i * 3 + 0] + 选择[i * 3 + 1]) == 2:
            下装 += 属性.进图属强加成(属强)  # 下装
        if (选择[i * 3 + 1] + 选择[i * 3 + 2]) == 2:
            戒指 += 属性.进图属强加成(属强)  # 戒指
        if (选择[i * 3 + 2] + 选择[i * 3 + 0]) == 2:
            辅助装备 += 属性.进图属强加成(属强)  # 辅助装备

        i = 4  # 洛多斯属性2
        if (选择[i * 3 + 0] + 选择[i * 3 + 1]) == 2:
            下装 += 属性.伤害增加加成(0.04)  # 下装
        if (选择[i * 3 + 1] + 选择[i * 3 + 2]) == 2:
            戒指 += 属性.暴击伤害加成(0.04)  # 戒指
        if (选择[i * 3 + 2] + 选择[i * 3 + 0]) == 2:
            辅助装备 += 属性.百分比力智加成(0.04)  # 辅助装备
        属性.装备描述 = 0

        if x == 1:
            return {2: 下装, 7: 戒指, 9: 辅助装备}


希洛克 = 希洛克属性()
