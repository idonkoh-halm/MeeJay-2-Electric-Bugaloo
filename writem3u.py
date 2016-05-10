def create_m3u():
    genre=(raw_input)
    pla = open(m3u, "wb")
    print "Name of the file: ", pla.name
    pla.write("http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/Jazz/Tank.mp3")
    pla.close()