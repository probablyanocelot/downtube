import re
import urllib.request
import requests
import pafy
import os
from config import YT_API_KEY

url_pattern = r"/^[a-z](?: [-a-z0-9\+\.])*: (?: \/\/(?: (?: % [0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0} -\x{D7FF}\x{F900} -\x{FDCF}\x{FDF0} -\x{FFEF}\x{10000} -\x{1FFFD}\x{20000} -\x{2FFFD}\x{30000} -\x{3FFFD}\x{40000} -\x{4FFFD}\x{50000} -\x{5FFFD}\x{60000} -\x{6FFFD}\x{70000} -\x{7FFFD}\x{80000} -\x{8FFFD}\x{90000} -\x{9FFFD}\x{A0000} -\x{AFFFD}\x{B0000} -\x{BFFFD}\x{C0000} -\x{CFFFD}\x{D0000} -\x{DFFFD}\x{E1000} -\x{EFFFD}!\$& '\(\)\*\+,;=:])*@)?(?:\[(?:(?:(?:[0-9a-f]{1,4}:){6}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|::(?:[0-9a-f]{1,4}:){5}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){4}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,1}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){3}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,2}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){2}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,3}[0-9a-f]{1,4})?::[0-9a-f]{1,4}:(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,4}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4})?::[0-9a-f]{1,4}|(?:(?:[0-9a-f]{1,4}:){0,6}[0-9a-f]{1,4})?::)|v[0-9a-f]+\.[-a-z0-9\._~!\$&'\(\)\*\+, ; =: ]+)\]|(?: [0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?: \.(?: [0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}|(?: % [0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0} -\x{D7FF}\x{F900} -\x{FDCF}\x{FDF0} -\x{FFEF}\x{10000} -\x{1FFFD}\x{20000} -\x{2FFFD}\x{30000} -\x{3FFFD}\x{40000} -\x{4FFFD}\x{50000} -\x{5FFFD}\x{60000} -\x{6FFFD}\x{70000} -\x{7FFFD}\x{80000} -\x{8FFFD}\x{90000} -\x{9FFFD}\x{A0000} -\x{AFFFD}\x{B0000} -\x{BFFFD}\x{C0000} -\x{CFFFD}\x{D0000} -\x{DFFFD}\x{E1000} -\x{EFFFD}!\$& '\(\)\*\+,;=])*)(?::[0-9]*)?(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+, ; =: @ ]))*)*|\/ (?: (?: (?: (?: % [0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0} -\x{D7FF}\x{F900} -\x{FDCF}\x{FDF0} -\x{FFEF}\x{10000} -\x{1FFFD}\x{20000} -\x{2FFFD}\x{30000} -\x{3FFFD}\x{40000} -\x{4FFFD}\x{50000} -\x{5FFFD}\x{60000} -\x{6FFFD}\x{70000} -\x{7FFFD}\x{80000} -\x{8FFFD}\x{90000} -\x{9FFFD}\x{A0000} -\x{AFFFD}\x{B0000} -\x{BFFFD}\x{C0000} -\x{CFFFD}\x{D0000} -\x{DFFFD}\x{E1000} -\x{EFFFD}!\$& '\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+, ; =: @ ]))*)*)?| (?: (?: (?: % [0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0} -\x{D7FF}\x{F900} -\x{FDCF}\x{FDF0} -\x{FFEF}\x{10000} -\x{1FFFD}\x{20000} -\x{2FFFD}\x{30000} -\x{3FFFD}\x{40000} -\x{4FFFD}\x{50000} -\x{5FFFD}\x{60000} -\x{6FFFD}\x{70000} -\x{7FFFD}\x{80000} -\x{8FFFD}\x{90000} -\x{9FFFD}\x{A0000} -\x{AFFFD}\x{B0000} -\x{BFFFD}\x{C0000} -\x{CFFFD}\x{D0000} -\x{DFFFD}\x{E1000} -\x{EFFFD}!\$& '\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+, ; =: @ ]))*)*|(?!(?: % [0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0} -\x{D7FF}\x{F900} -\x{FDCF}\x{FDF0} -\x{FFEF}\x{10000} -\x{1FFFD}\x{20000} -\x{2FFFD}\x{30000} -\x{3FFFD}\x{40000} -\x{4FFFD}\x{50000} -\x{5FFFD}\x{60000} -\x{6FFFD}\x{70000} -\x{7FFFD}\x{80000} -\x{8FFFD}\x{90000} -\x{9FFFD}\x{A0000} -\x{AFFFD}\x{B0000} -\x{BFFFD}\x{C0000} -\x{CFFFD}\x{D0000} -\x{DFFFD}\x{E1000} -\x{EFFFD}!\$& '\(\)\*\+,;=:@])))(?:\?(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+, ; =: @ ])|[\x{E000} -\x{F8FF}\x{F0000} -\x{FFFFD}\x{100000} -\x{10FFFD}\/\?])*)?(?: \  # (?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@])|[\/\?])*)?$/i"


def title_from_id(title, id, api_key=YT_API_KEY):
    '''
    Uses YouTube API to get first video's title
    '''

    # print('GETTING TITLE FROM ID')
    url = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}')  # .json()
    # url_json = json.loads(url)

    # if can get title, return
    try:
        new_title = url.json()['items'][0]['snippet']['title']
        return new_title

    # else: return whatever was input as first arg
    except:
        return title


def get_vid_list(terms):
    '''
    Gets list of videos matching terms
    '''

    url_terms = '+'.join(terms)  # 'each+term+here'
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + url_terms)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return video_ids


def get_first_match(terms):
    '''
    Returns title and url of first matching video
    '''

    video = get_vid_list(terms)[0]
    # print(video)
    url = "https://www.youtube.com/watch?v=" + video
    title = title_from_id(terms, video)
    return {'title': title, 'url': url}


def pafy_dl_audio(url):
    '''
    Downloads audio from url
    TODO: handle audio/video, etc
    '''
    pafy_video = pafy.new(url)
    print(pafy_video)  # shows video info

    # for stream in pafy_video.streams:
    #     print(stream)

    # get best resolution regardless of format
    # best_video = pafy_video.getbest()
    best_audio = pafy_video.getbestaudio(preftype='m4a')

    print(f'Extension: {best_audio.extension}\nBitrate: {best_audio.bitrate}')
    # print(f'Bitrate: {best_audio.bitrate}')
    print('\n')

    # Download the track
    os.chdir('./dl')
    best_audio.download()


def query_dl(query):
    '''
    Splits query terms by '-', gets first video, downloads
    '''
    # TODO: if url, don't do extra steps
    # if re.match(url_pattern, query):

    search_terms = query.split('-')
    # print(f'SEARCH TERMS :  {search_terms}')

    video = get_first_match(search_terms)
    # print(video)

    url = video["url"]
    title = video["title"]

    print(
        f'------------------------------ DOWNLOADING: {title} ------------------------------')
    pafy_dl_audio(url)


if __name__ == '__main__':
    # "https://www.youtube.com/results?search_query=" + '+'.join(terms)
    terms = ['pantera', 'walk']
    video = get_first_match(terms)
    print(video)
    # url = video.url
    # title = video.title
    # pafy_dl(video)
