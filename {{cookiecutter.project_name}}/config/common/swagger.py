# swagger 文档配置
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'DOC_EXPANSION': None,
    'SHOW_REQUEST_HEADERS': True,
    'USE_SESSION_AUTH': False,
    'APIS_SORTER': 'alpha',
    'JSON_EDITOR': True,
    'OPERATIONS_SORTER': 'alpha',
    'VALIDATOR_URL': None,
    'TAGS_SORTER': 'alpha',
    'DEFAULT_MODEL_DEPTH': -1
}
