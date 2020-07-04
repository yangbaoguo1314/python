import pickle,glob

suefile = open('sue.pkl','rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open('sue.pkl','wb')
pickle.dump(sue,suefile)
suefile.close()

for filename in glob.glob('*.pkl'):
    reco = open(filename,'rb')
    recd = pickle.load(reco)
    print(filename,'=>\n',recd)