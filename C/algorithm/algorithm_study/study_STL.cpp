#include <bits/stdc++.h>
using namespace std;
int main(){

    /**
     * .size()容器内的元素个数
     * .empty()判读容器是否为空，返回bool类型
     * .front()返回容器的第一个元素
     * .back()返回容器的最后一个元素
     * .begin()指向容器第一个元素的指针
     * .end()指向容器最后一个元素的下一个位置的指针
     * .swap(b)交换两个容器中的内容
     * ::iterator迭代器
     * 
     */
    vector<int>a(30);
    vector<int>a(20,33);//长度为20，值都为33
    vector<int>b(a);//copy a
    vector<int>b(a.begin()+3,a.end()-3);    //copy 指定区间
    a.insert(a.begin()+1,10); //插入
    a.erase(a.begin()+1); //删除omnhbgfdsxzZxazxz
    for(vector<int>::iterator it = a.begin();it<a.end();it++)
        cout<<*it;
    a.resize(10); //设置容器的大小为10，如果容器原本的大小大于10，那么超出10的部分会被丢弃掉。



    //--------------------------------栈-----------------------------------
    stack<int>s;
    s.push(23);
    s.pop();
    s.top(); //不会删除
    s.empty();
    s.size();

    // -------------------------------队列---------------------------------------
    queue<int>y;
    y.push(23);
    y.pop();
    y.front(); //取队头不会删除元素
    y.empty();
    y.size();



    //--------------------------------链表----i--------------------------------------
    list<int>i;
    list<int>j;
    i.merge(j); //将链表i与调用的链表合并，合并之前，两个链表必须时已经排序的，合并后排序的链表被保存在调用链表中，j为空
    i.remove(12);  //从链表中删除值为12的所有节点
    //i.splice(pos,j); //将链表b中的内容插入到pos的前面，j为空
    i.reverse(); //将链表翻转
    i.sort();   //将链表排序
    i.unique(); //将连续的相同元素压缩为单个元素。
    i.push_back(12);
    i.push_front(33);
    i.pop_front();
    i.pop_back();
    //i.insert(p,t); //在p之前插入t
    i.front();
    i.back();   //返回链表尾
    //i.erase(p); //删除p
    i.clear(); //清空链表



    //-----------------------------双端队列-----------------------------------------------
    deque<int> d[10];
    /**
     * push_front(x)/push_back(x)
     * pop_front()/pop_back()
     * front()/back()
     * size()
     * empty()
     * clear()
     */


     //-----------------------------优先队列---------------------------------------------------
     //内部使用堆进行实现，默认最大的在堆顶，不能直接移除指定的数
     priority_queue<int>p;
     p.push(12);
     p.pop();
     p.top();
     p.size();
     p.empty();

     

     //-----------------------------bitset-----------------------------------------------------
    bitset<100>e; //定义一个100位大小的二进制数e，初始值都为0
    // bitset<n> b(u); //b是unsigned long型的一个副本
    // bitset<n> b(s); //b是string对象s中含有的位串的副本
    // bitset<n> b(s, pos, n); //b是s中从位置pos开始的n位副本
    e.count();  //统计1的个数
    e.any();    //判断是否存在1
    e.none();   //判断是否全是0
    e.set();    //将所有位置设置为1
    e.set(2);   //将2位置的值设置为1
    e.set(2,0); //将2的位置位置为0
    e.reset();  //将所有位置都设置为0
    e.reset(2);
    e.flip();   //将所有位置取反
    e.flip(2);   //将2的位置取反
    e.size();   //返回大小
    e.to_ulong();  //返回它转换为unsigned long的结果，如果超出范围则会报错
    e.to_string();  //返回它转换为string的结果


    //-----------------------------set/multiset------------------------------------------------
    //set 和multiset set的键和值是统一的，内部不允许重复，multiset 允许多个值相同的键
    set<int>a; //升序
    set<int,greater<int> >a; //降序
    /*
        size/empty/clear
        begin/end
        insert(x)
        erase(x)
        erase(it) 删除it迭代器指向的元素
        find(x)
        count(x)    统计x的个数
        lower_bound/upper_bound 返回大于或等于x的最小元素位置、大于x的最小元素的位置
    */
    


    //---------------------------------map/multimap------------------------------------------------
    //map可以当作哈希表来使用
    map<string,int>mp; 
    map<string, int,greater<int> >mp; //降序
    /*
        size/empty/clear
        begin/end
        insert(x)
        erase(x)
        erase(it) 删除it迭代器指向的元素
        find(x)
    */




    //-----------------------------------STL常用函数----------------------------------------------------
    /*
        min(x,y)
        max(x,y)
        swap(x,y)
        find(begin,end,x)
        count(begin, end,x)
        reverse(begin, end)
        random_shuffle(begin,end)   随机打乱一个序列
        unique(begin, end)  将连续的相同元素压缩位一个元素，返回去重后的尾指针。不连续的相同元素不会被压缩，因此一般先排序
        fill(begin, end, val)   将区间[begin，end]的每个元素都设置位val
        sort(begin,end,compare)   compare 表示排序的比较函数，默认位升序
        nth_element(begin,begin+k,end,compare)  使区间[begin，end]第k小的元素处在第k个位置上，左边的元素都小与它，右边的元素都大于它，但并不保证其他元素有序
        lower_bound(begin, end, x)/upper_bound(begin,end,x) 两个函数都使用二分查找，在有序的数组中查找第一个满足条件的元素，返回指向该元素的指针
        next_permutation(begin, end)/pre_premutation(begin,end) next_permutation()要求按字典序的下一个排列的函数，可以得到全排列。

    */




    return 0;
}