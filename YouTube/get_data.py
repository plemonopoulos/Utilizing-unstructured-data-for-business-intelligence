import pickle



#You should get a dictionary in the form dic[title] = [[comment,replies,likes],....]

fd = open('youtube_comments','rb+');
data = fd.read();
data = pickle.loads(data);

#You can do whatever you want with the data
