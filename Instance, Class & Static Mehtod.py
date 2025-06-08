# ক্লাস মেথড কে অবজেক্ট ক্রিটে করার আগে কল দেওয়া যায়
# ক্লাস মেথড বাই ডিফল্ট আর্গুমেন্ট হিসেবে cls নেয়
# to create a class method we use @classmethod decorator
# ক্লাস এর  রেফারেন্সে কল দিতে হয়

class employee:
    org_name = "Google"

    # instance method
    def __init__(self,name):
        self.name = name
        return self.name
    
    @classmethod

    def info(cls):
        print(cls.org_name)

    @staticmethod
    def static_method():
        print("Static method created")
    
employee.info()
employee.static_method()
