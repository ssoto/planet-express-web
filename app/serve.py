#!/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_restful import Resource, Api

from settings import STATIC_PATH

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='<<',
        variable_end_string='>>',
        comment_start_string='<#',
        comment_end_string='#>'
    ))
app = CustomFlask(__name__)

@app.route('/')
def index():
    index_path = 'index.html'
    return render_template(index_path)

api = Api(app)
class Article(Resource):
    def get(self):
        return [
            {
                'title': '1st article title',
                'description': '1st description',
                'url': 'http://elpais.com/abcde',
                'date': '2017-08-03'
            },
            {
                'title': '2nd article title',
                'description': '2nd description',
                'url': 'http://elpais.com/abcde',
                'date': '2017-08-01'
            },
            {
                'title': '3rd article title',
                'description': '3rd description',
                'url': 'http://elpais.com/abcde',
                'date': '2017-08-03'
            }
        ]

api.add_resource(Article, '/api/articles')

if __name__ == '__main__':
    app.run(debug=True)
