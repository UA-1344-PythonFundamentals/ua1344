from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from .models import Post, db
from werkzeug.exceptions import abort
from .forms import PostForm

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, user=current_user)

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if post:
        return render_template('post.html', post=post)
    abort(404)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title=title, content=content, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('routes.index'))

    return render_template('create.html', form=form)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get(id)
    if not post or post.user_id != current_user.id:
        abort(403)

    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('routes.index'))

    return render_template('edit.html', form=form, post=post)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    post = Post.query.get(id)
    if not post or post.user_id != current_user.id:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash(f'"{post.title}" was successfully deleted!')
    return redirect(url_for('routes.index'))
