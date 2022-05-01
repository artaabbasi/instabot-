from rest_framework import serializers
from . import models

class AccountSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.InstagramAccounts
        fields = '__all__'



class IntractSetupSerialaizer(serializers.Serializer):
    amount = serializers.IntegerField()
    randomize = serializers.BooleanField()
    percentage = serializers.IntegerField()

class CommentSetupSerialaizer(serializers.Serializer):
    enabled = serializers.BooleanField()
    percentage = serializers.IntegerField()
    list = serializers.ListField()

class CommentReplySetupSerialaizer(serializers.Serializer):
    enabled = serializers.BooleanField()
    percentage = serializers.IntegerField()
    list = serializers.ListField()

class FollowSetupSerialaizer(serializers.Serializer):
    enabled = serializers.BooleanField()
    percentage = serializers.IntegerField()

class LikeSetupSerialaizer(serializers.Serializer):
    enabled = serializers.BooleanField()
    percentage = serializers.IntegerField()
class BaseSerialaizer(serializers.Serializer):
    accounts = serializers.ListField()
    intract_setup = IntractSetupSerialaizer()
    comment_setup = CommentSetupSerialaizer()
    comment_replies_setup = CommentReplySetupSerialaizer()
    follow_setup = FollowSetupSerialaizer()
    like_setup = LikeSetupSerialaizer()

class MainInteractByComments(serializers.Serializer):
    randomize = serializers.BooleanField()
    reply = serializers.BooleanField()
    interact = serializers.BooleanField()

class InteractByComments(BaseSerialaizer):
    users = serializers.ListField()
    main_setup = MainInteractByComments()

class MainInteractByFollowers(serializers.Serializer):
    randomize = serializers.BooleanField()
    amount = serializers.IntegerField()

class InteractByFollowers(BaseSerialaizer):
    users = serializers.ListField()
    main_setup = MainInteractByFollowers()

class MainInteractByLikers(serializers.Serializer):
    randomize = serializers.BooleanField()
    posts_grab_amount = serializers.IntegerField()
    interact_likers_per_post = serializers.IntegerField()


class InteractByLikers(BaseSerialaizer):
    users = serializers.ListField()
    main_setup = MainInteractByLikers()

class MainInteractByFollowing(serializers.Serializer):
    randomize = serializers.BooleanField()
    amount = serializers.IntegerField()

class InteractByFollowing(BaseSerialaizer):
    users = serializers.ListField()
    main_setup = MainInteractByFollowing()

class MainLikeByTags(serializers.Serializer):
    tags = serializers.ListField()
    use_random_tags = serializers.BooleanField()
    amount = serializers.IntegerField()
    skip_top_posts = serializers.BooleanField()
    use_smart_hashtags = serializers.BooleanField()
    use_smart_location_hashtags = serializers.BooleanField()
    interact = serializers.BooleanField()
    randomize = serializers.BooleanField()

class LikeByTags(BaseSerialaizer):
    main_setup = MainLikeByTags()

class MainLikeByLocations(serializers.Serializer):
    locations = serializers.ListField()
    use_random_tags = serializers.BooleanField()
    amount = serializers.IntegerField()
    skip_top_posts = serializers.BooleanField()
    randomize = serializers.BooleanField()

class LikeByLocations(BaseSerialaizer):
    main_setup = MainLikeByLocations()

class MainLikeByFeed(serializers.Serializer):
    amount = serializers.IntegerField()
    unfollow = serializers.BooleanField()
    randomize = serializers.BooleanField()
    interact = serializers.BooleanField()

class LikeByFeed(BaseSerialaizer):
    main_setup = MainLikeByFeed()
class SendPostSerializer(serializers.Serializer):
    accounts = serializers.ListField()
    media = serializers.CharField()
    caption = serializers.CharField()

class SendStorySerializer(serializers.Serializer):
    accounts = serializers.ListField()
    medias = serializers.ListField()
