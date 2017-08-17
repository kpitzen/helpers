'''Catch-all repo for helpful functions'''

DYNAMO_TYPE_MAP = {str: 'S', float: 'N', int: 'N', type(None): 'S'}

#TODO: Add recursion
def format_python_dict_for_dynamo(python_dict):
    '''given a python hash table, return a dynamo-ready payload'''
    output_payload = {}
    for key, value in python_dict.items():
        try:
            if not value:
                continue
        except TypeError:
            pass
        try:
            DYNAMO_TYPE_MAP[type(value)]
        except KeyError:
            print(key, value, type(value))
            raise NotImplementedError('This type is not yet supported: {}'.format(type(value)))
        else:
            output_payload[str(key)] = {DYNAMO_TYPE_MAP[type(value)]: str(value)}
    return output_payload

def parse_config_section_to_dict(config, section):
    output_dict = {}
    for key, value in config[section].items():
        output_dict[key] = value
    return output_dict
