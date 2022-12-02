Requirements:  
    - Python  
    - YouTube API key  

Installation:

    - Install Required Python Packages  
        pip install -r requirements.txt  
        
    - Remove or Comment Lines in the 'pafy' python package, usually `~/Lib/site-packages/pafy`:
            self._likes = self._ydl_info['like_count']  
            self._dislikes = self._ydl_info['dislike_count']  
            
    - Create a file named `.env` in project root directory that contains:  
            YT_API_KEY = whatever_your_api_key_is  

Usage:  
    In project root dir,  

    Download by query:  
        python dt.py separate-query-with-hyphens  

    Download by url:  
        python dt.py -u https://the.url.goes/here  

TODO: encoding  
TODO: better readme  
