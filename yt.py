import re
import urllib.request
import requests
from config import YT_API_KEY


def title_from_id(title, id, api_key=YT_API_KEY):
    print('GETTING TITLE FROM ID')
    url = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}')  # .json()
    # url_json = json.loads(url)
    try:
        new_title = url.json()['items'][0]['snippet']['title']
        return new_title
    except:
        return title


def get_vid_list(terms, api_key=YT_API_KEY):
    ''' GET VIDEO BY BEST MATCH OF QUERY '''

    print(terms)
    url_terms = '+'.join(terms)
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + url_terms)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return video_ids


def get_first_video(terms):
    video = get_vid_list(terms)[0]
    print(video)
    url = "https://www.youtube.com/watch?v=" + video
    title = title_from_id(terms, video)
    return {'title': title, 'url': url}


def pafy_dl(video):
    url = video.url
    title = video.title
    pafy_video = pafy.new(url)
    print(pafy_video)

    # get best resolution regardless of format
    best = pafy_video.getbest()
    print(best.resolution, best.extension)

    # Download the video
    best.download()


if __name__ == '__main__':
    # "https://www.youtube.com/results?search_query=" + '+'.join(terms)
    terms = ['pantera', 'walk']
    video = get_first_video(terms)
    print(video)
    # url = video.url
    # title = video.title
    # pafy_dl(video)
