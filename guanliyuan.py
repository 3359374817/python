glyd = []
import main as zjm
#管理员登录界面
def gly():
    print("--------------------------")
    print("欢迎管理员登录图书管理系统")
    print("1、查找书籍")
    print("2、添加书籍")
    print("3、删除书籍")
    print("4、退出登录")
    print("--------------------------")
    print("请输入你的操作")
    x = int(input())
    if x == 1:
        cz()
    elif x == 2:
        tjsj()
    elif x == 3:
        sc()
    elif x == 4:
        zjm.kaishi()

#管理员添加书籍
def tjsj():
    print("请输入你要添加的的书籍序号")
    y = input()
    print("请输入你要添加的的书籍名称")
    x = input()
    zjm.book.append([x,y])
    if [x,y] in zjm.book:
        print("添加成功")
    else:
        print("添加失败")


#管理员注册
def guanliyuan():
    print("请输入账号:")
    zhaohao = input()
    if len(zhaohao) < 8:
        print("输入的账号不正确")
        guanliyuan()
    elif len(zhaohao) > 8:
        print("输入的账号不正确")
        guanliyuan()
    print("请输入密码")
    mima = input()
    if len(mima) < 6:
        print("输入的密码不正确")
        guanliyuan()
    elif len(mima) > 6:
        print("输入的密码不正确")
        guanliyuan()
    glyd.append([zhaohao,mima])

#管理员登录
def dl():
    print("请输入账号:")
    zhaohao = input()
    if len(zhaohao) < 8:
        print("输入的账号不正确")
        guanliyuan()
    elif len(zhaohao) > 8:
        print("输入的账号不正确")
        guanliyuan()
    print("请输入密码")
    mima = input()
    if len(mima) < 6:
        print("输入的密码不正确")
        guanliyuan()
    elif len(mima) > 6:
        print("输入的密码不正确")
        guanliyuan()
    if [zhaohao,mima] in gly:
        print("登录成功")
        gly()
    else:
        print("您的账号或者密码输入错误")


#管理员是否注册
def glyzc():
    print("是否注册\n1、已注册\n2、未注册\n")
    x = int(input())
    if x == 1:
        dl()
    elif x == 2:
        guanliyuan()

# 选择是否登录
def xzdl():
    print("是否登录")
    print("1、登录")
    print("2、返回主界面")
    denglu = input()
    if denglu == 1:
        dl()
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
            cz()
#删除书籍
def sc():
    print("请输入你要删除的书籍序号")
    y = input()
    print("请输入你要删除的书籍名称")
    x = input()
    if [y,x] in zjm.book:
        zjm.book.remove([y,x])
        print("删除成功")