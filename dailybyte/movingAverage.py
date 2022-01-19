# public class MovingAverage {
#     //TODO: declare any instance variables you require.
# /**
#  * Initializes a MovingAverage with a
#  * capacity of `size`.
#  */
# public MovingAverage(int size) {
#   //TODO: initialize your MovingAverage.
# }

# /**
#  * Adds `val` to the stream of numbers
#  * and returns the current average of the numbers.
#  */
# public double next(int val) {
#    //TODO: implement this method.
# }

# }

class MovingAverage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.total = []
        self.count = 0
    
    def next(self,val):
        self.total.append(val)
        self.count += 1
        if self.count > self.capacity:
            self.total.pop(0)
            self.count -= 1
        return int(sum(self.total)/self.count)


m = MovingAverage(3);
print(m.next(3))
print(m.next(5))
print(m.next(7)) 
print(m.next(6))
