import json

with open('source_file_2.json') as json_f:
    data = json.load(json_f)

managers_name = []
watchers_name = []
priority_projects = []
projects_name = []

for something in data:
    managers_name += something["managers"]
    watchers_name += something["watchers"]

managers_names = set(managers_name)
watchers_names = set(watchers_name)


manager_projects = []
for manager in managers_names:
    manager_projects.append([])

managers = dict(zip(managers_names, manager_projects))

watchers_projects = []
for watcher in watchers_names:
    watchers_projects.append([])

watchers = dict(zip(watchers_names, watchers_projects))

for something in data:
    for manager in managers_names:
        if manager in something["managers"]:
            managers[manager].append([something["name"], something["priority"]])

    for watcher in watchers_names:
        if watcher in something["watchers"]:
            watchers[watcher].append([something["name"], something["priority"]])


(keys, values) = zip(*managers.items())

proj_names = []
for value in values:
    value.sort(key=lambda x: x[1], reverse=True)
    proj_names.append(list(map(lambda x: x[0], value)))

with open("managers.json", "w") as f:
    dictionary = dict(zip(keys, proj_names))
    json.dump(dictionary, f)

(keys, values) = zip(*watchers.items())

proj_names = []
for value in values:
    value.sort(key=lambda x: x[1], reverse=True)
    proj_names.append(list(map(lambda x: x[0], value)))

with open("watchers.json", "w") as f:
    dictionary = dict(zip(keys, proj_names))
    json.dump(dictionary, f)
