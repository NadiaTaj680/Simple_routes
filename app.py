from flask import Flask,render_template
app=Flask(__name__)
  
   # Creating routes and rendering templates :

   # Defining URls for displaying the selescted route :
    
@app.route('/')
def home():
    name="Taj Muhammad"
    return render_template("home.html", name=name)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__== "__main__":
    app.run(debug=True)