class Class:
    @classmethod
    def class_meth(self, param):
        # method with "self"
        print('1 ' + param)

    @staticmethod
    def static_meth(param):
        # without "self"
        print('2 ' + param)

obj = Class()
# But what if vise versa?
# We need decorators
Class.class_meth('Hi') # OK
obj.static_meth('Yo') # OK