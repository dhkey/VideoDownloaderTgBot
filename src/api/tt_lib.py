import requests
import re


def download(video_link, filename='fallback'):
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(video_link, headers=user_agent)
    if r.status_code == 200:
        with open(f'{filename}.mp4', 'wb') as f:
            f.write(r.content)
        print(f'Video downloaded as {filename}.mp4')
    else:
        print(f'Failed to download video from {video_link}.')

def download_tiktok(url):
    # Define user agent to mimic a real browser request
    user_agent = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}
    dl_url = 'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id='

    # Patterns to match TikTok URLs
    mobile_pattern = re.compile(r'(https?://[^\s]+tiktok.com/[^\s@]+)')
    web_pattern = re.compile(r'(https?://www.tiktok.com/@[^\s]+/video/[0-9]+)')

    if mobile_pattern.search(url):
        r = requests.get(url, headers=user_agent) # GET request to resolve the redirection or to fetch the final URL
        id_url = re.search(r'(https?://www.tiktok.com/@[^\s]+/video/[0-9]+)', r.text)
        if id_url:
            tiktok_id = id_url.group().split('/')[-1]
        else:
            print('Failed to extract TikTok ID from mobile URL.')
            return
    elif web_pattern.search(url):
        tiktok_id = url.split('/')[-1]
    else:
        print('Incorrect TikTok URL format.')
        return

    # Fetching video details using the TikTok ID
    r = requests.get(dl_url + tiktok_id, headers=user_agent)
    if r.status_code == 200:
        text = r.json()
        playAddr = text.get("aweme_list", None)[0].get('video', {}).get('play_addr', {}).get("url_list", None)

        if playAddr:
            download(playAddr[0], filename=tiktok_id)  
            return 'Success'
        else:
            return f'Video URL not found for TikTok ID {tiktok_id}.'
    else:
        return f'Failed to fetch video details for TikTok ID {tiktok_id}.'
    
    
download_tiktok("https://vm.tiktok.com/ZMh4Rtg95/")