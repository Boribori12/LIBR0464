#프로젝트의 환경을 설정하는 config

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'webp.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "webp"
