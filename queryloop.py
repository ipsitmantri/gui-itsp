from implibs import *
import imgprocessing as impro
import hashing as hsh
import indexing as indx


#def cosine_similarity(x,y):
#   return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))
def gaussian_similarity(x,y):
    p=math.exp(-np.linalg.norm((x-y))**2/(2*0.3*0.3))
    return p


def runqry(que): #takes in a query quad list and outputs result for each constellation
    res=np.zeros((len(const_name),1),dtype=int)
    
    for i in range(len(const_name)):
        fileload='index'+const_name[i]+'.csv'

        ind=pd.read_csv(fileload)
        ind=ind.iloc[:,1:]

        for u in range(ind.shape[0]):  #renaming the rows which are failed cases which have been stored as pi
            if (abs(ind.iloc[u,0] - np.pi) <0.001):
                ind=ind.rename({u:np.pi})


        for b in ind.index:
            if b==np.pi:
                ind = ind.drop(b,axis = 0)
                break
            else:
                pass
        
        ind = ind.iloc[:,0:].values
        

        print('Loop running...')
        similarity_matrix = np.zeros((que.shape[0],ind.shape[0]),dtype = float)
        for z in range(que.shape[0]):
            for c in range(ind.shape[0]):
                similarity_matrix[z,c] = np.abs(gaussian_similarity(que[z],ind[c]))
        
        stdev=np.zeros((similarity_matrix.shape[0],1),dtype=float)
        for j in range(similarity_matrix.shape[0]):
            stdev[j]=np.std(similarity_matrix[j])
        thresh=0.15
        stdev=stdev[stdev>thresh]
        res[i]=stdev.shape[0]

    return res

