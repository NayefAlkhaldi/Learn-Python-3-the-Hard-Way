from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code != 404

    rv = web.get('/game', follow_redirects=True)
    assert rv.status_code == 200
    assert b"Gothons From Planet Percal #25" in rv.data

    data = {'action': 'shoot!'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert b"You died." in rv.data