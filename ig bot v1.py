from time import sleep
from instapy import InstaPy
from instapy.util import smart_run
from getpass import getpass

UN = input("Enter username:  ")
while len(UN) == 0:
    UN = input("Enter username:  ")
PW = getpass("Enter password:  ")
while len(PW)==0:
    PW = input("Enter password:  ")
HT = input("enter hashtags related to your page followed by blank spaces:  ")
while len(HT) == 0:
    HT = input("enter hashtags related to your page followed by blank spaces:  ")
HT_list=HT.split(" ")
print("entered hashtags")
print(HT_list)

#login

session = InstaPy(username=UN, password=PW,headless_browser=False,disable_image_load=False)
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=50,
                                    min_following=75)


  #getting my followers and following

    mwp_followers = session.grab_followers(username="mobile_wallpaper_photography", amount="full", live_match=False, store_locally=True)
    mwp_following = session.grab_following(username="mobile_wallpaper_photography", amount="full", live_match=False, store_locally=True)

   #like by feeds

    session.set_user_interact(amount=1, randomize=True, percentage=25)
    session.set_do_like(enabled=True,percentage=100)
    session.set_comments(['This post is 🔥', 'Really Cool', 'I like your stuff'])
    session.set_do_comment(enabled=True, percentage=33)
    session.like_by_feed(amount=16, randomize=True, unfollow=True, interact=True)
    session.set_dont_like(["nude", "porn","naked"])

    #like by tags

    session.set_do_follow(enabled=True, percentage=75, times=1)
    session.set_comments(["Cool", "Super!","nice"])
    session.set_do_comment(enabled=True, percentage=50)
    session.like_by_tags(HT_list, amount=3)


   #follow likers of followers

    session.set_user_interact(amount=1, randomize=True, percentage=33)
    session.set_do_like(enabled=True,percentage=100)
    session.set_comments(['awesome','nice','great'])
    session.set_do_comment(enabled=True, percentage=20)
    session.follow_likers (mwp_followers, photos_grab_amount = 2, follow_likers_per_photo = 2, randomize=True, sleep_delay=600, interact=True)

    #follow likers of following

    session.set_user_interact(amount=1, randomize=True, percentage=45)
    session.set_do_like(enabled=True,percentage=100)
    session.set_comments(['nice','great'])
    session.set_do_comment(enabled=True, percentage=33)
    session.follow_likers (mwp_following, photos_grab_amount = 2, follow_likers_per_photo = 2, randomize=True, sleep_delay=600, interact=True)


    #follow own followers follower's

    session.set_user_interact(amount=1, randomize=False, percentage=33)
    session.set_do_like(enabled=True,percentage=100)
    session.set_comments(['nice','great'])
    session.set_comments(['good one'], media='Photo')
    session.set_do_comment(enabled=True, percentage=25)
    session.follow_user_followers(mwp_followers, amount=2, randomize=True, sleep_delay=90, interact=True)

    #unfollow

    session.unfollow_users(amount=30, allFollowing=True, style="RANDOM", unfollow_after=3*24*60*60, sleep_delay=450)

session.end()
