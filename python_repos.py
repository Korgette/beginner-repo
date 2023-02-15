import requests
from plotly.graph_objs import Bar
from plotly import offline

#make an api call and store the information
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'apllication/vnd.github.v3+json'} #accept only v3
r = requests.get(url,headers=headers) #call to API,store as r
print(f"Status code: {r.status_code}") #status code shows if working

#store API response in a variable
response_dict = r.json()#use json() to convert to a python dict
print(f"Total repositories: {response_dict['total_count']}") #show total repos

#process results
print(response_dict.keys()) #print the resulting keys
repo_dicts = response_dict['items']
repo_links,stars,labels = [],[],[]
print(f"Repositories returned: {len(repo_dicts)}") #show 'items' repo count)
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

   #visual
data = [{'type':'bar',
         'x':repo_links,#plot repo_names to x
         'y':stars, #plot stars to y
         'hovertext':labels,
         'marker':{
             'color': 'rgb(0,225,150)', #fill colour of bar
             'line':{'width':1.5, 'color':'rgb(225,0,0)'} #bar outline colour
             },
         'opacity':0.6,
         }]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub', #defining title of chart
    'xaxis':{
        'title':'Repository', #defining title of axis
        'titlefont':{'size':24}, #defining title font size
        'tickfont':{'size':14} #defining tick font size
        },
    'yaxis':{'title':'Stars',
             'titlefont':{'size':24},
            'tickfont':{'size':14}},
    }

fig = {'data':data,'layout':my_layout}
offline.plot(fig, filename='python_repos.html')
#doesn't open in safari, but resulting file will open in chrome            

############################ USE BELOW FOR REPO KEYS
#print(f"\nKeys: {len(repo_dict)}") #print number of keys
#for key in sorted(repo_dict.keys()): #loop through keys, reporting them all
    #print(key)
