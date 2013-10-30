from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB':'cg_blog'}
app.config['SECRET_KEY']="cg123456"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

def register_blueprints(app):
    # Prevents circular imports
    from blog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)
