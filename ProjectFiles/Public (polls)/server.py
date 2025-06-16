from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('easymeetingbooker.db')
c = conn.cursor()

