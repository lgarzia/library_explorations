import sys

p = r"C:\Users\lgarzia\Documents\GitHub\library_explorations\TaskWeaver\TaskWeaver" 

sys.path.insert(0, p)

from taskweaver.app.app import TaskWeaverApp

app_dir = "./TaskWeaver/pilot_project/project/"
app = TaskWeaverApp(app_dir=app_dir)
session = app.get_session()

user_query = "print out current working directory"
response_round = session.send_message(user_query)

response_dict = response_round.to_dict()

for p in response_dict.get('post_list'):
    print("\n", p)    print("\n", p)