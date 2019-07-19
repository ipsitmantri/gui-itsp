from implibs import *
import imgprocessing as impro
import hashing as hsh
import queryloop as qr

def main(imageio):
    #img2 = cv2.imread(imageio)

    centers2 = impro.processed_image(imageio)


    all_quads2 = hsh.make_quads(centers2)
    query = []
    for quad in all_quads2:
        query.append(hsh.make_hashcodes(quad))


    que = np.zeros((len(query),4),dtype = float)
    for i in range(len(query)):
        if not(query[i] == 'failed'):
            que[i] = query[i]
        else:
            que[i] = np.pi

    que = pd.DataFrame(que,index = que[0:,0])
    for b in que.index:
        if b==np.pi:
            que = que.drop(b,axis = 0)
            break
        else:
            pass
    que = que.iloc[:,0:].values

    result=np.zeros((len(const_name),1),dtype=int)
    result=qr.runqry(que)
    return result
    #for i in range(result.shape[0]):
        #print(const_name[i],result[i],sep=':')
