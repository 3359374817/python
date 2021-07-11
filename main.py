import students as st
import guanliyuan as gly

i = [123]
BorrowedBooks = []
book = [["意林", 1],
        ["西游记", 2],
        ["红楼梦",3]]
#登
def kaishi():
    print("--------------------------")
    print("欢迎来到图书管理系统")
    print("请登录或注册")
    print("1、学生注册")
    print("2、学生登录")
    print("3、管理员注册")
    print("4、管理员登录")
    print("--------------------------")
    x = int(input("请输入你的操作:"))
    if x == 1:
        st.zhuce()
    elif x == 2:
        st.zzc()
    elif x == 3:
        gly.guanliyuan()
    elif x == 4:
        gly.glyzc()








if __name__ == "__main__":
    kaishi()
