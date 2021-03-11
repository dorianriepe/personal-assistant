import os
import pickle
from datetime import datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


class Tasks:

    def __init__(self):
        
        if not os.path.isfile("./tasks-credentials.pkl"):
            
            if os.path.isfile("./tasks-client-secret.json"):
                flow = InstalledAppFlow.from_client_secrets_file("tasks-client-secret.json", scopes=['https://www.googleapis.com/auth/tasks'])
                credentials = flow.run_console()
                pickle.dump(credentials, open("tasks-credentials.pkl", "wb"))
            
            else:
                raise FileNotFoundError("Secrets file (./tasks-client-secret.json) not found")
        
        else:
            credentials = pickle.load(open("tasks-credentials.pkl", "rb"))
        
        service = build("tasks", "v1", credentials=credentials)

        self.service = service
    
    def get_list_id(self, list_name):
        
        results = self.service.tasklists().list().execute()
        items = results["items"]

        list_id = ""

        for item in items:
            if item["title"] == list_name:
                list_id = item["id"]

        if list_id == "":
            tasklist = {
                    "kind": "tasks#taskList",
                    "title": list_name
                }
            response = self.service.tasklists().insert(body=tasklist).execute()
            
            results = self.service.tasklists().list().execute()
            items = results["items"]
            
            for item in items:
                if item["title"] == list_name:
                    list_id = item["id"]

            if list_id == "":
                raise NameError("Calendar name is not valid")

        return list_id

    def get_tasks(self, list_id):
        
        response = self.service.tasks().list(tasklist=list_id).execute()

        return response

    def get_tasks_from_list(self, list_name):
        
        list_id = self.get_list_id(list_name)

        response = self.get_tasks(list_id)

        tasks = []

        if "items" in response:
            response = response["items"]
            for task in response:
                tasks.append(task["title"])

        return tasks

    def add_task_to_list(self, list_name, task_name):
        
        list_id = self.get_list_id(list_name)

        task = {'title': task_name}
        response = self.service.tasks().insert(tasklist=list_id, body=task).execute()

        return {"list": list_name, "task": task}

    def delete_list(self, list_name):
        
        list_id = self.get_list_id(list_name)

        response = self.service.tasklists().delete(tasklist=list_id).execute()

        return {"list": list_name}