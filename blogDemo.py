from flask import Flask,render_template,redirect,flash
from forms import LoginForm

app = Flask(__name__)
app.config.from_object("config")

@app.route('/')
@app.route('/index')
def index():
    user={"name":"huangxi"}
    posts=[
        {"author":{"name":"xiaoming"},"body":"this is a poem!"},
        {"author":{"name":"zhangshan"},"body":"today is a beautiful day!"}
           ]
    return render_template("index.html",title='Home',user=user,posts=posts)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash("Login requested for OpenID="+form.openid.data+",remember_me="+str(form.remember_me.data))
        return redirect("/index")
    return render_template("login.html",title="Sign In",form=form)









if __name__ == '__main__':
    app.run()
