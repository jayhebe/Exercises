class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg
        
error = MyException("something wrong")