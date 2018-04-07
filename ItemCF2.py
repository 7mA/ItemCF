import json
import sys

def Recommend(user,K=3,N=10):  
		#print user
		with open('train.json', 'r') as f:
			train = json.load(f)
		#for i in train:
		#	i.encode("ASCII")
			#train[i].encode("ASCII")
		#print(str(train))
		with open('metrix.json', 'r') as f:
			W = json.load(f)
		#print W
		rank = dict()  
		action_item = train[user]     
		for item,score in action_item.items():  
			for j,wj in sorted(W[item].items(),key=lambda x:x[1],reverse=True)[0:K]:  
				if j in action_item.keys():  
					continue  
				rank.setdefault(j,0)  
				rank[j] += score * wj  
		return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N]) 
		
recommenduser = sys.argv[1]
neighbornum = int(sys.argv[2])
recommendnum = int(sys.argv[3])	
recommedDic = Recommend(recommenduser, neighbornum, recommendnum) 
print("recommedDic")
for k,v in recommedDic.items():  
	print(str(k) + "\t" + str(v))  
