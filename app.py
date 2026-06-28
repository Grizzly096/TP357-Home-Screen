from flask import Flask, render_template
from database import db
import tp357_windows

app = Flask(__name__)  
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tp357.db"
db.init_app(app)
db.create_all()

@app.route("/tp357/get")
async def get_sensor_reading():
    return await tp357_windows.start()

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()