from sklearn import datasets
import matplotlib.pyplot as plt

digit=datasets.load_digits()

plt.figure(figsize=(5,5))
plt.imshow(digit.images[0],cmap=plt.cm.gray_r,interpolation='nearest')

plt.show()
print(digit.data[0])
print("이 숫자는 ",digit.target[0],"입니다.")

lfw=datasets.fetch_lfw_people(min_faces_per_person=70,resize=0.4)

plt.figure(figsize=(20,5))

for i in range(8):
    plt.subplot(1,8,i+1)
    plt.imshow(lfw.images[i],cmap=plt.cm.bone)
    plt.title(lfw.target_names[lfw.target[i]])
    
plt.show()