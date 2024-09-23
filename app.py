from flask import Flask, request,render_template,jsonify

import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "First time Flask"

# Dynamic URL
@app.route("/user")
@app.route("/user/<name>")
def user(name="Guest"):
    return f"Hello {name}"

@app.route("/posts/<int:post_id>/comments/<int:comment_id>")

def posts(post_id,comment_id):
    return f"Post id: {post_id} comment id: {comment_id}"


# Rendering HTML template


@app.route("/welcome")
def welcome():
    data = "Wow flask is very easy"
    languages = ['python','java','C','C++']
    context = {
        "data":data,
        "languages":languages,
    }
    
    return render_template("index.html",context=context)

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return f"User name is {username}"
    return render_template("login.html")

@app.route("/countries")
def countries():
    data = [
        {
            "name": "John Doe",
            "age": 30,
            "city": "New York",
            "email": "johndoe@example.com",
            "hobbies": ["reading", "travelling", "coding"]
        },
        {
            "name": "Jane Smith",
            "age": 25,
            "city": "Los Angeles",
            "email": "janesmith@example.com",
            "hobbies": ["painting", "yoga", "gaming"]
        },
        {
            "name": "Mike Brown",
            "age": 35,
            "city": "Chicago",
            "email": "mikebrown@example.com",
            "hobbies": ["photography", "hiking", "basketball"]
        }
    ]
    return jsonify(data)


@app.route("/posts")
def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    return jsonify(data)

@app.route("/posts/<int:post_id>")
def single_post(post_id):
    # Correctly format the URL with the post_id
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = response.json()
    return jsonify(data)
    
    
    


if __name__ == "__main__":
    app.run(debug=True)
