students = []
zhanghao = []
import main as zjm
#注册
def zhuce():
    global xuehao, zhaohao, mima
    print("<---注册--->")
    print("请输入账号:")
    zhaohao = input()
    if len(zhaohao) < 8:
        print("输入的账号不正确")
        zhuce()
    elif len(zhaohao) > 8:
        print("输入的账号不正确")
        zhuce()
    print("请输入密码")
    mima = input()
    if len(mima) < 6:
        print("输入的密码不正确")
        zhuce()
    elif len(mima) > 6:
        print("输入的密码不正确")
        zhuce()
    print("请输入学号")
    xuehao = input()
    if len(xuehao) < 6:
        print("输入的学号不正确")
        zhuce()
    elif len(xuehao) > 6:
        print("输入的学号不正确")
        zhuce()
    print("请输入姓名：")
    name = input()
    zhanghao.append([zhaohao,mima])
    students.append([zhaohao,mima,xuehao,name])
    print(students)
    xzdl()


# 选择是否登录
def xzdl():
    print("是否登录")
    print("1、登录")
    print("2、返回主界面")
    denglu = input()
    if denglu == 1:
        xuesheng()
    elif denglu == 2:
        zjm.kaishi()
    else:
        print("输入错误")
        zjm.kaishi()


#查找书籍
def cz():
    bookname = input('请输入书名：')
    j = 0
    for i in zjm.book:
        if i[0] == bookname:
            j = 1
            print('书名：', i[0])
            print('序号：', i[1])
        elif bookname not in zjm.book:
            print("输入错误，没有你要找的书")
            chenggong()

#借阅书籍
def jy():
    print("请输入你要借阅的书籍名称")
    x = input()

#还书
def hs():
    print("请输入你要还的的书籍名称")
    x = input()


def chenggong():
    print("--------------------------")
    print("欢迎学生登录图书管理系统")
    print("1、查找书籍")
    print("2、借阅书籍")
    print("3、还书")
    print("4、退出登录")
    print("--------------------------")
    print("请输入你的操作")
    x = int(input())
    if x == 1:
        cz()
    elif x == 2:
        jy()
    elif x == 3:
        hs()
    elif x == 4:
        zjm.kaishi()

#登录
def xuesheng():
    print("请输入账号:")
    zhaohao = input()
    if len(zhaohao) < 8:
        print("输入的账号不正确")
        zhuce()
    elif len(zhaohao) > 8:
        print("输入的账号不正确")
        zhuce()
    print("请输入密码")
    mima = input()
    if len(mima) < 6:
        print("输入的密码不正确")
        zhuce()
    elif len(mima) > 6:
        print("输入的密码不正确")
        zhuce()
    if [zhaohao,mima] in students:
        print("登录成功")
        chenggong()
    else:
        print("你未注册")
        zhuce()

#学生是否注册
def zzc():
    print("是否注册\n1、已注册\n2、未注册\n")
    x = int(input())
    if x == 1:
        xuesheng()
    elif x == 2:
        zhuce()

