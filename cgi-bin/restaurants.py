#!/usr/bin/env python3
import cgi
#import os

class Restaurant:
  def __init__(self, name, suburb):
    self.name = name
    self.suburb = suburb

form = cgi.FieldStorage()

path = "/Users/mikabrues/Dev/foundations-restaurants/cgi-bin/restaurants.txt"

lucaIstDoofi = []

berg = open(path, "r").readlines()
for line in berg:
  row = line.split(',')
  name,suburb = [i.strip() for i in row]
  lucaIstDoofi.append(Restaurant(name,suburb))

name = form.getvalue("name")
suburb = form.getvalue("suburb")

lucaIstDoofi.append(Restaurant(name, suburb))

yeet = """
<div class = "stfu">
  <hr>
  <h1>{}</h1>
  <h1>{}</h1>
  <hr>
</div>
"""

lucaIstDoofiString = ""

i = 0
while i < len(lucaIstDoofi):
  lucaIstDoofiString = lucaIstDoofiString + yeet.format(lucaIstDoofi[i].name,lucaIstDoofi[i].suburb)
  i = i + 1

print(f"""
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Restaurants</title>
        <link rel="stylesheet" href="/style.css">
      </head>
      <body>
        <div class="main">
          <h1>Restaurants</h1>
          {lucaIstDoofiString}
          <a href="/index.html">Try Again</a>
        </div>
      </body>
    </html>
""")