from flask import Flask, render_template
import tp357_windows

app = Flask(__name__)  # Create the app instance yourself

@app.route("/tp357/get")
async def get_sensor_reading():
    return await tp357_windows.start()

@app.route("/")        # Register the route
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()