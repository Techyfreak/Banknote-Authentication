from flask import Flask,render_template,redirect,url_for,request
from models.banknoteauth import banknote
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.htm')

@app.route('/register',methods=['GET','POST'])
def register():
    if (request.method =='POST'):
        form_data=request.form.to_dict()
        return redirect(url_for('confirms',email=form_data['email'],name=form_data['name']))
    return render_template('register.htm')


@app.route('/confirm')
def confirms():

    return render_template('Confirm.htm',email=request.args['email'],name=request.args['name'])

@app.route('/verify',methods=['GET','POST'])
def verify():
    res = ""
    if (request.method =='POST'):
        form_data=request.form.to_dict()
        result=banknote(form_data["variance"],form_data["skewness"],form_data["curtosis"],form_data["entropy"])
        print(result)
        res= result
        #return redirect(url_for('verify'))
    return render_template('model.htm',result=res)

if __name__ =='__main__':
    app.run(debug=True)