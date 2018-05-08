import os
import json
import datetime


def loadUserProfile(id):
    directoryname = "users"
    # create file if it does not exist
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)

    filename = str(id) + ".json"
    filepath = os.path.join(directoryname, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            u_dict = json.load(f)
            userprofile = User(u_dict['id'], u_dict['name'], u_dict['categories'], u_dict['searches'])
    else:
        userprofile = User(id)

    return userprofile


class User:

    def __init__(self, ID, name="", categories={}, searches={}):
        self.name = name
        self.ID = ID
        self.categories = categories
        self.searches = searches

    def setname(self, name):
        self.name = name

    def mergeCategories(self, category):
        # category: A list contains all categories the user visited
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for c in category:
            if c in self.categories.keys():
                self.categories[c]['visits'] += 1
                self.categories[c]['datetime'] = now
            else:
                record = {'visits': 1, 'datetime': now}
                self.categories[c] = record

    def mergeSearches(self, search):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for s in search:
            if s in self.searches.keys():
                self.searches[s]['searchtime'] += 1
                self.searches[s]['datetime'] = now
            else:
                record = {'searchtime': 1, 'datetime': now}
                self.categories[s] = record

    def todict(self):
        profile = {
            'name': self.name,
            'id': self.ID,
            'categories': self.categories,
            'searches': self.searches
        }
        return profile

    def saveToFile(self):
        profile = self.todict()
        directoryname = "users"

        filename = str(self.ID) + ".json"
        filepath = os.path.join(directoryname, filename)
        with open(filepath, 'w+') as f:
            json.dump(profile, f)

    def sortByDatetime(self):
        # sort here
        return 0


user = loadUserProfile(2)
json_str = json.dumps(user.todict(), indent=1)
print(json_str)

category = {"Programming languages", "Pythons| "}
search = {"Python", "information retrieval"}
user.mergeSearches(search)
user.mergeCategories(category)

json_str = json.dumps(user.todict(), indent=1)
print(json_str)

user.saveToFile()

