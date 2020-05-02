
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
	for i ,(input ,label) in enumerate(train_loader):
		
		output =model(input)

		





