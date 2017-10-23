#!encoding:utf-8

import os
from flask import render_template,request,abort,Response
from . import movie_blueprint


@movie_blueprint.route('/')
def index():
    return render_template('movie/show_movie.html')

@movie_blueprint.route('/play')
def play():
    return "<h1>PLAY</h1>"

@movie_blueprint.route('/get_video',methods=['GET'])
def get_video():
    movie_id=request.form['movie_id']
    filename=""
    if not os.path.exists(filename):
        abort(404)
    start=0
    end=0
    file_size=os.path.getsize(filename)
    default_read_buffer=file_size/2
    Range=request.headers.get('Range')
    if Range:
        temp_range=Range.split('-')
        start=int(temp_range[0].split("=")[-1])
        if len(temp_range)==2 and temp_range[1]:
            end=temp_range[1]
        else:
            end=file_size
    if start>file_size or start>end:
        abort(500)
    f=file(filename)
    f.seek(start)
    #后期优化read buffer size
    buf_size=end-start if end-start>1 else default_read_buffer
    resp=Response(f.read(buf_size))
    f.close()
    resp.status_code=206
    resp.headers['Accept-Ranges']='bytes'
    resp.headers['Content-Range']='bytes %d-%d/%d' % (start,end-1,file_size)
    return resp

