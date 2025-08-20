import getopt, sys
import yt_dlp

replace_proxy_url = ['piped.kavin.rocks', 'inv.nadeko.net']


def main(file_name):
    url_list = []
    save_path = 'downloads/'

    file = open(file_name)
    for line in file.readlines():
        for rpu in replace_proxy_url:
            if rpu in line:
                line = line.replace(rpu, 'www.youtube.com')
        url_list.append(line)
    file.close()

    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '0'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in url_list:
            error_code = ydl.download(url)


if __name__ == '__main__':
    file_name = ''

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'f:', [])

    for opt, arg in opts:
        if opt in ['-f', '']:
            file_name = arg

    try:
        main(file_name)
    except FileNotFoundError:
        print(f'Error: {file_name} file doesn\'t not found.')