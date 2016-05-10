import flask
import linkcreator as lc
myapp=flask.Flask('Hello')

@myapp.route('/',methods=['POST','GET'])
def getm3u():
    if flask.request.method=='GET':
        html=file ('UI.html','r').read()
        return html
    else:
        #If it is post
        return str(flask.request.form)

@myapp.route('/USER_select_genre',methods=['POST'])
def genre_get():
    genre1=flask.request.form['genre1']
    genre2=flask.request.form['genre2']
    genre3=flask.request.form['genre3']
    genre4=flask.request.form['genre4']
    genre5=flask.request.form['genre5']
    genre6=flask.request.form['genre6']
    print "flask.send_file(lc.generate_m3us_for_genres_samples('MeeJay Playlist',",[genre1,genre2,genre3,genre4,genre5,genre6],2,"))"
    return flask.send_file(lc.generate_m3us_for_genres_samples('MeeJay Playlist',[genre1,genre2,genre3,genre4,genre5,genre6],2))

myapp.run(debug=True)

print 'hey look at me! I exist in github now!'