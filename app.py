from flask import Flask, render_template, request


app = Flask("My Flask Application")


@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    



if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
