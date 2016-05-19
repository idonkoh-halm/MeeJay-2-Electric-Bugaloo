import sys
import urllib2
import random
import glob
from os.path import expanduser as host_music_library
class Text_Output:
    '''
    from a bunch of user defined links, this will attempt to take those links
    and add them line by line to create a m3u file.
    '''
    def ___init___(self,filename):
        self.f = file(filename,'w')
    def new_text (self, txt):
        self.f.write(txt+'\n') #creates a new line
    def output_list(self, url_list):
        txt=''
        for itm in data_list:
            txt+= str(itm)+'\n'
            
    
    def finish(self):
        self.f.close()

def generate_m3u(playlist_name,songs):
    "Takes what is generated from make html, and generates an .m3u"
    playlist_name_m3u=playlist_name+".m3u"
    pla = open(playlist_name_m3u, "wb")

    print "Name of the file: ", pla.name
    for song in songs:
        pla.write(str(make_html(song,)))
        #pla.write(str(make_html(song,"/Users/programmer/Documents/Meejay/Music Directory/%s/"%m3u_name)))
        pla.write('\n')
    pla.close()
    return playlist_name_m3u
# Hinkle's reworking of above..
def make_html (song_path): #="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/"):
    '''
    argument "song_path" is wrapped around the root directory in order to create a proper path name.
    Example: takes word "tank", and changes it to "http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/tank"
    '''

    newlink=song_path#+urllib2.quote(song_path)#+".mp3"
    return newlink
    text_output=Text_Output()
    text_output.new_text(newlink)



def generate_m3us_for_genres(playlist_name, genres):
    songs=[]
    for genre in genres:
        songs.extend(song_data[genre])
    return generate_m3u(playlist_name,songs)



def generate_m3us_for_genres_samples(playlist_name, genres,sample_count):
    songs=[]
    for genre in genres:
        if genre!='blank':
            songs.extend(random.sample(song_data[genre],sample_count))
    return generate_m3u(playlist_name,songs)


song_data ={
    'Rock':glob.glob(host_music_library("~/Music/Meejay Music Directory/Rock/*.mp3")),
    'Rap' : glob.glob(host_music_library("~/Music/Meejay Music Directory/Rap/*.mp3")),
    'Jazz' : glob.glob(host_music_library("~/Music/Meejay Music Directory/Jazz/*.mp3")),

    'vg_ost':glob.glob(host_music_library("~/Music/Meejay Music Directory/vg_ost/*.mp3")),
    'pcast_edu':[],
    'pcast_sports':[],
    'pcast_comedy':glob.glob(host_music_library("~/Music/Meejay Music Directory/pcast_comedy/*.mp3")),
    'pcast_vidja':glob.glob(host_music_library("~/Music/Meejay Music Directory/pcast_vidja/*.mp3"))


    }

if __name__ == '__main__':
    for genre,songs in song_data.items():
        generate_m3u(genre,songs)


    #def texttohtml():
    #    directory="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/JetSetRadio/"
    #    text=raw_input('Enter normie text here')
    #    newlink=directory+urllib2.quote(text)+".mp3"
    #    print newlink

    #generate_m3us_for_genres('pytest-rock-rap',['Rock','Rap'])
    #generate_m3us_for_genres('pytest-just-rock',['Rock'])
    #generate_m3us_for_genres('pytest-jazz-rock',['Rock','Jazz'])
    #generate_m3us_for_genres_samples('Sample Rock and Jazz',['Rock','Jazz'],1)
    #generate_m3us_for_genres_samples('Sample Rock and Jazz2',['Rock','Jazz'],2)
    #generate_m3us_for_genres_samples('Sample Rock and Jazz3',['Rock','Jazz'],3)
    #generate_m3us_for_genres_samples('Sample All',['Rock','Jazz','Rap'],2)

    #DEPRECATED CODE
    #def get_url_from_user ():
    #    print texttohtml(raw_input('Enter normie text here'))
    #texttohtml("touch and go")
    #get_url_from_user()
    #m3u_generator('playlist.txt')
