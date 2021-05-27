# C++

[TOC]


## 1.C++ 中智能指针和指针的区别是什么？

### 普通指针，new
**普通指针赋值**
```c++
    int x;
    int y;
    int *p = &x;
    int *q = &y;

    x = 35;
    y = 46;

    p = q;      // at this point p is now pointing to the same memory address 
                // as q, both of them are pointing to the memory allocated to y

    *p = 90;    // this will also change the values in *q and y 

    cout << x << " " << y << endl;
    cout << *p << " " << *q << endl;

    return 0;
```

输出结果
```
35 90
90 90
```

**通过new创建指针**
- new是一个局部指针，在堆中开辟了一块内存空间，如果超出了new的作用域，就无法delete，并且也无法获取到该指针，但内存空间依然被分配，甚至在程序结束之后都在那儿，这就是所谓内存泄漏。
```c++
int a = 5;
{
int *p;
int *b = new int;
p = &a;
b = &a;
}
delete b;//Wrong. b is not defined
```
### 智能指针
由于 C++ 语言没有自动内存回收机制，程序员每次 new 出来的内存都要手动 delete。程序员忘记 delete，流程太复杂，最终导致没有 delete，异常导致程序过早退出，没有执行 delete 的情况并不罕见。
   如果使用智能指针，即使程序块过早结束，智能指针也能确保在内存不再需要时将其释放。

C++ 标准库（STL）中  头文件：#include <memory>


1. shared_ptr
2. unique_ptr
3. weak_ptr
4. auto_ptr（被 C++11 弃用）

---常用前两个

- shared_ptr    
	- 多个智能指针可以共享同一个对象，对象的最末一个拥有着有责任销毁对象，并清理与该对象相关的所有资源。

	- 支持定制型删除器（custom deleter），可防范 Cross-DLL 问题（对象在动态链接库（DLL）中被 new 创建，却在另一个 DLL 内被 delete 销毁）、自动解除互斥锁
```c++
shared_ptr<int> p3 = make_shared<int>(42);
shared_ptr<string> p4 = make_shared<string>(10,'9');
shared_ptr<int> p5 = make_shared<int>();

```

- unique_ptr
	- unique_ptr 是 C++11 才开始提供的类型，是一种在异常时可以帮助避免资源泄漏的智能指针。采用独占式拥有，意味着可以确保一个对象和其相应的资源同一时间只被一个 pointer 拥有。一旦拥有着被销毁或编程 empty，或开始拥有另一个对象，先前拥有的那个对象就会被销毁，其任何相应资源亦会被释放。

	- unique_ptr 用于取代 auto_ptr

```c++
//将所有权从p1（指向string Stegosaurus）转移给p2
unique_ptr<string> p2(p1.release());//release将p1置为空
unique_ptr<string>p3(new string("Trex"));
//将所有权从p3转移到p2
p2.reset(p3.release());//reset释放了p2原来指向的内存
```
### 对比，区别
- 智能指针不需要手动删除，过了他的使用周期会自动删除
- 智能指针是对普通指针的封装，更方便管理一个对象的生命期
- 智能指针实质是一个对象，表现为一个指针


## 2.简述 C++ 右值引用与转移语义

### 左值和右值
	- 左值 表示存储在计算机内存的对象，左值相当于地址值。
	- 右值 当一个符号或者常量放在操作符右边时，计算机读取他的右值，也就是其代表的真实值
L-value中的L指的是Location，表示可寻址。A value (computer science)that has an address.

R-value中的R指的是Read，表示可读。in computer science, a value that does not have an address in a computer language.

###右值引用
右值引用 (Rvalue Referene) 是 C++ 新标准 (C++11, 11 代表 2011 年 ) 中引入的新特性 , 它实现了转移语义 (Move Sementics) 和精确传递 (Perfect Forwarding)。它的主要目的有两个方面：

- 消除两个对象交互时不必要的对象拷贝，节省运算存储资源，提高效率。
- 能够更简洁明确地定义泛型函数。

```c++
void process_value(int& i) {
    std::cout << "LValue processed: " << i << std::endl;
}

void process_value(int&& i) {
    std::cout << "RValue processed: " << i << std::endl;
}

void forward_value(int&& i) {
    //  在函数传递中i被认为是命名对象。
    process_value(i);
}

int main() {
    int a = 0;
    process_value(a);
    process_value(1);
    forward_value(2);
}
```
output
```
LValue processed: 0
RValue processed: 1
LValue processed: 2
```

### 转移语义

- 转移语义可以将资源 ( 堆，系统对象等 ) 从一个对象转移到另一个对象，这样能够减少不必要的临时对象的创建、拷贝以及销毁，能够大幅度提高 C++ 应用程序的性能。临时对象的维护 ( 创建和销毁 ) 对性能有严重影响。
- 在现有的 C++ 机制中，我们可以定义拷贝构造函数和赋值函数。要实现转移语义，需要定义转移构造函数，还可以定义转移赋值操作符。对于右值的拷贝和赋值会调用转移构造函数和转移赋值操作符。如果转移构造函数和转移拷贝操作符没有定义，那么就遵循现有的机制，拷贝构造函数和赋值操作符会被调用

```c++
#include <cassert>
#include <iostream>
#include <cstring>

using namespace std;

class String
{
    private :
    char *_data;
    int _len;

    void init(const char* s)
    {
        _data=new char[_len+1];
        memcpy(_data,s,_len);
        _data[_len]='\0';
    }

    public:
    String():_data(nullptr),_len(0){}
    String(const char* str)
    {
        assert(str!=nullptr);
        _len=strlen(str);
        init(str);
    }

    String(const String& str)
    {
        cout<<"call cctor"<<endl;
        _len=str._len;
        init(str._data);
    }

    String& operator=(const String& str)
    {
        cout<<"call copy assignment"<<endl;
        if(this!=&str)
        {
        _len=str._len;
        init(str._data);
        }
        return *this;
    }

    //转移构造函数（C++11）
    String(String&& str)
    {
        cout<<"call move ctor"<<endl;
        _len=str._len;
        _data=str._data;
        str._data=nullptr;
        str._len=0;
    }

    //转移赋值操作符（C++11）
    String& operator=(String&& str)
    {
        cout<<"call move assign"<<endl;
        if(this!=&str)
        {
        _len=str._len;
        _data=str._data;
        }
        return *this;
    }

    void print()
    {
        cout<<"data:"<<hex<<_data<<endl;
    }

    ~String()
    {
        cout<<"dctor"<<endl;
        if(_data)
        {
        delete[] _data;
        }
    }
};


int main()
{
    const char* s="hello world";
    String str(s);
    str.print();

    String tmp(String("hello"));
    tmp.print();

    String&& mstr=std::move(str);
    tmp=mstr;
    tmp.print();
}
```

**标准库函数std::move**

- 既然编译器只对右值引用才能调用转移构造函数和转移赋值函数，而所有命名对象都只能是左值引用，如果已知一个命名对象不再被使用而想对它调用转移构造函数和转移赋值函数，也就是把一个左值引用当做右值引用来使用，怎么做呢？标准库提供了函数 std::move，这个函数以非常简单的方式将左值引用转换为右值引用。

```c++
#include<iostream>
using namespace std;

template<class T>
void m_swap(T& a,T& b)
{
    T tmp(std::move(a));
    a=std::move(b);
    b=std::move(tmp);
}

int main()
{
    int a=0;
    int b=1;
    cout<<"before swap:"<<a<<" "<<b<<endl;

    m_swap(a,b);
    cout<<"after swap:"<<a<<" "<<b<<endl;
}
```

##3.C++ 中多态是怎么实现的  
- 多态，即多种状态（形态）。简单来说，我们可以将多态定义为消息以多种形式显示的能力。
- 多态是以封装和继承为基础的。
- C++ 多态分类及实现：
    1. 重载多态（Ad-hoc Polymorphism，编译期）：函数重载（子类与父类函数名一致属于重载多态）、运算符重载（命名 operate  <运算符> 的函数即运算符重载）
    2. 子类型多态（Subtype Polymorphism，运行期）：虚函数 *
    3. 参数多态性（Parametric Polymorphism，编译期）：类模板、函数模板
    4. 强制多态（Coercion Polymorphism，编译期/运行期）：基本类型转换、自定义类型转换

- 虚函数
	- 类里如果声明了虚函数，这个函数是实现的，哪怕是空实现，它的作用就是为了能让这个函数在它的子类里面可以被覆盖（override），这样的话，编译器就可以使用后期绑定来达到多态了。

**代码实现**(虚函数)

```c++
#include "stdio.h"
#include "conio.h"
class Parent
{    
public:
    char data[20];    
    void Function1();
    virtual void Function2(); // 这里声明Function2是虚函数    
}parent;
void Parent::Function1()
{
    printf("This is parent,function1\n");
}
void Parent::Function2()
{
    printf("This is parent,function2\n");
}
class Child: public Parent
{
    void Function1();
    void Function2();

} child;
void Child::Function1()
{
    printf("This is child,function1\n");
}
void Child::Function2()
{
    printf("This is child,function2\n");
}
int main(int argc, char* argv[])
{    
    Parent *p; // 定义一个基类指针    

    if ( _getch()=='c' ) // 如果输入一个小写字母c
        p=&child; // 指向继承类对象
    else
        p=&parent; // 否则指向基类对象

    p->Function1(); // 这里在编译时会直接给出Parent::Function1()的 入口地址。   
    p->Function2(); // 注意这里，执行的是哪一个Function2？

    return 0;
}

```
- 用任意版本的Visual C++或Borland C++编译并运行，输入一个小写字母c，得到下面的结果：
**This is parent,function1
This is child,function2**
- 为什么会有第一行的结果呢？因为我们是用一个Parent类的指针调用函数Fuction1()，虽然实际上这个指针指向的是Child类的对象，但编译器 无法知道这一事实（直到运行的时候，程序才可以根据用户的输入判断出指针指向的对象），它只能按照调用Parent类的函数来理解并编译，所以我们看到了 第一行的结果。

- 那么第二行的结果又是怎么回事呢？我们注意到，Function2()函数在基类中被virtual关键字修饰，也就是 说，它是一个虚函数。虚函数最关键的特点是“**动态联编**”，它可以在运行时判断指针指向的对象，并自动调用相应的函数。如果我们在运行上面的程序时任意输入 一个非c的字符，结果如下：
**This is parent,function1
This is parent,function2**

- 请注意看第二行，它的结果出现了变化。程序中仅仅调用了一个Function2()函数，却可以根据用户的输入自动决定到底调用基类中的Function2 还是继承类中的Function2，这就是虚函数的作用。把它定义为虚函数,可以保证时刻调用的是用户自己编写的函数。



##4.C++ 11 有什么新特性

### **auto**
auto: 让编译器自动推导出变量的类型，可以通过=右边的类型推导出变量的类型。
```c++
auto a = 10
```

### **左值右值**
- 左值：可以取地址并且有名字的东西就是左值。
- 右值：不能取地址的没有名字的东西就是右值。

### **列表初始化**
- 在C++11中可以直接在变量名后面加上初始化列表来进行对象的初始化

### **智能指针**
- std::shared_ptr
- std::weak_ptr
- std::unique_ptr

### **基于范围的for循环**
```c++
vector<int> vec;

for (auto iter = vec.begin(); iter != vec.end(); iter++) { // before c++11
    cout << *iter << endl;
}

for (int i : vec) { // c++11基于范围的for循环
    cout << "i" << endl;
}
```

### **nullptr**
- nullptr 是c++11 用来表示空指针引入的常量值，在c++中如果表示空指针语义时建议用nullptr而不是NULL，因为NULL本质上是个int型的0

```c++
void func(void *ptr) {
    cout << "func ptr" << endl;
}

void func(int i) {
    cout << "func i" << endl;
}

int main() {
    func(NULL); // 编译失败，会产生二义性
    func(nullptr); // 输出func ptr
    return 0;
}
```

### **final & override**
- final 用于修饰一个类，表示禁止该类进一步派生和虚函数的进一步重载，override用于修饰派生类中的成员函数，表明该函数重写了基类函数

## 简述 C++ 中智能指针的特点，简述 new 与 malloc 的区别

C++中的智能指针
![](img/智能指针.png)
- std::shared_ptr
- std::unique_ptr
- std::weak_ptr

###new 与 malloc
- 1.申请内存所在位置，new在自由存储区（free store)上为对象分配内存，而malloc从堆上动态为对象分配内存
	1.凡是通过new进行内存申请，该内存即为自由存储区。而堆是操作系统中的术语，是操作系统维护的一块特殊内存

- 2.返回类型，new返回的是严格匹配对象的类型，malloc返回void （\*），需要强制转换成我们需要的类型

- 3.类型分配失败时返回值 new分配失败会报出 bac_alloc异常，malloc失败则会返回NULL

- 4.是否需要制定内存大小    new编译器会自动计算，而malloc需要显示指出所需内存的尺寸

- 5.是否需要调用构造函数和析构函数  new delete 调用  malloc则不需要调用

**总结**


|特征|new/delete|malloc/free|
|-|-|-|
|分配内存的位置   |自由存储区   |  堆 |
| 内存分配成功返回值   | 对象类型    | void\*    |
| 内存分配失败返回   |  抛出异常   |  NULL   |
| 分配内存   |  由编译器计算得出   |  需要指定大小   |
| 数组分配内存   |  可以直接处理数组new[]   |  需要给定数组长度 |
|内存扩充    |  自动扩充   | 需要使用realloc    |
| 调用构造函数和析构函数 | 调用 |不调用  |





## STL 中 vector 与 list 具体是怎么实现的？常见操作的时间复杂度是多少？

###vector&&list
- **vector**
	- 表示可以改变大小的数组的序列容器
	- 底层结构为数组，里面有一个指针指向一篇连续的地址空间，如果空间不够，需要重新分配内存，一般是当前大小的两倍
	- size()表示数组元素 capacity()表示数组有多大容量
- **list**
	- 是序列容容器，允许在序列中任何地方进行常数时间插入和删除操作，并在两个方向上进行迭代
	- 底层数据结构为双向列表，以节点为单位存放数据，节点在内存中的地址不一定连续，每次插入或删除一个元素，就配置或释放一个元素空间
	- 无序，可重复 
- **vector vs list**
|对比项   | vector  | list  |
| -   |  -  |   - |
|底层实现   | 数组  | 链表  |
| 是否支持随机访问  | 支持  | 不支持  |
| 分配内存  | 一次分配好，不够的话重新分配  | 每次插入新节点进行内存申请  |
| 插入删除  | 需要遍历O(N)  | O(1)  |
|  有序访问下标  |  O(1)  |  O(N)  |

