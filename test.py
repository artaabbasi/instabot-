from instapy import InstaPy , smart_run

session = InstaPy(username="novatest822", password="avangp23")

session.login()




with  smart_run(session):
    session.set_user_interact(amount=2, randomize=True, percentage=100)
    session.set_do_follow(enabled=True, percentage=100)
    session.set_comments(["عالی بود", "بسیار مفید و آموزنده!"])
    session.set_do_comment(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)
    # session.set_do_story(enabled=True, percentage=100)
    session.set_comment_replies(["راس میگیا", "پخ یییمه"])
    session.set_do_reply_to_comments(enabled=True, percentage=10)
    # session.interact_user_following(['udemy'], amount=2, randomize=True)
    session.interact_by_users(['cristiano'], randomize=True,)
