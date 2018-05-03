# -*- coding:utf-8 -*-
import random

#用户选择游戏难度的模块。
def chiose():
    print "欢迎来到猜数字游戏，游戏会随机生成N位不重复的数字（默认为4位数，7步），在规定步数内，根据略微的提示，猜出完整的数字既为通关。"
#循环判断用户输入是否符合规定，不符合规定则输入到符合规定为止。
    while True:
        try:
            t=int(raw_input('选择难度，1为默认难度，2为自定义难度：'))
            break
        except Exception, e:
            print '请输入正确的数字。'
#判断用户的游戏类型选择
    if t == 1:
        difficulty(4,7)
    elif t == 2:
        #循环判断用户输入是否符合规定，不符合规定则输入到符合规定为止。
        while True:
            try:
                type_number=int(raw_input('请输入数字长度（范围为1-9位数），如果要4位数直接输入4即可：'))
                type_steps=int(raw_input('请输入需要使用的步数，默认为7:'))
                break
            except Exception, e:
                print '请输入正确的数字。'
        if 10 > type_number > 0:
            if type_steps > 0:
                difficulty(type_number,type_steps)
            else:
                print "请输入正确的步数"
                return chiose()
    else:
        print '请输入正确的数字。'
        print '\n'
        return chiose()

#用户自定义的难度，通过调用此模块传入参数到游戏模块
def difficulty(number,steps):
    num=''
    while len(str(num)) < number:
        rn=random.randint(1, 9)
        if str(rn) not in str(num):
            num=num+str(rn)
    game(num, steps)

#游戏模块
def game(num,steps):
#设置变量的初始值
    s=0
    cz=0
    zq=0
    pn=0
    print "游戏开始，数字为%s位数，步数为%s" % (len(str(num)),steps)
    print "\n"
#循环步数以内的次数，来使游戏在规定步数内完成。
    while 0 <= s < steps:
        cz = 0
        zq = 0
# 循环判断用户输入是否符合规定，不符合规定则输入到符合规定为止。
        while True:
            try:
                pn=int(raw_input('输入数字（%s位数）：' % len(str(num))))
                if len(str(pn)) == len(str(num)):
                    break
                else:
                    print '请输入正确的数字。'
            except Exception, e:
                print '请输入正确的数字。'
        #统计猜中的数字。
        for i in ','.join(str(pn)).split(','):
            if i in str(num):
                cz += 1
            else:
                pass
        print "您输入的数字中有%s个数字被随机数包含。" % cz
        #统计完全正确的数字。
        for i in range(len(str(num))):
            if ','.join(str(pn)).split(',')[i] == ','.join(str(num)).split(',')[i]:
                zq += 1
            else:
                pass
        print "您输入的数字，有%s个数字及位置完全填写正确。" % zq

        #判断是否通关成功
        if zq == len(str(num)):
            print "*********************************************"
            print "恭喜您通关，随机数为%s，您填写的数为%s" % (num,pn)
            print "*********************************************"
            s = -1
        else:
            s += 1
            print "您已使用%s步,还剩余%s步" % (s,int(steps) - int(s))
            print '\n'
        #判断是否通关失败
        if s == steps:
            print "很遗憾，游戏失败，随机数为%s还需继续努力。" % num
            break
        else:
            pass

    print "是否再来一把？？"
#循环判断用户输入是否符合规定，不符合规定则输入到符合规定为止。
    while True:
        try:
            replay = int(raw_input('1为重新开始，2为退出游戏：'))
            break
        except Exception, e:
            print '请重新输入'
    if replay == 1:
        chiose()
    else:
        print "再见！"

chiose()
