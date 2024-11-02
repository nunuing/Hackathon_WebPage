from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Main.html', data='main')

@app.route('/chat')
def chat():
    return render_template('Chat.html', data='chat')

if __name__ == '__main__':  
    # app.run(debug=True) # 포트 5000 이미 사용중이면 포트에 5001 넣어주자.
    app.run('0.0.0.0', port=5001, debug=True)