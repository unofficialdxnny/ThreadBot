from threads_api.src.threads_api import ThreadsAPI
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def post():
    api = ThreadsAPI()
    
    await api.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'), cached_token_path=".token")
    result = await api.post(caption="Automating the threads account to post quotes using python", image_path="./img.png")


    if result:
        print("Post has been successfully posted")
    else:
        print("Unable to post.")
    
    await api.close_gracefully()
    

async def main():
    await post()

# Run the main function
asyncio.run(main())


'''
This is an unstable API sometimes its 
working and sometimes it is not...
'''