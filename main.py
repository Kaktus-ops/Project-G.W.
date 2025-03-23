from flask import Flask, render_template,request, redirect


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def feedback():
    email = request.form.get['email']
    text = request.form.get['text']

    with open('form.txt', 'a') as f:
        f.write(f"Email: {email}\n")
        f.write(f"Commentary: {text}\n")
        f.write("-" * 20 + "\n")

    
    return render_template('index.html', 
                           email=email, text=text)

if __name__ == "__main__":
    app.run(debug=True)



    