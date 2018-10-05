"""
作者：sky
版本：3.0
功能：XX周存钱
日期：20181003
"""
import math
import datetime

def savemoney(money_par_week,increase_money,total_week):
    money_list = [] #记录每周的数值
    saving_monet_list = []

    for i in range(total_week):
        money_list.append(money_par_week)
        saving = math.fsum(money_list)
        saving_monet_list.append(saving)
        print('第{}周，存入{}元，账户累计{}元'.format(i+1, money_par_week, saving))
        money_par_week += increase_money

    return saving_monet_list


def main():
    '''
    主函数
    '''

    money_par_week = float(input('请输入每周存入的金额：')) #每周存入的金额
    increase_money = float(input('请输入递增的金额：')) #递增的金额
    total_week = int(input('请输入总周数：')) #总周数

    #input_date_str = input('请输入日期（yyyy/mm/dd）：')
    #input_date = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    input_date = datetime.datetime.now()
    week_num = int(input_date.isocalendar()[1])

    #查看当前日期，字符串和datetime转换
    #now = datetime.datetime.now()
    #str_now = datetime.datetime.strftime(now, '%d/%m/%Y')
    #print('当前日期为：{}'.format(str_now))

    if week_num < total_week:
        saving_list = savemoney(money_par_week, increase_money, total_week)  # 账户累计
        print('第{}周的存款为{}元。'.format(week_num, saving_list[week_num-1]))
    else:
        saving_list = savemoney(money_par_week, increase_money, week_num)
        print('总周数小于查询周数，重新计算后。第{}周的存款为{}元。'.format(week_num, saving_list[week_num-1]))



if __name__ == '__main__':
    main()