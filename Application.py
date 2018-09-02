from flask import Flask, request, jsonify, make_response, send_file, send_from_directory
import os
import Dao

app = Flask(__name__, static_url_path='')
app.config['JSON_AS_ASCII'] = False


@app.route('/data/getFutureUnusualAction', methods=['GET'])
def getFutureUnusualAction():
    count = Dao.select("select count(*) co from t_future_unusual_action where f_read = 0", ())[0]['co']
    if count == 0:
        return ""
    items = Dao.select("select f_code, f_name, f_speed, f_rate, f_read, f_createtime from t_future_unusual_action where f_read = 0", ())
    for item in items:
        createtime = item['f_createtime']
        Dao.update("update t_future_unusual_action set f_read=%s where f_read=%s and f_createtime=%s", (1, 0, createtime))
    return jsonify(items)


@app.route('/image/<filename>', methods=['GET'])
def show_future(filename):
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open("future/" + filename, "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass


@app.route('/notify_html', methods=['GET'])
def view_notify():
    return send_file('notify.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

app.run(host="0.0.0.0", port=64212)