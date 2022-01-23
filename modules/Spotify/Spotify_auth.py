import tekore as tk


def Spotify_Auth():
    # auth of Spotify account
    conf = tk.config_from_file("tekore.cfg", return_refresh=True)
    user_token = tk.refresh_user_token(*conf[:2], conf[3])

    # give Spotify acces to API
    spotify = tk.Spotify(conf)
    spotify.token = user_token

    return spotify.token, spotify


def create_credentials():
    print(
        "Please go see https://developer.spotify.com/dashboard/applications and create necessary credentials."
    )

    redirect_uri = input("Your redirect URI paste here: >>> ")
    client_id = input("Your client ID paste here: >>> ")
    client_secret = input("Your client secret paste here: >>> ")

    user_token = tk.prompt_for_user_token(
        client_id, client_secret, redirect_uri, scope=tk.scope.every
    )

    conf = (client_id, client_secret, redirect_uri, user_token.refresh_token)
    tk.config_to_file("tekore.cfg", conf)

    return
