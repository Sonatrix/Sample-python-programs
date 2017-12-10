from pymongo import MongoClient
import matplotlib.pyplot as plt
client = MongoClient()
db = client['TechCrunch']
#result = db.Company.find({})
result = db.Company.aggregate([
        {
                '$match':{'state':'WA'}
        },
        {
                
                '$group':{'_id':'$company','count':{'$sum':1}}
        }
])
for comp in result:
    print(comp)
