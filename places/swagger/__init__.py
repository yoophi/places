from os import path
import yaml


def get_swagger_spec():
    _current_dir = path.dirname(path.abspath(__file__))
    spec = {
        'info': {
            'description': None
        }
    }

    with open(path.join(_current_dir, 'SWAGGER_SPEC.yaml'), 'r') as spec_file:
        spec.update(yaml.load(spec_file.read()))

    with open(path.join(_current_dir, 'API_DESCRIPTION.md'), 'r') as description_file:
        spec['info']['description'] = description_file.read()

    return spec
