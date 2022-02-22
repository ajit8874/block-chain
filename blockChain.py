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
        self.tail=None
      
    

    def append(self,data):

        # if data is None:
        #     return None
        
        if self.head is None:
            self.head=Block(get_time_stamp(),data,0)
        else:
            while self.head.next is not None:
                self.head=self.head.next
            self.head.next=Block(get_time_stamp(),data,self.head.hash)
         
        
        # if self.head.next is not None:
        #     self.head=self.head.next
        # else:

        #     self.head.next=Block(get_time_stamp,value,0)
        
        
    

    def to_str(self):
        output=[]
        if self.head is not None:
            output.append(self.head)
            self.head=self.head.next
        return output




            

blockchain=BlockChain()
blockchain.append("abc")
blockchain.append("def")
blockchain.append("ghi")

for i in blockchain.to_str():
    print(i,"\n")

