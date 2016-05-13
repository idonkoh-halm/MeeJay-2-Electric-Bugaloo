import sys
import urllib2
import random

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
        pla.write(str(make_html(song,"/Users/programmer/Documents/MeeJay-2--Electric-Bugaloo/Meejay Music Directory/")))
        #pla.write(str(make_html(song,"/Users/programmer/Documents/Meejay/Music Directory/%s/"%m3u_name)))
        pla.write('\n')
    pla.close()
    return playlist_name_m3u
# Hinkle's reworking of above..
def make_html (song_path, directory): #="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/"):
    '''
    argument "song_path" is wrapped around the root directory in order to create a proper path name.
    Example: takes word "tank", and changes it to "http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/tank"
    '''
    newlink=directory+urllib2.quote(song_path)+".mp3"
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
    'Rock':['%sThe Toadies - Possum Kingdom'%'Rock/','%sQueen - Another One Bites the Dust'%'Rock/',
            '%sPearl Jam - Life Wasted'%'Rock/','%sThe Fratellis - Whistle for the Choir'%'Rock/'],
    'Rap' : ['%s01 Ultralight Beam'%'Rap/','%sLupe Fiasco - SNDCLSH in Vegas'%'Rap/',
             '''%sLupe Fiasco - WWJD He'd Prolly LOL Like WTF!!!'''%'Rap/''','%sRJD2 - Ghostwriter'%'Rap/'],
    'Jazz' : ['%sVince Guaraldi Trio - Pebble Beach'%'Jazz/','%sVince Guaraldi Trio - Christmas Time Is Here (instrumental)'%'Jazz/',
              '%sThe Seatbelts - COSMOS'%'Jazz/','%sThe Seatbelts - TOO GOOD TOO BAD'%'Jazz/','%sThe Seatbelts - Tank!'%'Jazz/','%sMiles Davis _ John Coltrane - Blue in Green'%'Jazz/',
            '%sRed Garland - Almost Like Being in Love'%'Jazz/', '%sSonny Rollins - God Bless the Child'%'Jazz/',
            '%sThe Seatbelts - CAT BLUES'%'Jazz/', '%sThe Seatbelts - The EGG and I'%'Jazz/',
            '%sVince Guaraldi - Oh, Good Grief!'%'Jazz/', '%sVince Guaraldi - Skating'%'Jazz/',
            '%sVince Guaraldi Trio - Baseball Theme'%'Jazz/', '%sVince Guaraldi Trio - Blue Charlie Brown'%'Jazz/',
            '%sVince Guaraldi Trio - Great Pumpkin Waltz'%'Jazz/', '%sVince Guaraldi Trio - O Nosso Amor.mp3,'%'Jazz/',],
    'vg_ost':['%s01-hideki-naganuma-let-mom-sleep'%'vg_ost/',  '%s02-hideki-naganuma-humming-the-bassline'%'vg_ost/' ,
              '%s05-hideki-naganuma-sneakman'%'vg_ost/', '%s08-let-mom-sleep-no-sleep-mix-'%'vg_ost/',
              '%s09-hideki-naganuma-rock-it'%'vg_ost/','%s14-teknopathetic.mp3'%'vg_ost/'],
    'pcast_edu':[],
    'pcast_sports':[],
    'pcast_comedy':['%sHARMONTOWN 193'%'pcast_comedy/','%sMAGIC TABERN 001'%'pcast_comedy/','%sWAIT WAIT - 002'%'pcast_comedy/'],
    'pcast_vidja':['%sTOVG - 087'%'pcast_vidja/','%sCO-OPTIONAL-121'%'pcast_vidja/']


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
print 'hey look at me! I exist in github now!'
