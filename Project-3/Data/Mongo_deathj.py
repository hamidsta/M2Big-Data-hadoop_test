
try :
    import pymongo as pym
    import pandas as pd
    import numpy
    import pprint
    from bson.code import Code
except Exception as e:
    raise Exception(' module missing : {}'.format(e))

# Making a connection to MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['local'] # acces database
print(db) # test if connect to mongodb database

death = db['death'] # acces to collection

db.death.find_one() # show random exemple

mapFunc = Code("function() {var skill =this.candidate.skill; for( i in skill) {/emit({name:this.dandidate.first.name+' '+this.candidate.last_name,skill,\skill:this.candidate.skills},1);}}")

redFunc = ("function(keyName,valSkillCount){\
return Array.sum(valSkillCount);}")

map_red =db.death.map_reduce(mapFunc,redFunc,'ppl_skillCount')

# aggregate framwork :
# pipeline
pipeline = [
    {"$match":{"Death State":"CT"}}
]

pprint.pprint(list(db.things.aggregate(pipeline)))



ct_result = my_collection.aggregate(
    [{
    "$match":
        {"id":"Death State",
         "T"

        }
    }]
)


for doc in col.aggregate([{'$unwind': '$death'},
    {'$match': {'Race': 'Heroin Toxicity'}},
    {'$group': {'_id': '$impressions.id', 'impressions_count': {'$sum': 1}}},
    ]):
    print(doc)


# setup mapreduce
x=MongoClient().client

one_record = my_collection.find_one()
print(one_record)

# change datatype

# use aggragation framework :
import pymongo

conn = pymongo.MongoClient("mongodb://localhost:2701")
db = conn.test
col =  db.collection

for doc in col.aggregate([{'$unwind': '$death'},
    {'$match': {'Race': 'Heroin Toxicity'}},
    {'$group': {'_id': '$impressions.id', 'impressions_count': {'$sum': 1}}},
    ]):
    print(doc)


