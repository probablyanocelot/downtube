import pafy
import os
import pyfiglet
import argparse
import search_yt


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

    # Add the arguments
    my_parser.add_argument('Url',
                           metavar='url',
                           type=str,
                           help='the link to the video')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    url = args.Url

    pafy_dl(url)

    # input_path = args.Path

    # if not os.path.isdir(input_path):
    #     print('The path specified does not exist')
    #     sys.exit()


if __name__ == '__main__':
    cli_banner('DownTube')
    cli_main()
