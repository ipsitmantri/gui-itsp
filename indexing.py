from implibs import *
import hashing as hsh
import imgprocessing as impro
img1 = cv2.imread(r'D:\Documents\ursamajortemp.png')
#using the template image to create index in the same way as for a query image.
centers1 = impro.processed_image(img1)
all_quads1 = hsh.make_quads(centers1)
index = []
for quad1 in all_quads1:
    index.append(hsh.make_hashcodes(quad1))
ind = np.zeros((len(index),4),dtype = float)
for i in range(len(index)):
    if not(index[i] == 'failed'):
        ind[i] = index[i]
    else:
        ind[i] = np.pi

#storing the hash codes in csv file.
pd.DataFrame(ind).to_csv("indexursamajor.csv")
