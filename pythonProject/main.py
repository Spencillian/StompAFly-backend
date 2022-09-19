from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
from models import Img
from db import db_init, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)
# run_with_ngrok(app)


data = [
    {
        'name': 'andrew_carnegie',
        'kills': 34,
        'rank': 1,
    },
    {
        'name': 'vpeet',
        'kills': 32,
        'rank': 2,
    },
    {
        'name': 'joe_biden',
        'kills': 31,
        'rank': 3,
    },
    {
        'name': 'shushushu',
        'kills': 30,
        'rank': 4,
    },
    {
        'name': 'mysta',
        'kills': 30,
        'rank': 5,
    },
    {
        'name': '88w88',
        'kills': 30,
        'rank': 6,
    },
    {
        'name': 'i_need_sleep',
        'kills': 28,
        'rank': 7,
    },
    {
        'name': 'msg',
        'kills': 23,
        'rank': 8,
    },
    {
        'name': 'luxluca',
        'kills': 22,
        'rank': 9,
    },
    {
        'name': 'NotHRE',
        'kills': 21,
        'rank': 10,
    },
    {
        'name': 'toad_lover',
        'kills': 21,
        'rank': 11,
    },
    {
        'name': 'botoverlord',
        'kills': 20,
        'rank': 12,
    },
    {
        'name': 'animepfp',
        'kills': 19,
        'rank': 13,
    },
]


@app.route('/leaderboard')
def leaderboard():
    return jsonify(data), 200


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']

    if not pic:
        return jsonify({'error': 'no pic'}), 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    img = Img(name=filename, mimetype=mimetype, img=pic.read())
    db.session.add(img)
    db.session.commit()

    return jsonify({'message': 'success'}), 200


@app.route('/<int:id>.jpg')
def get_img(id):
    img = Img.query.filter_by(id=id).first()

    if not img:
        return jsonify({'error': 'no img'}), 400

    return Response(img.img, mimetype=img.mimetype)


@app.route('/img')
def get_all_img():
    imgs = Img.query.all()

    if not imgs:
        return jsonify({'error': 'no imgs'}), 400

    ids = [img.id for img in imgs]

    return jsonify(ids), 200


@app.route('/delete/<int:id>')
def delete_img(id):
    img = Img.query.filter_by(id=id).first()

    if not img:
        return jsonify({'error': 'no img'}), 400

    db.session.delete(img)
    db.session.commit()

    return jsonify({'message': 'success'}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
