import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.tornado


def clear_data():
    db.devops_modules.remove()


if __name__ == '__main__':
    # clear_data()
    pass