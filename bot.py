from playwright.sync_api import sync_playwright
import os

email = os.environ.get('email')
password = os.environ.get('password')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.newPage()
    # Open the TikTok trending page
    page.goto('https://proxitok.pabloferreiro.es/tag/fyp', timeout = 30000)

    # Select the first video on the page
    video = page.querySelector('body > section.section > div.container > article:nth-child(1) > div > div:nth-child(8) > div:nth-child(2) > div.dropdown-menu > div > a:nth-child(2)')
    
    # Get the video URL
    video_url = video.getAttribute('href')

    # Download the video
    page.goto(video_url)
    page.waitForSelector('video')
    video_data = page.querySelector('video').screenshot()
    with open('video.mp4', 'wb') as f:
        f.write(video_data)
        
#Login to Youtube
    page.goto('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    email_input = page.querySelector('input#identifierId')
    email_input.type(email)
    next_btn = page.querySelector('div#identifierNext > span > span')
    next_btn.click()
    pass_input = page.querySelector('input[name="password"]')
    pass_input.type(password)
    signin_btn = page.querySelector('div#passwordNext > span > span')
    signin_btn.click()

#Upload video
    upload_btn = page.querySelector('#logo-icon-container > yt-img-shadow > img')
    upload_btn.click()
    upload_vid_btn = page.querySelector('paper-button#upload-prompt-box > div > input')
    upload_vid_btn.uploadFile('video.mp4')
    upload_confirm_btn = page.querySelector('#start-upload-button-single > span > span')
    upload_confirm_btn.click()

#Done
    print("Video successfully uploaded!")
