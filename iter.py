
def data_iter(dataset,batch_size):
	skeleton_all=[]
	batches_sk=[]

	num_class= len(dataset)
	for i in range(num_class):
		for j in range(len(dataset[i])):
			skeleton_all.append(dataset[i][j])
	random.shuffle(skeleton_all)

	num_iter = skeleton_all//batch_size

	for i in range(num_iter):
		start_index=i
		end_index=(i+1)*32
		batch_sk =[(tuple(skeleton_all[start_index:end_index][0]),tuple(skeleton_all[start_index:end_index][]))]
		batches_sk.append(batch_sk)
	return batches_sk

train_loader =data_iter(dataset.train,batch_size)
#####initialize the model######
print("initialize the model #########")

model =torch.nn.LSTM(batch_size,embed_size,hidden_size,n_layers=2,dropout=0.5)
classifer = torch.nn.Linear(hidden_size,num_class)
loss =torch.softmax(output,label)


def train(model,dataset,optimizer,batch_size):
	model.train()
	total_loss =0



import math
import torch
import random
from torch import nn
from torch.autograd import Variable
import torch.nn.functional as F

class LSTMGait(nn.module):
	def __init__(self, batch_size，embed_size,hidden_size，num_class, n_layers=1 ,dropout=0.5):
		super(LSTMGait,self).__init__()
		self.batch_size = batch_size
		self.embed_size = embed_size
		self.hidden_size =hidden_size
		self.num_class = num_class
		self.lstm = nn.LSTM(input_size=self.embed_size, hidden_size=self.hidden_dim, num_layers=1, batch_first=True)
		self.classfier = nn.linear(self.hidden_size, self.num_class)

	def forward(self,input):
		output,(h_n,c_n)=self.lstm(input)
		
		if not self.traning:
			return output
		else:
			y=self.classfier(output)
			return y, output


