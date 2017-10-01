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
        return {'hello': 'world'}

api.add_resource(Article, '/api/articles')

if __name__ == '__main__':
    app.run(debug=True)
