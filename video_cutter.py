"""
Esse codigo corta videos. caso você não queira baixar nenhum software para fazer cortes em seu video.

By: George Telles
+55 11 93290-7425
"""

from moviepy.video.io.VideoFileClip import VideoFileClip

def cortar_video(input_path, output_path, start_time, end_time):
    video = VideoFileClip(input_path)
    video_duration = video.duration
    end_time = video_duration - 38 if video_duration > 38 else 0
    
    video_cortado = video.subclip(start_time, end_time)
    video_cortado.write_videofile(output_path, codec="libx264")
    
    video.close()

# Caminho do vídeo de entrada
input_path = "C:/Users/George Telles/Desktop/OpEx_668_HD.MKV"

# Caminho do vídeo de saída após o corte
output_path = "C:/Users/George Telles/Desktop/OpEx_668_HD_EDIT.MKV"

# Tempo de início (em segundos)
start_time = 312

# Chama a função para cortar o vídeo
cortar_video(input_path, output_path, start_time, None)

