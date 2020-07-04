from initdata import bob,sue,tom

import pickle

for (key,record) in [('bob',bob),('tom',tom),('sue',sue)]:
    recfile = open(key + '.pkl','wb')#wb模式打开并写入key+pkl的文件
    pickle.dump(record,recfile)
    recfile.close()