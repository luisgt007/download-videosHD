print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ \n")
print("\033[;36;1m" + "DESCARGADOR DE  VIDEOS EN HD. \n" + "\033[0;m")
print("♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ \n")

from pytube import YouTube

print("\033[;31m" + "Acontinuación Pega el enlace o URL. \n" + "\033[0;m")

url_video = input("\033[;35m" + "Ingrese la url del video AQUÍ: \n" + "\033[0;m")

print("\n")

destino = input("\033[;33m" + "Ingrese el destino donde se almacenara el video descargado: \n" + "\033[0;m")


yt = YouTube(url_video)

video = yt.streams.get_highest_resolution()

video.download(destino)

print("\033[;32;1m" + "Video descargado con exito: " + "\033[0;m" + destino)
