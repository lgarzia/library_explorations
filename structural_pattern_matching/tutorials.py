# %%
def http_error(status):
    match status:
        case 200:
            return 'OK'
        case 400:
            return 'Bad request'
        case 401 | 403 | 404:
            return 'Not allowed'
        case _:
            return 'Something is wrong'
# you can combine multiple conditions in a single pattern using |.
# %%
def get_service_level(user_data: dict):
    match user_data:
        case {'subscription': _, 'msg_type': 'info'}:
            return 'Service level = 0'
        case {'subscription': 'free', 'msg_type': 'error'}:
            return 'Service level = 1'
        case {'subscription': 'premium', 'msg_type': 'error'}:
            return 'Service level = 2'
# %%
class ServiceLevel:
    def __init__(self, subscription, msg_type):
        self.subscription = subscription
        self.msg_type = msg_type
        
    def get_service_level(user_data):
        match user_data:
            case ServiceLevel(subscription=_, msg_type='info'):
                print('Level = 0')
            case ServiceLevel(subscription='free', msg_type='error'):
                print('Level = 1')
            case ServiceLevel(subscription='premium', msg_type='error'):
                print('Level = 2')
            case _:
                print('Provide valid parameters')
# %%
