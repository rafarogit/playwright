from flask import Flask, send_file
from playwright.sync_api import sync_playwright
import subprocess

app = Flask(__name__)

@app.route('/')
def captura():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://google.com")
        ti = page.title()
        # page.screenshot(path="captura.png")
        browser.close()
        return ti
    # subprocess.run("apt install xauth -y", shell=True).stdout
    # subprocess.run("xvfb-run python main.py", shell=True).stdout
    # subprocess.run("python main.py", shell=True).stdout
    # return send_file("captura.png", mimetype='image/png')
    #return "OK"
