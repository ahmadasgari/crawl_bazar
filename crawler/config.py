BASE_URL = 'https://api.cafebazaar.ir/rest-v1/process/GetPageV2Request'

HEADER = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}
payload = {
    'properties': {
        "clientID": "xosfmx0w3h4imuraeuzo6drbadccuqsh",
        "clientVersion": "web",
        "deviceID": "xosfmx0w3h4imuraeuzo6drbadccuqsh",
        "language": 2
    },
    "singleRequest": {"getPageV2Request": {"path": "category_entertainment"}}
}

CATEGORIES = [
    'home-app',
    'category_weather',
    'category_food-drink',
    'category_education',
    'category_tools',
    'category_finance',
    'category_medical',
    'category_health-fitness',
    'category_shopping',
    'category_maps-navigation',
    'category_lifestyle',
    'category_entertainment',
    'category_travel-local',
    'category_social',
    'category_personalization',
    'category_photography',
    'category_books-reference',
    'category_kids-apps',
    'category_religious',
    'category_music-audio',
    'category_sports',
    'home-game',
    'category_strategy',
    'category_action',
    'category_arcade',
    'category_casual',
    'category_racing',
    'category_simulation',
    'category_word-trivia',
    'category_kids-games',
    'category_puzzle',
    'category_sports-game',
]
