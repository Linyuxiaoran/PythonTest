class Myclass:
    """一个简单的类实例"""
    i  = 12345
    def f(self):
        return 'hello world'
    
#实例化类
x = Myclass()

#访问类的属性和方法
print("MyClass 类的属性i为:",x.i)
print("类方法f的输出为:",x.f())