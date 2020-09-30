# -*- coding: utf-8 -*-

# 修改fahrenheit函数，完成正确的温度转换
def fahrenheit(celsius):
    return (9.0/5)*celsius+32.0

# 不能修改以下代码
def main():
    c = eval(input("输入要转换的温度（摄氏度）"))
    f = fahrenheit(c)
    print('%.2f\u2103 = %.2f\u2109' % (c, f))
    
if __name__ == '__main__':
    main()