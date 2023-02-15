
class node:
#class for individual nodes

    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node(1)
#class for the entire list
    def new_node(self,data):
        #create a new node
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def introduce_loop(self):
        #introduce loop at end of list
        current = self.head
        while current.next != None:
            current = current.next
        current.next = self.head
        current = self.head
        current = current.next
        target = current
        current = current.next
        current.next = target

    def leng(self):
        #report the length of the list
        count = 0
        current = self.head
        while current.next != None:
            count += 1
            current = current.next
        return(count)
    
    def loop_test(self):
        #check if there is a loop in the list
        ls = set()
        current = self.head
        while current.next != None:
            if current in ls:
                return True
            ls.add(current)
            current = current.next
        return False

    def listy(self):
        #create a list of current nodes
        lsy = []
        current = self.head
        while current.next != None:
            lsy.append(current.data)
            current = current.next
        lsy.append(current.data)
        return(lsy)
            
    def remove_node(self,n):
        #remove nth node from end
        #print commands for understanding
        count = 1
        current = self.head
        while current.next != None:
            print('current node: ' +str(current.data))
            print('count: ' + str(count))
            print('my next node is: ' +str(current.next.data))
            count += 1
            current = current.next
        print(count)
        x = count - n
        print('x is: ' +str(x))
        current = self.head
        count = 1
        while current.next != None:
            if count == x:
                print('i am: ' + str(current.data) + ' and ' +str(current.next.data) \
                      + ' is the target!')
                current.next = current.next.next
                count += 1
                break
            else:
                current = current.next
                count += 1
        
            
    
        
#test with numbers for node 'index'
my_list = linked_list()
for n in range(2,10):
    my_list.new_node(n)
print(my_list.listy())
my_list.remove_node(2)
print(my_list.listy())
print(my_list.loop_test())
my_list.introduce_loop()
print(my_list.loop_test())
