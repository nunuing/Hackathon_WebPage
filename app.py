from flask import Flask, request, render_template, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

app = Flask(__name__)

# ChatOpenAI 모델 초기화
llm = ChatOpenAI(model="gpt-4")  # "gpt-3.5-turbo" 또는 "gpt-4" 모델 사용

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # LangChain이 요구하는 HumanMessage 객체로 메시지를 구성
    messages = [HumanMessage(content=user_message)]
    
    try:
        # llm 객체를 호출하여 messages 전달
        response = llm(messages)
        return jsonify({"response": response.content})  # 응답에서 content만 반환
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, render_template, jsonify
# from langchain.llms import OpenAI

# app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return render_template('Main.html', data='main')

# @app.route('/')
# def home():
#     return render_template('Temp.html', data='temp')

# @app.route('/chat')
# def chat():
#     return render_template('Chat.html', data='chat')

# @app.route('/pay')
# def pay():
#     return render_template('Payment.html', data='pay')

# @app.route('/confirm')
# def confirm() : 
#     return render_template('Confirm.html', data='confirm')

# @app.route('/finger')
# def finger() : 
#     return render_template('Finger.html', data='finger')

# @app.route('/print')
# def print() : 
#     return render_template('Print.html', data='print')

# @app.route('/done')
# def done() : 
#     return render_template('PrintDone.html', data='done')


# if __name__ == '__main__':  
#     # app.run(debug=True) # 포트 5000 이미 사용중이면 포트에 5001 넣어주자.
#     app.run('0.0.0.0', port=5001, debug=True)

# # # LangChain의 OpenAI 모델 초기화
# # llm = OpenAI(model_name="gpt-4")  # gpt-4로 변경 가능

# # @app.route('/gptTest', methods=['POST'])
# # def chat():
# #     # 클라이언트 요청으로부터 사용자 메시지 가져오기
# #     data = request.get_json()
# #     user_message = data.get("message")
    
# #     if not user_message:
# #         return jsonify({"error": "No message provided"}), 400
    
# #     # LangChain을 통해 OpenAI 모델에 질문을 전달
# #     try:
# #         response = llm(user_message)
# #         return jsonify({"response": response})
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500