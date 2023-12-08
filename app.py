from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Remove spaces in the password section of the URI
uri = "mongodb+srv://FMuser:KoolWordz@cluster0.ykezvyd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["my_database"]

try:
    client.server_info()
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(e)

# Send a ping to confirm a successful connection
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mongo_data')
def get_mongo_data():
    # Example: Fetch data from MongoDB
    data_from_mongo = db.my_collection.find_one()
    return jsonify(data_from_mongo)

if __name__ == '__main__':
    app.run(debug=True)





from flask import Flask, jsonify
# from pymongo import MongoClient


# app = Flask(__name__)

# uri = "mongodb+srv://FMuser: KoolWordz @cluster0.ykezvyd.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri)
# db = client["my_database"]
# try:

#     client.server_info()
#     print("Connected to MongoDB successfully!")

# except Exception as e:
#     print(e)
# # Send a ping to confirm a successful connection
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/mongo_data')
# def get_mongo_data():
#     # Example: Fetch data from MongoDB
#     data_from_mongo = db.my_collection.find_one()
#     return jsonify(data_from_mongo)

# if __name__ == '__main__':
#     app.run(debug=True)

# KoolWordz