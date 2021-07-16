import requests
import json
import time

from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/')

def index():
  return "<h1>Welcome to Coding by Korn Version 2</h2>"


@app.route('/test-get-002', methods=['GET'])
def test_get():
  try:
    return {"message":"test get successful", "error":""}, 200
  except Exception as e:
    error_message = "[ error log ] - from message-receiver : " + str(e)
    return {"message": error_message, "error":e}, 400


@app.route('/create-list', methods=['POST'])
def create_song():
  try:
    if request.method == "POST":
      print("[ operation log ] - create a song")
      req = json.loads(request.data)

      # handle requests
      print("[ data log ] - request:", req)
      name   = req['name'] # wuwuwu
      list_name = req['list'] # jajaja
      list_data = req['data']

      # update to database
      f = open("list_of_data.txt", "a")
      f.write( name + "," + list_name + "," + list_data + "\n")
      f.close()

      return {"message": "successfully create a song", "error":""}, 200

  except Exception as e:
    return {"message": "", "error": e}

# if __name__ == '__main__':
#     app.run()