import pytest
from blog.models import Post

# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db

#def test_published_posts_only_returns_those_with_published_status():
#    assert False

def test_publish_sets_status_to_published():
    post = mommy.make('blog.Post', status=Post.DRAFT)
    post.publish()
    assert post.status == Post.PUBLISHED
