# 4번캡처
import os
import numpy as np
from scipy.spatial import distance 

# 원본 IMDB 데이터 읽기
fname='./glove.6B/glove.6B/glove.6B.100d.txt'
f=open(fname,encoding='utf8')

for line in f:
          print(type(line))
          print(line)
          break
    
# 사전 구축
dictionary={}
for line in f:
    li=line.split()
    word=li[0]
    vector=np.asarray([float(val) for val in li[1:]], dtype='float32')
    dictionary[word]=vector
    
# 가장 가까운 단어를 찾아주는 함수
def find_closest_words(vector):
    return sorted(dictionary.keys(),key=lambda w: distance.euclidean(dictionary[w],vector))

# 가까운 단어 찾기
print(find_closest_words(dictionary['movie'])[:5])
print(find_closest_words(dictionary['school'])[:5])
print(find_closest_words(dictionary['oak'])[:5])
                  
# 단어 추론
print(find_closest_words(dictionary["seoul"]-dictionary["korean"]+dictionary["spain"])[:5])
print(find_closest_words(dictionary["animal"]-dictionary["lion"]+dictionary["oak"])[:5])
print(find_closest_words(dictionary["queen"]-dictionary["king"]+dictionary["actress"])[:5])

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# tsne를 이용하여 2차원 공간으로 축소하고 시각화
tsne=TSNE(n_components=2,random_state=0)
words=list(dictionary.keys())
vectors=np.array([dictionary[word]for word in words])
p2=tsne.fit_transform(vectors[:50])
plt.scatter(p2[:,0],p2[:,1])

for label,x,y in zip(words,p2[:,0],p2[:,1]):
    plt.annotate(label,xy=(x,y))
    
plt.show()