#!/bin/bash

apt-get update
playwright install
pip install --upgrade pip
playwright install chromium
playwright install-deps chromium
apt-get update

