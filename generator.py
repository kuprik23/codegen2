from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Generate a random code with the specified format
def generate_random_code():
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/"
    random_code = ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) \
                  + ''.join(random.choice(string.digits) for _ in range(5)) \
                  + ''.join(random.choice(special_characters) for _ in range(9))
    return random_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code')
def get_generated_code():
    code = generate_random_code()
    return jsonify(code=code)

if __name__ == '__main__':
    app.run(debug=True)
