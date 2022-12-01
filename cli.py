import pafy
import os
import pyfiglet
import argparse
from dotenv import load_dotenv

load_dotenv()

YT_API_KEY = os.getenv('YT_API_KEY')


def yt_query(*terms, api_key=YT_API_KEY):
    ''' GET VIDEO BY BEST MATCH OF QUERY '''

    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + '+'.join(term for term in terms))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    title = title_from_id(video_ids[0])
    return url


def cli_banner(text):
    print(pyfiglet.figlet_format(text))


def pafy_dl(url):
    video = pafy.new(url)

    # get best resolution regardless of format
    best = video.getbest()
    print(best.resolution, best.extension)

    # Download the video
    best.download()


def cli_main():
    # Create the parser
    my_parser = argparse.ArgumentParser(
        description='Provide a youtube link to download')

    # Define argument behavior
    my_args = {
        '-u': '',
    }

    # Add the arguments
    my_parser.add_argument('-u', '--url',
                           default=False,
                           action="store_true",
                           help="the link to the video",
                           )

    # my_parser.add_argument('Url',
    #                        metavar='url',
    #                        type=str,
    #                        help='the link to the video')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    if args.url:
        url = args.url()
        pafy_dl(url)

    # input_path = args.Path

    # if not os.path.isdir(input_path):
    #     print('The path specified does not exist')
    #     sys.exit()


if __name__ == '__main__':
    cli_banner('DownTube')
    cli_main()
