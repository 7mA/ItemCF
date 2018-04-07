import math  
import json
  
class ItemBasedCF:  
    def __init__(self,train_file):  
        self.train_file = train_file  
        self.readData()  
    def readData(self):  
         
        self.train = dict()       
        for line in open(self.train_file):  
            # user,item,score = line.strip().split(",")  
            user,score,item = line.strip().split(",")  
            self.train.setdefault(user,{})  
            self.train[user][item] = int(float(score))  
  
    def ItemSimilarity(self):  
          
        C = dict()    
        N = dict()    
        for user,items in self.train.items():  
            for i in items.keys():  
                N.setdefault(i,0)  
                N[i] += 1  
                C.setdefault(i,{})  
                for j in items.keys():  
                    if i == j : continue  
                    C[i].setdefault(j,0)  
                    C[i][j] += 1  
          
        self.W = dict()  
        for i,related_items in C.items():  
            self.W.setdefault(i,{})  
            for j,cij in related_items.items():  
                self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))  
        return self.W  
  
      
    def Recommend(self,user,K=3,N=10):  
        rank = dict()  
        action_item = self.train[user]     
        for item,score in action_item.items():  
            for j,wj in sorted(self.W[item].items(),key=lambda x:x[1],reverse=True)[0:K]:  
                if j in action_item.keys():  
                    continue  
                rank.setdefault(j,0)  
                rank[j] += score * wj  
        return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])  
      
    
	
Item = ItemBasedCF("history.csv")  
w2 = Item.ItemSimilarity()
with open('train.json', 'w') as f:
	json.dump(Item.train, f)
with open('metrix.json', 'w') as f:
	json.dump(w2, f)  
print("Build Complete.")
#recommedDic = Item.Recommend(recommenduser, neighbornum, recommendnum)  
#for k,v in recommedDic.iteritems():  
#    print k,"\t",v  
