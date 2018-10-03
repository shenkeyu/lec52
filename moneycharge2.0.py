"""
作者：sky
版本：2.0
功能：52周存钱
日期：20181003
"""
import math

saving1 = 0

def savemoney(money_par_week,increase_money,total_week):
    saving = 0
    money_list = [] #记录每周的数值

    for i in range(total_week):
        money_list.append(money_par_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i+1, money_par_week, saving))
        money_par_week += increase_money

    global saving1
    saving1 = saving

    return saving


def main():
    '''
    主函数
    '''

    money_par_week = float(input('请输入每周存入的金额：')) #每周存入的金额
    increase_money = float(input('请输入递增的金额：')) #递增的金额
    total_week = int(input('请输入总周数：')) #总周数
    saving = savemoney(money_par_week, increase_money, total_week) #账户累计
    print('52周总共存款为{}元'.format(saving))

    print('全局变量方式，52周总共存款为{}元'.format(saving))


if __name__ == '__main__':
    main()