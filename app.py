from flask import Flask, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def captura():
    # subprocess.run("apt install xauth -y", shell=True).stdout
    # subprocess.run("xvfb-run python main.py", shell=True).stdout
    subprocess.run("python main.py", shell=True).stdout
    return send_file("captura.png", mimetype='image/png')
    #return "OK"
