from flask import Flask, render_template, redirect
from form import MessageForm
from formRemove import RemoveForm
from config import Config

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_to_do_list = []
def addToDoItem(toDo):
  global my_to_do_list
  my_to_do_list.append(toDo.upper())
  print(my_to_do_list)

def removeToDoItem(remove):
  global my_to_do_list
  print(remove)
  my_to_do_list.remove(remove.upper())

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form = MessageForm()
  formRemove = RemoveForm()

  if form.is_submitted():
    print("about to add")
    addToDoItem(form.toDo.data)
    return redirect('/display')
  # if formRemove.is_submitted():
  #   print("about to remove")
  #   removeToDoItem(formRemove.remove.data)
  #   return redirect('/display')
  return render_template('pageOne.html', form=form, my_to_do_list=my_to_do_list, formRemove=formRemove)

@app.route('/display', methods=['GET', 'POST'])
def page_two():
  formRemove = RemoveForm()
  
  if formRemove.is_submitted():
    print("about to remove")
    removeToDoItem(formRemove.remove.data)
    return redirect('/display')
  return render_template('pageTwo.html', my_to_do_list=my_to_do_list, formRemove=formRemove)

app.run(host='0.0.0.0', port=8080)