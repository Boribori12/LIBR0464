from flask import Blueprint, render_template, request, url_for, flash, g, session
from werkzeug.utils import redirect
from datetime import datetime
from .. import db

from app.views.auth_views import login_required
from ..models import Item
from ..forms import ItemForm
from PIL import Image
import base64

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/detail_item/<int:item_id>/')
def detail_item(item_id):
    item = Item.query.get_or_404(item_id)
    encoded_img_data = base64.b64encode(item.img)
    item.img = encoded_img_data.decode('utf-8')
    return render_template('item-detail.htm', item = item)

@bp.route('/list_item/')
def _list_item():
    page = request.args.get('page', type = int, default = 1)
    loc = request.args.get('loc', type=str, default='*')
    if loc == '*':
        item_list = Item.query.order_by(Item.create_date.desc())
    else:
        item_list = Item.query.filter_by(location=loc).order_by(Item.create_date.desc())
    item_list = item_list.paginate(page = page, per_page = 6)

    for item in item_list:
        encoded_img_data = base64.b64encode(item.img)
        item.img = encoded_img_data.decode('utf-8')

    return render_template('item-list.htm', item_list = item_list)

@bp.route('/create_item/', methods = ('GET', 'POST'))
def create_item():
    form = ItemForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not g.user:
            return redirect(url_for('auth.login'))
        file = request.files['img']
        data = file.read()
        item = Item(store_name = form.store_name.data, desc = form.desc.data, create_date = datetime.now(), user = g.user,
                            rate = form.rate.data, img=data, location=form.location.data)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('item-form.htm', form = form)

# @bp.route('/modify/<int:item_id>', methods = ('GET', 'POST'))
# @login_required
# def modify(item_id):
#     item = Item.query.get_or_404(item_id)
#     if g.user != item.user:
#         flash('수정 권한이 없습니다.')
#         return redirect(url_for('question.detail_item', item_id = item_id))
#     if request.method == 'POST':
#         form = ItemForm()
#         if form.validate_on_submit():
#             form.populate_obj(item)
#             item.modify_date = datetime.now()
#             db.session.commit()
#             return redirect(url_for('question.detail_item', item_id = item_id))
#     else:
#         form = ItemForm(obj = item)
#     return render_template('item-form.htm', form = form)

@bp.route('/delete_item/<int:item_id>')
@login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    if session['user_id'] != item.user_id:
        flash('삭제 권한이 없습니다')
        return redirect(url_for('question.detail_item', item_id = item_id))
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('question._list_item'))
