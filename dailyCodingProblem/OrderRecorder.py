



class OrderRecorder:
    def __init__(self, N):
        self.logs = []
        self.N = N
    
    def record(self, order_id):
        self.logs.append(order_id)
        if len(self.logs)>self.N:
            self.logs.pop(0)
    
    def get_last(self,i):
        index = len(self.logs) - i 
        return self.logs[index]

recorder = OrderRecorder(10)
recorder.record(1)
recorder.record(2)
recorder.record(3)
recorder.record(4)
recorder.record(5)
recorder.record(6)
recorder.record(7)
print(recorder.get_last(3))
