import tornado.web

from bson.objectid import ObjectId

from db_helper import db
from models import *


class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        modules = self._find_modules()
        self.render('dashboard.html', modules=modules)

    def _find_modules(self):
        modules = []
        for module in db.sys_module.find():
            modules.append(module)
        return modules


class ModuleHandler(tornado.web.RequestHandler):
    def get(self):
        _id = self.get_argument('id', None)
        module = None
        if _id:
            module = db.sys_module.find_one({"_id": ObjectId(_id)})
        self.render('edit_module.html', module=module)

    def post(self):
        _id = self.get_argument('id', None)
        title = self.get_argument('title')
        memo = self.get_argument('memo')
        image = self.get_argument('image')
        module = Module(title=title, memo=memo, image=image)
        if _id:
            db.sys_module.replace_one({"_id": ObjectId(_id)}, module.__dict__)
            print ("module updated..." + str(module.__dict__))
        else:
            db.sys_module.insert_one(module.__dict__)
            print ("module inserted..." + str(module.__dict__))
        self.redirect('/')

    def delete(self):

        _id = self.get_argument('_id')
        db.sys_module.remove({"_id": ObjectId(_id)})
        print ("module deleted:" + _id)


class TaskHandler(tornado.web.RequestHandler):
    def get(self):
        task = Task(name='b', priority=5, status='doing', link='b')
        db.leo_task.insert_one(task.__dict__)
        for task in db.leo_task.find():
            print task

    def post(self):
        task = Task(name='a', priority='3', status='start', link='a')
        db.leo_task.insert_one(task.__dict__)
        # db.sys_module.
