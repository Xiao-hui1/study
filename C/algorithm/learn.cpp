#include <iostream>
#include <iomanip>  //格式控制的头文件
using namespace std;
// // class Box{
    
// // };
// class Student{
//     private:
//         int id;
//         string name;    //与c 语言不同c语言的字符串为char*变量名   在c++中为string
//         int *p;
//     public:
//         //声名并初始化构造函数
//         Student(int id, string name,int *p);
//         ~Student(){
//             cout<<"I will free"<< id << "space"<<endl;
//             delete p;
//         }
//         void input_data();     //普通类函数
//         Student(Student &p);    //拷贝函数 浅拷贝没有定义也可以直接调用类会自动生成
// };
// Student::Student(int id, string name,int *p):id(id),name(name),p(new int(10)){}    //使用参数表来声明形参变量
//         //构造  折构函数
// //拷贝函数的定义
// Student::Student(Student &r){
//     id = r.id;
//     name = r.name;
//     *p = *(r.p);
// }

// void Student::input_data(){
//     cout<<"you are id:"<<setiosflags(ios::left)<<setw(5)<<this->id<<this->name<<endl;
// }
// int main(){
//     int i,j;
//     //定义一个Student类的公用成员函数的指针变量
//     void (Student::*p)();
//     p = &Student::input_data;
//     //调用构造函数
//     int num[] ={1,3,5,7};
//     Student x(12,"libai",num);
//     //调用拷贝函数 拷贝x 函数
//     Student s(x);
// }
class Address;
class Point{
    private:
        int m_age;
        char* m_name;
    public:
        Point(int age,char* name):m_age(age),m_name(name){} //构造一个构造函数
        void show(const Address *p);      //声名组合函数

};
class Address{
    private:
        char* m_privince;
        char* m_communicty;
    public:
        Address(char* privince,char* communicty):m_privince(privince),m_communicty(communicty){}
        friend class Point;     //将整个类声明成Student类的友元函数
};
//定义组合函数
void Point::show(const Address *s){
    cout<<m_name<<"my age:"<<m_age<<endl;
    cout<<"your privince:"<<s->m_privince<<"your communcity"<<s->m_communicty<<endl;
}
int main()
{
    Point x(21,"libai");
    Address y("湖南省","衡阳市");       //注意友元函数可以调用另一个类的私有成员，但是组合函数只能调用公有成员
    x.show(&y);

}