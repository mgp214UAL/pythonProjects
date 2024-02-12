import flet as ft
from pytube import YouTube as YT
import os

def main(page):
    url = ft.TextField(label="URL", autocorrect=True)
    download_video_btn = ft.ElevatedButton("Descargar Video")
    download_audio_btn = ft.ElevatedButton("Descargar Audio")

    def download_video(e):
        current_folder = os.getcwd()
        yt = YT(url.value)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=current_folder)
        print("Descarga de video completada.")

    def download_audio(e):
        current_folder = "E:/"
        yt = YT(url.value)
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        if audio_stream:
            audio_stream.download(output_path=current_folder)
            print("Descarga de audio (MP3) completada.")
        else:
            print("No se encontró una corriente de audio en formato MP3.")

    download_video_btn.on_click = download_video
    download_audio_btn.on_click = download_audio

    page.add(url, download_video_btn, download_audio_btn)

ft.app(target=main)
