#Protected examples - starts
class ProtectedClass:
    _ProtectedProperty="I am protected...@....ProtectedClass...!!"
    def __init__(self):
        pass
    def _ProtectedMethod(self):
        print("I am protected method...@...ProtectedClass...")
class DerivedProtectedClass(ProtectedClass):
    def Testcase(self):
        print("I am Test Case @ DerivedProtectedClass....", self._ProtectedProperty)
dc= DerivedProtectedClass()
dc.Testcase()
dc._ProtectedMethod()


class ProtectedClassV2:
    def __init__(self):
        self._ProtectedProperty="I am protected...@....ProtectedClassV2....!!"
    def _ProtectedMethod(self):
        print("I am protected method...@....ProtectedClassV2...")
class DerivedProtectedClassV2(ProtectedClassV2):
    def Testcase(self):
        print("I am Test Case @...DerivedProtectedClassV2....", self._ProtectedProperty)
dc2= DerivedProtectedClassV2()
dc2.Testcase()
dc2._ProtectedMethod()
#Protected examples - ends


#Private examples - starts
class PrivateClass:
    __PrivateProperty="I am Private...@....PrivateClass....!!"
    def __init__(self):
        pass
    def __PrivateMethod(self):
        print("I am Private method...@....PrivateClass...")
class DerivedPrivateClass(PrivateClass):
    def Testcase(self):
        pass
        #print("I am Test Case ", self.__PrivateProperty) Problem case
dc= DerivedPrivateClass()
dc.Testcase()
#dc.__PrivateMethod() problem case
pc=PrivateClass()
#print(pc.__PrivateProperty) problem case
#pc.__PrivateMethod() problem case

class PrivateClassV2:
    def __init__(self):
        self.__PrivateProperty="I am Private...@....PrivateClassV2....!!"
    def __PrivateMethod(self):
        print("I am Private method.....@....PrivateClassV2....")
class DerivedPrivateClassV2(PrivateClassV2):
    def Testcase(self):
        pass
        #print("I am Test Case ", self.__PrivateProperty) problem case
dc2= DerivedPrivateClassV2()
dc2.Testcase()
#dc2.__PrivateMethod() Problem case
pc=PrivateClass()
#print(pc.__PrivateProperty) problem case
#pc.__PrivateMethod() problem case
#Private examples - ends



#Public examples - starts
class PublicClass:
    PublicProperty="I am Public...@...PublicClass....!!"
    def __init__(self):
        pass
    def PublicMethod(self):
        print("I am Public method....@...PublicClass....")
class DerivedPublicClass(PublicClass):
    def Testcase(self):
        print("I am Test Case....@...DerivedPublicClass...", self.PublicProperty)
dc= DerivedPublicClass()
dc.Testcase()
print("I am object call...", dc.PublicProperty)
dc.PublicMethod()


class PublicClassV2:
    def __init__(self):
        self.PublicProperty="I am Public Property...@....PublicClassV2......!!"
    def PublicMethod(self):
        print("I am Public method...@...PublicClassV2 ")
class DerivedPublicClassV2(PublicClassV2):
    def Testcase(self):
        print("I am Test Case...@...DerivedPublicClassV2", self.PublicProperty)
dc2= DerivedPublicClassV2()
dc2.Testcase()
dc2.PublicMethod()
print(dc2.PublicProperty)

pc=PublicClass()
print(pc.PublicProperty)
pc.PublicMethod()

#Public examples - ends
