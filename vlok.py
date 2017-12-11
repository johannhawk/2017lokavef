import sqlite3, datetime, sys
from bottle import route, run, template, debug, template, request, static_file, error, post, get



@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/')
@route('/todo')
@route('/my_todo_list')
def todo_list():
    #connect to database
    con = sqlite3.connect('static/todo.db')
    cur = con.cursor()
    #cur.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    cur.execute("SELECT id, title FROM todo")
    result = cur.fetchall()
    cur.close()
    output = template('make_table', rows=result)
    return output

#kodi fyrir tpl i geymslu ef eitthvað vantar
'''<ul>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</ul>
</table>'''

@route('/new', method=['GET','POST'])#bottle todo newtask
def new_task():
    if request.POST.get('save','').strip():
        todotitle = request.POST.get('task')
        tododesc = request.POST.get('desc')
        tododatetime = datetime.datetime.now()

        #connect database
        con = sqlite3.connect('static/todo.db', timeout=20)
        cur = con.cursor()
        rec = cur.execute('INSERT INTO todo VALUES (null,?,?,?)',(todotitle,tododesc,tododatetime))
        #cur.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        con.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')

        #new_id = cur.lastrowid
        #cur.close()

        return template('make_table.tpl', rows=rows)
        #return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')

#@route("/item1")
@route('/item<item:re:[0-9]+>')
def show_task(item):
    todoid = item
    # connect database
    con = sqlite3.connect('static/todo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM todo WHERE id=?',(todoid))
    rec = cur.fetchone()
    todotitle = rec[1]
    tododesc = rec[2]
    tododate = convDate = datetime.datetime.strptime(rec[3], "%Y-%m-%d %H:%M:%S.%f").strftime("%A %d %B %Y - %I:%M %p")
    if not rec:
        return "Þetta númer er ekki til!"
        # close database
        #con.close()
        

    else:
        output = template('item_task.tpl', todotitle=todotitle, tododesc=tododesc, tododate=tododate)
        return output
        # close database
        #con.close()
        
@route('/edit/<no:int>', method=['GET','POST'])
def edit_item(no):
    todoid = no
    if request.POST.get('save').strip():
        todotitle = request.POST.get('task')
        tododesc = request.POST.get('desc')
        tododatetime = request.POST.get('tdate')

        #connect database
        con = sqlite3.connect('static/todo.db', timeout=20)
        cur = con.cursor()
        rec = cur.execute('UPDATE todo SET title=?,desc=?,datetime=? WHERE id=?',(todotitle,tododesc,tododatetime,todoid))
        con.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY datetime ASC')
        return template('make_table.tpl', rows=rows)

        con.close()

    else:
        con = sqlite3.connect('static/todo.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM todo WHERE id=?',(todoid,))
        rec = cur.fetchone()
        return template("edit_task.tpl", no=no, rec=rec)

        con.close()
        '''

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        con = sqlite3.connect('static/todo.db')
        cur = con.cursor()
        cur.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        con.commit()
        cur.close()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        con = sqlite3.connect('static/todo.db')
        cur = con.cursor()
        cur.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = cur.fetchone()

        return template('edit_task', old=cur_data, no=no)'''

@error(403)
def mistake403(code):
    return 'Error 403: Það er mistök í þínu url!'


#@error(404)
#def mistake404(code):
#    return 'Error404: Þessi síða er ekki til!'

debug(True)
run(app = app,host='0.0.0.0', port=argv[1], debug=True)
#run(host='localhost', port=8080, reloader=True)



