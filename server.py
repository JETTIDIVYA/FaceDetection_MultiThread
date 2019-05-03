from flask import Flask, request, jsonify
import time
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post() :
    # f = open("file.txt", "a+")
    # f.write (" Face detected \n")
    time.sleep(5)
    return jsonify(data="face detected",status_code=200)
    # time.sleep(5)


if __name__=="__main__":
    app.run("127.0.0.1", 5000)
    

    
