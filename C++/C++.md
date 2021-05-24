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



