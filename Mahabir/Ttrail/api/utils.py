import pymongo
import urllib


client = pymongo.MongoClient("mongodb+srv://admin:" + urllib.parse.quote("DSds12@@")+ "@fielmente.dsj0myw.mongodb.net/myFirstDatabase?appName=mongosh+1.3.1")


def Create_Domain(name):
    domain = ''
    name_list = name.split(' ')
    for i in name_list:
        domain = domain+i

    return domain




def Mongocmd_Edit_menu(data):

    change =  client["mahabir_palace"].Ttrail_menu.find_one_and_update({"Domain":data["domain"]},{'$set':{
        data['key']:data['value']
    }})


def Mongocmd_Edit_services(data):

    change =  client["mahabir_palace"].Ttrail_services.find_one_and_update({"Domain":data["domain"]},{'$set':{
        data['key']:data['value']
    }})




