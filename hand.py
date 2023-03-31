#rule 1 is exact fingers

class hand:

    def __init__(self,rule1):
        self.fingers=1
        self.rule1=rule1
        

    def attack(self,other):
        other.get_hit(self.fingers)


    def get_hit(self,num):
        self.fingers+=num
        if self.rule1:
            if self.fingers>=5:
                self.fingers-=5
        else:
            if self.fingers>=5:
                self.fingers=0
                    
    
                
        
