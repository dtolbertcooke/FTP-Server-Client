from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('FTP-Server-Client')
ftp.retrlines('LIST')

def uploadFile():
    filename = 'Program -1 - Data File.txt'
    ftp.storbinary('STOR ' +filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile():
    filename = 'Program -1 - Data File.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

uploadFile()
downloadFile()
