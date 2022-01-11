from flask import Flask, render_template, redirect
from form import MessageForm
from config import Config

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_to_do_list = []
def addToDoItem(toDo):
  global my_to_do_list
  my_to_do_list.append(toDo)

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form = MessageForm()
  if form.is_submitted():
    print("made it")
    addToDoItem(form.toDo.data)
    return redirect('/display')
  return render_template('pageOne.html', form=form)

@app.route('/display')
def page_two():
  return render_template('pageTwo.html', my_to_do_list=my_to_do_list)

app.run(host='0.0.0.0', port=8080)