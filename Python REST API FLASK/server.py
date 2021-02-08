from flask import Flask,render_template
import connexion

#create an application instance for connexion


#create the application instance
	
app  = Flask(__name__,template_folder="templates")


#adding a COnnexion to the server

app = connexion.App(__name__,specification_dir='./')

app.add_api('swagger.yml')





#
#create a URL route in our application for "/"

@app.route('/')
def home():
    """
    The method just responds to the browsers URL,localhost:5000/
    :return: the rendered template 'home.html'
    
    """
    
    return render_template('home.html')
    
    #if we're running in the stand mode ,run the application
    
if __name__ == '__main__':
    app.run(debug=True)
