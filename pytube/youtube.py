from pytube import YouTube
from pytube import Playlist


class YTClass:
    def __init__(self, URL):
        self.YT = YouTube(URL)
    
    def __init__(self, URL, isList):
        self.isList = isList
        if(self.isList):
            self.List = Playlist(URL)
        else:
            self.YT = YouTube(URL)
            
    def GetTitle(self):
        if(self.isList):
            return self.List.title
        else:
            return self.YT.title
    
    def GetAllTitle(self):   
        if(self.isList):
            for video in self.List.videos:
                print(f"開始下載:{video.title}")
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
                print(f"下載完成:{video.title}")
        
    def GetViews(self):
        if(self.isList):
            return self.YT.title
        else:
            return self.List.title


if __name__ == '__main__':       
    print('check') 
    yt = YTClass('https://www.youtube.com/playlist?list=PL7BY4zjaOMAgrj9txV3eOIpt3Wevy6ber',True)
    print(f"列表標題:{yt.GetAllTitle()}")

#print(f"Views:{yt.GetViews()}")



