import pafy
import pyfiglet
import argparse
import yt


def cli_banner(text):
    print(pyfiglet.figlet_format(text))


def cli_main():
    # Create the parser
    my_parser = argparse.ArgumentParser(
        description='Download a video from YouTube')

    # Add the arguments
    my_parser.add_argument('-u', '--url',
                           default=False,
                           action="store_true",
                           help="the link to the video",
                           )

    my_parser.add_argument('Query',
                           metavar='query',
                           type=str,
                           help='search by keywords')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    if args.Query:
        query = args.Query
        print(f'QUERY :  {query}')
        search_terms = query.split('-')
        print(f'SEARCH TERMS :  {search_terms}')

        video = yt.get_first_video(search_terms)

        url = video.url
        title = video.title

    if args.url:
        url = args.url()
        yt.pafy_dl(url)

    # input_path = args.Path

    # if not os.path.isdir(input_path):
    #     print('The path specified does not exist')
    #     sys.exit()


if __name__ == '__main__':
    cli_banner('DownTube')
    cli_main()
