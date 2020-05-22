class Queue(object):
    def __init(self,):
        self._worker=None
        
    def worker(self,func):
        self._worker = func
        print(self._worker)
        return self.worker
    
    def __iter__(self):
        for i in range(10):
            yield i
    
    def consume(self,):
        for message in self:
            self._worker(message)
            

queue = Queue()

@queue.worker
def process(message):
    print(message,"==========")
    
queue.consume()
