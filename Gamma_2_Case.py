import random

money_spent = 0
money_earned = 0
case_opened = 0

mil_spec = 0             #军规
restricted = 0           #受限
classified = 0           #保密
covert = 0               #隐秘
exceedingly_rare = 0     #罕见

name_list = []
#品质
def random1():
    global money_spent,rare,mil_spec,restricted,classified,covert,exceedingly_rare
    x = random.randint(1,10000)
    if x>0 and x<=7992:
        rare = 1
    elif x>7992 and x<=9590:
        rare = 2
    elif x>9590 and x<=9910:
        rare = 3
    elif x>9910 and x<=9974:
        rare = 4
    else:
        rare = 5



#磨损 & 暗金
def random2():
    global abrasion,stattrak
    x = random.randint(1,5)
    abrasion = x
    y = random.randint(1,10)
    if y == 1:
        stattrak = 1



#物品
def random3():
    global item
    if rare == 1:
        x = random.randint(1,7)
    if rare == 2:
        x = random.randint(1,5)
    if rare == 3:
        x = random.randint(1,3)
    if rare == 4:
        x = random.randint(1,2)
    item = x



#修复错误
def fix():
    if (rare == 1 and ((item == 3 and abrasion == 1) or (item == 5 and abrasion == 5))) or (rare == 2 and item == 4 and abrasion == 5):
        return True



#主函数(输出名字)
def main_name():
    global rare,abrasion,stattrak
    if rare == 1:
        if item == 1:
            item_name = "P90"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 冷血无情"
        if item == 2:
            item_name = "CZ75"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 印花板"
        if item == 3:
            item_name = "内格夫"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 眩目"
        if item == 4:
            item_name = "FN57"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 斯康里娅"
        if item == 5:
            item_name = "G3SG1"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 通风机"
        if item == 6:
            item_name = "UMP45"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 简报"
        if item == 7:
            item_name = "XM1014"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 滑流"
    if rare == 2:
        if item == 1:
            item_name = "格洛克18型"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 鼬鼠"
        if item == 2:
            item_name = "沙漠之鹰"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 指挥"
        if item == 3:
            item_name = "SG 553"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 三巨头"
        if item == 4:
            item_name = "MAG-7"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 石雕"
        if item == 5:
            item_name = "SCAR-20"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 权力之心"
    if rare == 3:
        if item == 1:
            item_name = "AUG"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 席德.米德"
        if item == 2:
            item_name = "Tec-9"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 燃料喷射器"
        if item == 3:
            item_name = "MP9"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 气密"
    if rare == 4:
        if item == 1:
            item_name = "法玛斯"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 防滚架"
        if item == 2:
            item_name = "AK-47"
            if stattrak == 1:
                item_name = item_name + " (StatTrak™)"
            item_name = item_name + " | 霓虹革命"
    if rare == 5:
        item_name = "Knife"
        if stattrak == 1:
            item_name = item_name + " (StatTrak™) | 随机皮肤"
    
    if abrasion == 1:
        item_name = item_name + "(崭新出厂)"
    if abrasion == 2:
        item_name = item_name + "(略有磨损)"
    if abrasion == 3:
        item_name = item_name + "(久经沙场)"
    if abrasion == 4:
        item_name = item_name + "(破损不堪)"
    if abrasion == 5:
        item_name = item_name + "(战痕累累)"
    
    print("获得饰品: " + str(item_name))
    print("")
    print("已经开启的箱子数: "+str(case_opened))
    print("获得金额: "+str(money_earned))
    print("花费金额: "+str(money_spent))
    name_list.append(str(item_name))



#主函数(money_earned计算)
def main_money():
    print("尚未完成")

while True:
    for x in range(1,4):
        print("")
    print("""请问您要干什么？
    1.开箱
    2.查看已获得的所有饰品
    3.查看开到的皮肤品质数量
    4.离开""")
    do = int(input("请输入:"))
    for x in range(1,4):
        print("")
    if do == 1:
        while True:
            rare = 0
            abrasion = 0
            stattrak = 0
            item = 0
            random1()
            random2()
            random3()
            if fix():
                continue
            case_opened = case_opened + 1
            money_spent = money_spent + 18.18
            if rare == 1:
                mil_spec = mil_spec + 1
            if rare == 2:
                restricted = restricted + 1
            if rare == 3:
                classified = classified + 1
            if rare == 4:
                covert = covert + 1
            if rare == 5:
                exceedingly_rare = exceedingly_rare + 1
            main_name()
            break
    if do == 2:
        len_of_list = len(name_list)
        for x in range(0,len_of_list):
            print(str(x+1) +". "+name_list[x])
    if do == 3:
        print("您已经获得了" + str(case_opened) + "个饰品")
        print("军规级皮肤数: " + str(mil_spec))
        print("受限级皮肤数: " + str(restricted))
        print("保密级皮肤数: " + str(classified))
        print("隐秘级皮肤数: " + str(covert))
        print("罕见级皮肤数: " + str(exceedingly_rare))
    if do == 4:
        break