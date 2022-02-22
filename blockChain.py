import datetime
import hashlib
from webbrowser import get

def calc_hash():
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
class Block:
    def __init__(self, timestamp, data, previous_hash):

        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash()
        self.next=None

def get_time_stamp():
    return datetime.datetime.now()

class BlockChain:
    def __init__(self):
        self.head=None
        # self.tail=None

    def append(self,data):

        # if data is None:
        #     return None
        
        if self.head is None:
            self.head=Block(get_time_stamp(),data,0)
        else:
            while self.head.next is not None:
                self.head=self.head.next
            
            self.head.next=Block(get_time_stamp(),data,self.head.hash)
        
        

    def to_print(self):
        output=[]
        node=self.head
        index_no=0
        if self.head is not None:
            output.append(self.head)
            self.head=self.head.next
        
        print("Index No: ",index_no)
        print("TimeStamp: ",str(node.timestamp))
        print("Date: ", node.data)
        print("SHA256 hASH: ",node.hash)
        print("previous hash: ",node.previous_hash)

        node =node.next
        count +=1

        print("\n")
        # return output




            

blockchain1=BlockChain()
print("block chain",blockchain1)

blockchain1.to_print()

blockchain1.append("abc")
blockchain1.append("def")
blockchain1.append("ghi")

blockchain1.to_print()

# for i in blockchain.to_str():
#     print(i,"\n")

