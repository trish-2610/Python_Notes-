from flask import Flask , request , jsonify 
app = Flask(__name__)

## TO-DO list
## initial data in my to do list 
items = [
    {"id":1 , "name":"Item1" , "description":"This is item1"},
    {"id":2 , "name":"Item2", "description":"This is item2"}
]

@app.route("/")
def home():
    return "Welcome to my to do list home page"

## Get : Retrieve all items
@app.route("/items" , methods = ["GET"])
def get_items():
    return jsonify(items)

## Get : retieve a specific item by id 
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id ), None)
    if item is None :
        return jsonify({"error":"item not found"})
    return jsonify(item)
    
## Post : create a new task - API (using POSTMAN)
@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1 ,
        "description" : request.json["description"] ,
        "name" : request.json["name"]
    }
    items.append(new_item)
    return jsonify(new_item)

## Put : update an existing item 
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id ), None)
    if item is None :
        return jsonify({"error":"item not found"})
    item["name"] = request.json.get("name",item["name"])
    item["description"] = request.json.get("description",item["description"])
    return jsonify(item)

## DELETE : Delete an item 
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    global items 
    items = [ item for item in items if item["id"] != item_id ]
    return jsonify({"result":"item deleted"})

if __name__ == "__main__":
    app.run(debug = True )