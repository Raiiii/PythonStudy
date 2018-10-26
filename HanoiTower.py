# 利用递归函数移动汉诺塔:
def move(n,From,buffer,to):
    if n==1:
        print('Move',n,'from',From,'to',to)
    else:
        move(n-1,From,to,buffer)
        move(1,From,buffer,to)
        move(n-1,buffer,From,to)
move(4, "from", "buffer", "to")