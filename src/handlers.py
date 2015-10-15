import tornado.web
import json

from bson.objectid import ObjectId

from db_helper import db
from models import *


class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        modules = self._find_modules()
        self.render('dashboard.html', modules=modules)

    def _find_modules(self):
        modules = []
        for module in db.leo_scrum.find():
            modules.append(module)
        return modules


class ModuleHandler(tornado.web.RequestHandler):
    def get(self):
        _id = self.get_argument('id', None)
        module = None
        if _id:
            module = db.leo_scrum.find_one({"_id": ObjectId(_id)})
        self.render('edit_module.html', module=module)

    def post(self):
        _id = self.get_argument('id', None)
        title = self.get_argument('title')
        memo = self.get_argument('memo')
        image = self.get_argument('image')
        module = Module(title, memo, image)
        if _id:
            db.leo_scrum.replace_one({"_id": ObjectId(_id)}, module.__dict__)
            print ("module updated..." + json.dumps(module.__dict__))
        else:
            db.leo_scrum.insert_one({"title": title, "memo": memo, "image": image})

            print ("module inserted..." + json.dumps(module.__dict__))
        self.redirect('/')

    def delete(self):

        _id = self.get_argument('_id')
        db.leo_scrum.remove({"_id": ObjectId(_id)})
        print ("module deleted:" + _id)


class TaskHandler(tornado.web.RequestHandler):
    def get(self):
        print(1)

    def post(self):
        task = Task('1', 'a', '3', 'start', 'a')
        db.leo_scrum.insert_one(task)
        # db.leo_scrum.
