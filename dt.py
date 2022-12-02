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
        # print(f'QUERY :  {query}')
        yt.query_dl(query)

    if args.url:
        url = args.url()
        yt.pafy_dl_audio(url)

    print('------------------------------ DOWNLOAD COMPLETE ------------------------------')

    # input_path = args.Path

    # if not os.path.isdir(input_path):
    #     print('The path specified does not exist')
    #     sys.exit()


def cli_secondary():
    query = input('[X] Next download query (use-hyphens): ')

    if query == 'exit':
        sys.exit()

    yt.query_dl(query)


if __name__ == '__main__':
    cli_banner('DownTube')
    cli_main()
