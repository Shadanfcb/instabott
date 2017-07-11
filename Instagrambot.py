import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

APP_ACCESS_TOKEN = '372728299.6be5ef5.da34ffe315894053818b404943c559ef'

BASE_URL = 'https://api.instagram.com/v1/'


# defining the self info
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get the ID of a user by username


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


#Function declaration to get the info of a user by username


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'No data found for the user!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get your recent post


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Image downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get the recent post of a user by username


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Image downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#Function declaration to get the ID of the recent post of a user by username


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'The user does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'No recent post of the user fpund!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


#Function declaration to like the recent post of a user


def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Post liked!'
    else:
        print 'Unable to like. Try again!'


#Function declaration to make a comment on the recent post of the user


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Added a new comment successfully !"
    else:
        print "We were not able to add comment. Sorry, please try again!"


# Function declaration to get the liked by user


def liked_by_user(insta_username):
    media_id = get_post_id(insta_username)
    print "Get request URL:" + ((BASE_URL + "users/self/media/liked?access_token=%s") % (APP_ACCESS_TOKEN))
    liked = requests.get((BASE_URL + "users/self/media/liked?access_token=%s") % (APP_ACCESS_TOKEN)).json()
    print liked["data"][0]["id"]


# Function declaration to get the comments

def get_the_comments(insta_username):
    media_id = get_post_id(insta_username)
    print "Get request URL:" + ((BASE_URL + "media/%s/comments?access_token=%s") % (media_id, APP_ACCESS_TOKEN))
    comments = requests.get((BASE_URL + "media/%s/comments?access_token=%s") % (media_id, APP_ACCESS_TOKEN)).json()
    print comments["data"]


def start_bot():
    while True:
        print '\n'
        print 'Hello! Welcome to InstagramBot! :D'
        print 'You can choose from the following menu options:'
        print "a.Show your details\n"
        print "b.Show the details of a user by username\n"
        print "c.Show your own recent post\n"
        print "d.Show users recent post\n"
        print "e.Show the list of people who have liked the recent post of a user\n"
        print "f.Like recent post of a user\n"
        print "g.Show the list of comments on the recent post of a user\n"
        print "h.Comment on the recent post of a user\n"
        print "i.Exit"

        choice = raw_input("Please enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter username of the user: ")
            get_user_post(insta_username)
        elif choice == "e":
            insta_username = raw_input("Enter username of the user: ")
            liked_by_user(insta_username)
        elif choice == "f":
            insta_username = raw_input("Enter username of the user: ")
            like_a_post(insta_username)
        elif choice == "g":
            insta_username = raw_input("Enter username of the user: ")
            get_the_comments(insta_username)
        elif choice == "h":
            insta_username = raw_input("Enter username of the user: ")
            post_a_comment(insta_username)
        elif choice == "i":
            exit()
        else:
            print "wrong choice"

start_bot()