import json
import os
def load_data():
    file_path = os.path.join('youtube_manager', 'youtube.txt')  
    try:
        with open(file_path,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    file_path = os.path.join('youtube_manager', 'youtube.txt') 
    with open(file_path,'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("*"*125 )
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']}, Duration:{video['time']}")
    print("*"*125 )
    
def add_video(video):
    name=input("enter video name:\t")
    time=input("enter video time:\t")
    video.append({"name":name,"time":time})
    save_data_helper(video)

def update_video(video):
    list_all_videos(video)
    index=int(input("enter the video number to update :\t"))
    if 1<=index<=len(video):
        name=input("enter the new video name :\t")
        time=input("enter the new video duration:\t")
        video[index-1]={"name":name,"time":time}
        save_data_helper(video)
    else:
        print('invalid index salected')

def delete_video(video):
    list_all_videos(video)
    index=int(input("enter the video number to delete:\t"))
    if 1<=index<=len(video):
        del video[index-1]
        save_data_helper(video)
    else:
        print("Invalid syntax")

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager")
        print("1. list the favourite video")
        print("2. add a youtube video")
        print("3. update a youtube video detail")
        print("4. delete a youtube video")
        print("5.  exit the app")
        choice= input("enter your choice:\t")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Syntax")
        
if __name__ == "__main__":
    main()
