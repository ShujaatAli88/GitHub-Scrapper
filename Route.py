from flask import Flask, jsonify
from ES_Connection import my_Connection

app = Flask(__name__)

@app.route("/fetchData")
def data():
    ob = my_Connection()
    search_Query = {
        "query": {
            "match_all": {}
        }
    }

    searched_data = ob.search(index='github', body=search_Query)
    return jsonify({"Data": searched_data})

app.run()
