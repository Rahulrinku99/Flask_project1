from flask import Flask

FAI=Flask(__name__)
@FAI.route('/wish')
def wish():
    return 'This is flask project'
 
 
@FAI.route('/server')
def server():
    return 'server running successfully'

if __name__=='__main__':
    FAI.run(debug=True)



