import os
import pytube
import sys

def youtube_preprocess(link):
    """
    Pré-processa um vídeo do YouTube, extraindo o áudio e o título do vídeo.

    Args:
        link: O link do vídeo do YouTube a ser pré-processado.

    Returns:
        O caminho do arquivo de áudio extraído e o título do vídeo.
    """

    # Cria um objeto `pytube.YouTube` para o vídeo especificado.
    yt = pytube.YouTube(link)

    # Registra uma função de callback para ser chamada sempre que um trecho do vídeo for baixado.
    yt.register_on_progress_callback(show_progress_bar)

    # Filtra os streams de vídeo para obter apenas o stream de áudio.
    video = yt.streams.filter(only_audio=True).first()

    # Obtém o título do vídeo.
    video_title = video.title

    # Cria um diretório para armazenar o arquivo de áudio extraído.
    destination = f"./transcription-{video_title}"
    if not os.path.exists(destination):
        os.mkdir(destination)

    # Baixa o stream de áudio do vídeo e o renomeia para um arquivo WAV.
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".wav"
    os.rename(out_file, new_file)

    return new_file, video_title

# Display a download progress bar
def show_progress_bar(stream, _chunk, bytes_remaining):
    """
    Exibe uma barra de progresso de download para o stream de vídeo especificado.

    Args:
        stream: O stream de vídeo a ser baixado.
        _chunk: Um trecho do vídeo que foi baixado.
        bytes_remaining: O número de bytes restantes para serem baixados.
    """

    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = "{0:.1f}".format(current * 100)
    progress = int(50 * current)
    status = "█" * progress + "-" * (50 - progress)

    print(f"Video Download ↳ |{status}| {percent}%\r\n".format(bar=status, percent=percent))

    sys.stdout.flush()
