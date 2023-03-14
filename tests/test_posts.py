

from app.schemas import PostOut


def test_get_all_posts(authorized_client, test_posts):

    res = authorized_client.get("/posts/")
    data = res.json()
    posts = [PostOut(**post) for post in data]

    assert res.status_code == 200
    assert len(posts) == len(test_posts)
    # assert posts[0].Post.id == test_posts[0].id


def test_unauth_user_get_all_post(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauth_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_unauth_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
