from app.schemas import PostOut


def test_get_all_posts(authorized_client, test_posts):

    res = authorized_client.get("/posts/")
    data = res.json()
    posts = [PostOut(**post) for post in data]

    assert res.status_code == 200
    assert len(posts) == len(test_posts)
    # assert posts[0].Post.id == test_posts[0].id


def test_get_one_post(authorized_client, test_posts):

    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/8888")
    assert res.status_code == 404


def test_unauth_user_get_all_post(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauth_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


# def test_create_post(authorized_client, test_user, test_posts):
