#!/bin/bash

sudo apt-get update
pip install --upgrade pip
playwright install chromium
playwright install-deps chromium
sudo apt-get update

