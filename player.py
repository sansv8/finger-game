from hand import*
#rule 1 is exact rule 
#split rule is rule 2 

class player:
    

    def __init__(self,rule1,rule2):
        self.rightH=hand(rule1)
        self.leftH=hand(rule1)
        self.splitRule=rule2 

    def attack(self, hand_select, other):
        if other.fingers==5 or other.fingers==0:
            return False
        else:
            if hand_select==0:
                self.leftH.attack(other)
            else:
                self.rightH.attack(other)

                
    #hand_select is telling which hand is giving which hand fingers if left is giving right it is 0 else it is 1
    def split(self,hand_select,num=0):
        if self.splitRule:
            if (self.rightH.fingers+self.leftH.fingers)% 2 ==1:
                return False
            else:
                self.rightH.fingers==(self.rightH.fingers+self.leftH.fingers)/2
                self.leftH.fingers==(self.rightH.fingers+self.leftH.fingers)/2
        else:
            if hand_select==0:
                self.leftH.fingers-=num
                self.rightH.fingers+=num
            elif hand_select==1:
                self.leftH.fingers+=num
                self.rightH.fingers-=num
            else:
                raise IndexError

