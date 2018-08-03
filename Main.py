from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'      #render_template('index.html')
    
app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))
	
if __name__ == "__main__":
	app.run(debug=True)