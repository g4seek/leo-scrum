import tornado.web

from bson.objectid import ObjectId

from db_helper import db


class DashboardHandler(tornado.web.RequestHandler):
    def get(self):
        modules = self._find_modules()
        self.render('dashboard.html', modules=modules)


    def _find_modules(self):
        modules = []
        for module in db.devops_modules.find():
            modules.append(module)
        return modules


class ModuleHandler(tornado.web.RequestHandler):
    def get(self):
        _id = self.get_argument('id', None)
        module = None
        if _id:
            module = db.devops_modules.find_one({"_id": ObjectId(_id)})
        self.render('edit_module.html', module=module)

    def post(self):
        _id = self.get_argument('id', None)
        title = self.get_argument('title')
        memo = self.get_argument('memo')
        image = self.get_argument('image')
        if _id:
            db.devops_modules.replace_one({"_id": ObjectId(_id)}, {"title": title, "memo": memo, "image": image})
            print ("module updated...{_id:" + _id + ",title:" + title + ",memo:" + memo + ",image:" + image + "}")
        else:
            db.devops_modules.insert_one({"title": title, "memo": memo, "image": image})
            print ("module inserted...{title:" + title + ",memo:" + memo + ",image:" + image + "}")
        self.redirect('/')

    def delete(self):

        _id = self.get_argument('_id')
        db.devops_modules.remove({"_id": ObjectId(_id)})
        print ("module deleted:" + _id)


class TaskHandler(tornado.web.RequestHandler):
    def get(self):
        print(1)
