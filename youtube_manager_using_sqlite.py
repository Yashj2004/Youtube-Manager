import sqlite3
conn= sqlite3.connect('youtube_manager.db')
cur=conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
            ''')
def list_video():
    cur.execute('select * from videos')
    for row in cur.fetchall():
        print(row)

def add_video(name , time):
    cur.execute("insert into videos(name, time) values(?,?)",(name,time))
    conn.commit()

def update_video(id , name , time):
    cur.execute('update videos set name=? , time=? where id =?' ,(name ,time,id))
    conn.commit()

def delete_video(id):
    cur.execute('delete from videos where id =?',(id,))
    conn.commit()
def main():
    while True:
        print('''
              YOUTUBE MANAGER
              1. list videos
              2. add videos
              3. update videos
              4. delete videos
              5. exit 
            ''')
        choice= input("enter your choice:\t")
        match choice:
            case '1':
                list_video()

            case '2':
                name =input("enter the name of video:\t")
                time =input("enter the time of video:\t")
                add_video(name , time)

            case '3':
                id=int(input("enter video id to update:\t"))
                name =input("enter the new name of video:\t")
                time =input("enter the new time of video:\t")
                update_video(id , name , time)
            case '4':
                id= int(input("enter the video id to delete :\t"))
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid syntax")
    conn.close()
if __name__=='__main__':
    main()
