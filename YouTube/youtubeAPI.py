import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret_881602924758-9thatkhmm336bkrbdiii81u12ru07cua.apps.googleusercontent.com.json" 

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
#key = AIzaSyCAFJ3MZj-eOvOOlYUt15FyMAQCeB-ECAo
def get_authenticated_service():
	credentials = None
	if(os.path.exists('token.pickle')):
		token  = open('token.pickle', 'rb');
		credentials = pickle.load(token)
	
	if(not credentials or not credentials.valid):
		if(credentials and credentials.expired and credentials.refresh_token):
			try:	
				credentials.refresh(Request())
			except:
				print('delete token.pickle')
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
			credentials = flow.run_console()
 		# Save the credentials for the next run
		token = open('token.pickle', 'wb');
		pickle.dump(credentials, token)

	return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
service = get_authenticated_service()


# =============================================================================
# Search Query Initialisation
# =============================================================================


query = input('Enter search : ');
results = input('Enter number of videos you want to extract : ')
filename = input('Enter filename you want to write comments : ')

query_results = service.search().list(
        part = 'snippet',
        q = query,
        order = 'relevance', # You can consider using viewCount
        maxResults = results,
        type = 'video', # Channels might appear in search results
        relevanceLanguage = 'en',
        safeSearch = 'moderate',
        ).execute()



# =============================================================================
# Get Video IDs
# =============================================================================
video_id_dic = {};
comment_dic = {};
description_dic = {};
title_dic = {}
video_title = []
video_id = []
video_desc = []
for item in query_results['items']:
    video_id_dic[item['id']['videoId']] = item['snippet']['title']
    video_id.append(item['id']['videoId']);
    description_dic[item['snippet']['title']] = item['snippet']['description'];
    video_title.append(item['snippet']['title'])
    

for title in video_title:
	title_dic[title] = [];

# =============================================================================
# Get Comments of Top Videos
# =============================================================================
video_id_pop = []
channel_pop = []
video_title_pop = []
video_desc_pop = []
comments_pop = []
comment_id_pop = []
reply_count_pop = []
like_count_pop = []

print(video_id)
from tqdm import tqdm
for i, video in enumerate(tqdm(video_id, ncols = 100)):
    
    title = video_id_dic[video];
    try:
    	response = service.commentThreads().list(part = 'snippet',videoId = video,maxResults = 100, order = 'relevance', textFormat = 'plainText').execute()
    
    	comments_temp = []
    	comment_id_temp = []
    	reply_count_temp = []
    	like_count_temp = []
    	for item in response['items']:
    	    title_dic[title].append([item['snippet']['topLevelComment']['snippet']['textDisplay'],item['snippet']['totalReplyCount'],item['snippet']['topLevelComment']['snippet']['likeCount']]);
    	    reply_count_temp.append(item['snippet']['totalReplyCount'])
    	    like_count_temp.append(item['snippet']['topLevelComment']['snippet']['likeCount'])
    	comments_pop.extend(comments_temp)
    	comment_id_pop.extend(comment_id_temp)
    	reply_count_pop.extend(reply_count_temp)
    	like_count_pop.extend(like_count_temp)
    
    	video_id_pop.extend([video_id[i]]*len(comments_temp))
    
    	video_title_pop.extend([video_title[i]]*len(comments_temp))
    except:
    	print("Unable to find comments " + str(i))

print(title_dic)
print("===================")
print("===================")
print("===================")
print("===================")
print("===================")
print("===================")
print(description_dic)

fd = open(filename,'wb+');
fd.write(pickle.dumps(title_dic));
fd.close();


fd = open('Video descriptions','wb+');
fd.write(pickle.dumps(description_dic));
fd.close();