import math
import os

from pydub import AudioSegment
from pydub.utils import make_chunks


def chunk_by_size(my_file, video_title):
    """
    Divide um arquivo de áudio em trechos de um tamanho específico.

    Args:
        my_file: O caminho do arquivo de áudio a ser dividido.
        video_title: O título do vídeo a partir do qual o arquivo de áudio foi extraído.

    Returns:
        O número total de trechos.
    """

    # Carrega o arquivo de áudio.
    myaudio = AudioSegment.from_file(my_file)

    # Obtém o número de canais, a largura de amostra, a duração em segundos, a taxa de amostragem e a profundidade de bits do arquivo de áudio.
    channel_count = myaudio.channels
    sample_width = myaudio.sample_width
    duration_in_sec = len(myaudio) / 1000
    sample_rate = myaudio.frame_rate
    bit_depth = sample_width * 8

    # Calcula o tamanho do arquivo WAV em bytes.
    wav_file_size = (sample_rate * bit_depth * channel_count * duration_in_sec) / 8

    # Define o tamanho de cada trecho em bytes.
    file_split_size = 24000000  # 24Mb OR 24,000,000 bytes

    # Calcula o número total de trechos.
    total_chunks = wav_file_size // file_split_size

    # Calcula a duração de cada trecho em segundos.
    chunk_length_in_sec = math.ceil((duration_in_sec * file_split_size) / wav_file_size)

    # Converte a duração de cada trecho em milissegundos.
    chunk_length_ms = chunk_length_in_sec * 1000

    # Divide o arquivo de áudio em trechos.
    chunks = make_chunks(myaudio, chunk_length_ms)

    # Cria o diretório para armazenar os trechos de áudio.
    if not os.path.exists(f"./transcription-{video_title}/process_chunks"):
        os.mkdir(f"./transcription-{video_title}/process_chunks")

    # Exporta cada trecho de áudio como um arquivo WAV.
    for i, chunk in enumerate(chunks):
        chunk_name = f"./transcription-{video_title}/process_chunks/chunk{i}.wav"
        chunk.export(chunk_name, format="wav")

    return total_chunks
