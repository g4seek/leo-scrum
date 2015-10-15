import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.tornado


def clear_data():
    db.sys_module.remove()


if __name__ == '__main__':
    clear_data()
    pass