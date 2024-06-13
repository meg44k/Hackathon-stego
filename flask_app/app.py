from flask_app import create_app

app =  create_app()

app.run(port=80,host='0.0.0.0', debug=True)