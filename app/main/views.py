from . import main
from flask import render_template,request,redirect,url_for,abort,flash
# from  .import get_quote
from ..models import Bill,User
from .forms import BillForm,UpdateProfile,DeleteForm
from .. import db,photos
from flask_login import login_required,current_user


@main.route('/')
def index():
  # random_quote = get_quote()  

  bills = Bills.query.all()
  Housing = Bill.query.filter_by(category='Housing').all()
  Utilities = Bill.query.filter_by(category='Utilities').all()
  car = Blog.query.filter_by(category='Car').all()
  Living = Bill.query.filter_by(category='Living Expenses').all()

  return render_template('index.html',Housing=Housing,Utilities=Utilities,car=car,Living = Expenses)


@main.route('/bill/new',methods = ['GET','POST'])
@login_required
def new_bill():
  form = billForm()

  if form.validate_on_submit():
    title=form.title.data
    category = form.category.data
    bill = form.bill_post.data
    writer= form.writer.data
    biller = current_user
    new_bill = bill(title=title,category=category,bill=bill,biller=current_user._get_current_object().id)

    db.session.add(new_bill)
    db.session.commit()

    flash('Your Bill has been added...','success')
    return redirect(url_for('main.index',id=new_bill.id))

  return render_template('new_bill.html',title='Add Your Bill',bill_form=form)

@main.route('/delete_bill/<int:id>',methods =['POST'])
@login_required
def delete_bill(id):
  
  bill = Bill.query.get_or_404(id)
  if bill.biller != current_user:
    abort(403)
  db.session.delete(bill)
  db.session.commit()
  flash('Your bill has been deleted!', 'success')
  return redirect(url_for('main.index'))
    
  return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort (404)
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()

  return redirect(url_for('main.profile',uname=uname))


# @main.route('/comments/<int:id>',methods=['GET','POST'])
# def comment_review(id):
#   comment = CommentForm()
#   blog=Blog.query.get(id)

  # if comment.validate_on_submit():
  #   content = comment.comment.data
    
  #   new_post = Comment(comment=content,topic=blog.id)

  #   db.session.add(new_post)
  #   db.session.commit()  
    
  # post = 'Share Your Sentiments'
  # user=User.query.get(id)
  # comments = Comment.query.filter_by(topic=blog.id).all()  
  # if blog is None:
  #   abort(404)
  
  # return render_template('blog_comments.html',comment_form=comment,post=post,comments=comments,blog=blog,user=user)

# @main.route('/delete_comment/<blog_id>/<comment_id>',methods=['POST'])
# @login_required
# def delete_comment(blog_id,comment_id): 
  
  # blog = Blog.query.filter_by(id = blog_id).first()
  # comments = Comment.query.filter_by(topic = blog.id).order_by(Comment.posted.desc())
  # comment = Comment.query.filter_by(id = comment_id).first()
  # if blog.user_id == current_user.id:

  #   Comment.delete_comment(comment)

  # return render_template('blog_comments.html', blog = blog, comments = comments)
  # comment_form = CommentForm()
  # blog=Blog.query.get(id)
  # comment = Comment.query.filter_by(id = comment_id).first()
  # comments = Comment.query.filter_by(topic=blog.id).all()

  # if comment.validate_on_submit():
  #   content = comment.comment.data
    
  #   new_post = Comment(comment=content,topic=blog.id)

  #   db.session.add(new_post)
  #   db.session.commit()  

  # if blog.user_id == current_user.id:

  #   Comment.delete_comment(comment)
  #   return redirect('main.comment_review')
    
  # post = 'Share Your Sentiments'
  # user=User.query.get(id)
    
  # if blog is None:
  #   abort(404)
  
  # return render_template('blog_comments.html',comment_form=comment_form,post=post,comments=comments,blog=blog,user=user)
