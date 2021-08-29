try:
    from json.decoder import JSONDecodeError # Json error
    import requests # The hearth of the script
    from twocaptcha import TwoCaptcha # This is brain because solving captcha for us :)
except ImportError:
    print("Import Error, maybe you forget to run 'pip install -r requirements.txt'")

vote_count = 0 # Vote count

site_key = "6LfDlbAbAAAAALJvKffc-P-uv5EVxTN9gdyO1O4x" # Google site key

api_key = "" # 2captcha api key

solver = TwoCaptcha(api_key) # 2captcha client

token_url = "" # Watcher.guru token page url. Example(https://watcher.guru/coin/minibitcoin)

token = "" # Watcher.guru token code (if you don't know how to get this, look README.md->Getting token)

proxies = open("path/my_proxies.txt","r").read().split("\n") # Open proxy list file


def Upvote(proxy,token,token_url): # Upvote functions
    try:
        global vote_count # set vote_count globally because after voting this will change
        print("Solving Captcha...") # if you don't know this close the script and go to (https://www.youtube.com/results?search_query=python+course).
        result = solver.recaptcha(sitekey=site_key,url=token_url) # This will solve the captcha and return response code
        print("Captcha Solved!")
        http_proxy  = f"http://{proxy}" # Some proxy stuffs
        https_proxy = f"http://{proxy}" # //
        ftp_proxy   = f"http://{proxy}" # //
        proxyDict = { "http":http_proxy,"https":https_proxy,"ftp":ftp_proxy} # //
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'} # Request headers
        data = '{"token":"%s","captcha":"%s"}'%(token,result['code']) # This data sending to vote site by post
        print("Trying to vote..")
        response = requests.post('https://api2.watcher.guru/coinvote/create', headers=headers, data=data, proxies=proxyDict) # Yes everything is this, this makes vote
        print("ERROR: "+ str(response.json().get("message"))) # If response is a json then we have a problem, look output to find problem
        return # This just finish the functions
    except JSONDecodeError: # If we succeeded to vote then response is not a json and we won
        print(f"Vote success, Total Vote: {vote_count}") # This message will you be happy and you can see how many vote you sent
    else:
        return # You know what is this



if __name__ == "__main__": # Actually still i don't know why i should to use this
    for proxy in proxies:
        Upvote(proxy,token,token_url)