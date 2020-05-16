import json
import os
from suggestAi1 import *
from record import *
from flask import Flask
from flask import Flask, request
from flask import Response
from flask_cors import CORS


def returnSuggestAi(inp):
    return returnSuggest(inp)

#---FLASK---
app = Flask(__name__)
CORS(app)
@app.route('/input', methods=['GET','POST'])
def recordHandle():
    jsonData = request.get_json()
    rObj = fileService()
    if rObj.check_file(jsonData["id"]) == True:
       op = rObj.read_file(str(jsonData["id"]))
       if len(op) == 1:
          os.remove(str(jsonData["id"]) + ".json")
          return "updated"
       else:
          return "can't understand"
    else:
       ai3 = returnSuggestAi(jsonData["text"])
       if(len(ai3["suggestion"]) > 0):
          if rObj.write_file(str(jsonData["id"]),str(ai3["suggestion"][0]) + "," + str(jsonData["text"])) == True:
             return "patient id"
          else:
             return "something wrong"
       else:
          return "can't understand"

if __name__ == '__main__':
    port = int(os.getenv('PORT',80))
    app.run(host='0.0.0.0',port=port,threaded=True)
