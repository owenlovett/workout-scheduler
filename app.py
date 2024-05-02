from flask import Flask, render_template, request, jsonify
from openai import OpenAI

client = OpenAI(
    api_key = "sk-proj-bDkUku71eerfb0DJUsTAT3BlbkFJbJfU3olEwwdzWGCyzqhB",
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    days = request.json['days']
    prompt = f"Create a full workout schedule and list out every excercise with sets and reps for the following days: {', '.join(days)}. Focus on weightlifting and account for fatigue."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
    return jsonify({"schedule": completion.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)
