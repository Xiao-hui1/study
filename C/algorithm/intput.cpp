#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    float i=1.3;
    cout<<i<<endl;
    /**
     *  oct 表示八进制
     *  hex 表示十六进制
     *  dec 表示十进制
     *  setprecision(n) 设置精度
     *  setw(n) 设置宽度
     *  fixed(n) 设置固定宽度
     *  setfill(char c) 以c表示的填充字符
     *  uppercase 以十六进制输出时字母大写
     *  skipws 在输出时跳过空白
     *  flush   刷新流
     *  showbase 输出前缀 0/0x
     *  scientific 以科学计数法的形式输出
     *  showpos 在输出正整数时加’+‘
     *  showpoint 在输出浮点数时加小数点
     * 
     * 
     * strchr() 查找字符
     * strrchr() 右侧查找字符
     * strstr() 查找字符串
     * strlwr() 转换为小写
     * strupr() 转换为大写
     * **/


    int j;
    cin>>j;
    int *data = new int[j]; //动态数组
    printf("%lf",i);
    return 0;
}