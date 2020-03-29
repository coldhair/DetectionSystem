s='''
主芯片
CPU辅槽
CPU类型
内容类型
集戚芯片
主板板型
USB投口
SXTA按口
PC1拥槽
供电模式
显卡插槽

Intel Z77
LGA 1155
Core i7/Core is/Core i3/Pentium
DDR3
声卡/网卡
ATX板型
10xUSB 2.0接口(6内置+4背板)
4xSATA II接口: 2xSATAII接口
3xPCI插槽
4+1+1相
PC-E 3.0标准, PCL-E 2.0标准
'''
p=s.strip().split('\n')

for i in range(int(len(p)/2)):
    px=p[i]+'--'+p[i+12]
    print(px)