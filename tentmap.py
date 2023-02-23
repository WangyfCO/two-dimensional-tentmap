import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
a=0.43
b=0.57
x0=0.342780#0.342781
y0=0.543980#0.543981
x_list=[]
y_list=[]
i_list=[]
U_dict={}
fun_list=np.array([[1,9,9,5,5,5,5,9,9,0],[2,2,2,2,1,0,3,3,3,3],[6,6,9,9,5,5,9,9,0,8],
                   [6,6,1,9,5,5,9,0,8,8],[2,6,6,1,5,5,0,8,8,3],[2,2,2,2,0,1,3,3,3,3],
                   [2,6,6,0,4,4,1,8,8,3],[6,6,0,7,4,4,7,1,8,8],[6,0,7,7,4,4,7,7,1,8],
                   [0,7,7,4,4,4,4,7,7,1]])
h_list=[]
Z_list=[]
points_list=[[0 for i in range(10)] for j in range(10)]
#绘制三维点图
def draw(i_max):
    fig=plt.figure()
    #print(fig)
    ax=fig.add_subplot(projection="3d")
    #print(ax)
    ax.scatter(i_list,x_list,y_list,s=10,c='black')
    ax.set_zlabel('Y value', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('X value', fontdict={'size': 10, 'color': 'red'})
    ax.set_xlabel('Iteration number', fontdict={'size': 10, 'color': 'red'})
    ax.set_title('x='+str(x0)+',y='+str(y0)+',iteration='+str(i_max),fontdict={'size': 10, 'color': 'black'})
    plt.savefig('tent_map_x'+str(x0)+'_y'+str(y0)+'_a'+str(a)+'_b'+str(b)+'iteration'+str(i_max)+'.png')
    plt.show()

def points(x,y):
    i=0
    j=0
    while i<10:
        j=0
        while j<10:
            i1=i/10
            i2=(i+1)/10
            j1=j/10
            j2=(j+1)/10
            if x>=i1 and x<=i2 and y>=j1 and y<=j2:
                points_list[i][j]+=1
            j+=1
        i+=1
def max_min():
    min=1000
    max=1000
    i=0
    while i<10:
        j=0
        while j<10:
            if min>points_list[i][j]:
                min=points_list[i][j]
            if max<points_list[i][j]:
                max=points_list[i][j]
            j+=1
        i+=1
    print('min=',min,'max=',max)
def kafang_test():
    res=0
    for i in range(10):
        for j in range(10):
            temp=pow(points_list[i][j]-1000,2)/1000
            res+=temp
    print('kafang_res=',res)

def fun(x,y):
    i=0
    j=0
    while i<10:
        j=0
        while j<10:
            i1=i/10
            i2=(i+1)/10
            j1=j/10
            j2=(j+1)/10
            if x>=i1 and x<=i2 and y>=j1 and y<=j2:
                #print('i1=',i1,'i2=',i2,'j1=',j1,'j2=',j2)
                #print('U_list[',i,'][',j,']=',fun_list[i,j])
                return fun_list[i,j]
            j+=1
        i+=1
    

def two_tent_map(x0,y0,a,b):
    x=x0
    y=y0
    i=1
    i_max=100
    while i<(i_max+1):
        i_list.append(i)
        if x>=0 and x<=a and y>=0 and y<=b:
            x=x/a
            y=y/b
        elif x>=a and x<=1 and y>=0 and y<=b:
            x=(1-x)/(1-a)
            y=y/b
        elif x>=0 and x<=a and y>=b and y<=1:
            x=x/a
            y=(1-y)/(1-b)
        elif x>=a and x<=1 and y>=b and y<=1:
            x=(1-x)/(1-a)
            y=(1-y)/(1-b)
        x_list.append(x)
        y_list.append(y)
        points(x,y)
        #print('x=',x,',y=',y)
        N=fun(x,y)
        U_dict[i]=N
        i+=1

    #print(x_list)
    #print(y_list)
    draw(i_max)
    #print('points_list:',points_list)
    #max_min()
    #kafang_test()


def reverse(sv):
    #transform number sv into array
    while sv>=1:
        a=sv%10
        sv=int(sv/10)
        Z_list.append(a)
    cd=len(Z_list)
    i=0
    while i<cd/2:
        temp=Z_list[i]
        Z_list[i]=Z_list[cd-1-i]
        Z_list[cd-1-i]=temp
        i+=1
def found_hlist():
    for z in range(len(Z_list)):
        for i,n in U_dict.items():
            if n==Z_list[z]:
                h_list.append(i)
                break
def found_Z(h_list):
    value=0
    for h in range(len(h_list)):
        for i,n in U_dict.items():
            if i==h_list[h]:
                value=value*10+int(U_dict[i])
                break
    return value

def main(sv):
    reverse(sv)
    print(Z_list)
    #start to get tenp map
    two_tent_map(x0,y0,a,b)
    found_hlist()
    print('h_list',h_list)#iteration array h_list
    #if len(h_list)!=len(Z_list):
        #print('iteration number is too small!')
        
    return found_Z(h_list)

        
if __name__=="__main__":
    sv=1234567890
    #main(sv)
    value=main(sv)
    print("value=",value)
    
