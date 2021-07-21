import os
from flask import Flask, jsonify
from flask import request, render_template, url_for

app = Flask(__name__)

@app.context_processor  # 上下文渲染器，给所有html添加渲染参数
def inject_url():
    data = {
        "url_for": dated_url_for,
    }
    return data

def dated_url_for(endpoint, **values):
    filename = None
    if endpoint == 'static':
        filename = values.get('filename', None)
    if filename:
        file_path = os.path.join(app.root_path, endpoint, filename)
        values['v'] = int(os.stat(file_path).st_mtime)  # 取文件最後修改時間的時間戳，文件沒更新，則可用緩存
        return url_for(endpoint, **values)

#------------------------------------------------------------------------------------------------------------------- assessment
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    return render_template('chatbot.html', content_type='application/json')

@app.route('/get_msg', methods=['GET', 'POST'])
def get_msg():
    render_template('chatbot.html', content_type='application/json')
    msg = request.get_json(force=True)
    send_msg = msg.get('send_msg','')
    data = {'res_msg': 'res: '+send_msg}
    return jsonify(data)


if __name__=="__main__":
    app.debug = True
    # app.run(host="0.0.0.0", port=8090)
    app.run(port=8090)
