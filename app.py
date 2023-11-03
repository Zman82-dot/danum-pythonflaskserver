from flask import Flask, render_template, request


app = Flask("My Flask Application")


@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    
@app.route("/image_search.html")
def renderimage_search():
    return render_template('image_search.html')

@app.route("/advanced_search.html")
def renderadvanced_search():
    return render_template('advanced_search.html')

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
