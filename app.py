from flask import Flask, request, abort, jsonify, render_template

app = Flask(__name__)

# 監聽所有來自 /try 的 Post Request
@app.route("/try", methods=['GET'])
def callback():
    # get X-Line-Signature header value
    # signature = request.headers['X-Line-Signature']
    # get request body as text
    # body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    # handle webhook body
    # try:
        # handler.handle(body, signature)
    # except InvalidSignatureError:
        # abort(400)
    result = ""
    for _ in range(8):
        result += str(_)
    return result


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
