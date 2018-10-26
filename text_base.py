bool = False
users = {"admin":"123456"}
while(True):
    print("欢迎来到python之家")
    print("1.登录系统")
    print("2.注册用户")
    login = input("请选择操作:")
    if login == "1":
        username = input("请输入你的用户名:")
        password = input("请输入密码:")
        if username in users and users[username] == password:
            bool = True
            print("登录成功!")
            print("%s! 欢迎登录python之家" %username)
            break
        else:
            print("用户名或密码错误请重新输入.")
            continue;
    if login == "2":
        registerUsername = input("请输入你的用户名:")
        registerPassword = input("请输入密码:")
        if registerUsername == '' or registerPassword == '':
            print("用户名或密码不能为空")
            continue
        else:
            users[registerUsername] = registerPassword
            print("注册成功,请前往登录.")
            continue
if bool:
    while(True):
        print("===================菜单====================")
        print("1.成绩评测")
        print("2.体重评测")
        select = input("请输入要操作的序号:")
        if select == "1":
            oldPoint = float(input('请输入去年的成绩：'))
            newPoint = float(input('请输入今年的成绩：'))
            gapPoint = newPoint-oldPoint
            str1 = '提升'
            if gapPoint<0:
                str1 = '降低'
                gapPoint = -gapPoint
            str2 = '''你的的成绩从去年的%.1f%s到了今年的%.1f
            你的的成绩%s了{0:.1f}%%'''%(oldPoint,str1,newPoint,str1)
            print(str2.format(gapPoint/oldPoint*100))
        elif select == "2":
            height = float(input('请输入你的身高(CM)：'))
            weight = float(input('请输入你的体重(KG)：'))
            bim = weight/pow(height,2)
            if bim < 18.5:
                print("您的BIM %d, 体重过轻！" %bim)
            elif 18.5 <= bim <= 25:
                print("恭喜您！您的BIM%d, 体重过轻！" %bim)
            elif 25 <= bim <= 28:
                print("您的BIM %d, 体重过重！" %bim)
            elif 28 <= bim <= 32:
                print("您的BIM %d, 属于肥胖类型了！" %bim)
            elif bim > 32:
                print("警告：您的BIM %d, 严重肥胖！" %bim)
        is_continue = input("您是否想继续测试？ (Y/N)")
        if is_continue == "Y" or is_continue == 'y':
            continue
        else:
            print("程序退出")
            break
else:
    print("你还没有登录请前往登录")        