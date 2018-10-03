"""
作者：sky
版本：1.0
功能：52周存钱
日期：20181003
"""
import math

def main():
    '''
    主函数
    '''

    money_par_week = 10 #每周存入的金额
    weeki = 1 #记录周数
    increase_money = 10 #递增的金额
    total_week = 52 #总周数
    saving = 0 #账户累计

    money_list = [] #记录每周的数值

    while weeki <= total_week:
        money_list.append(money_par_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(weeki, money_par_week, saving))
        money_par_week += increase_money
        weeki += 1

    print('52周总共存款为{}元'.format(saving))


if __name__  == '__main__':
    main()