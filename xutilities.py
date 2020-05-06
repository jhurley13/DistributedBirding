# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
# This solution is modified from a recipe in Beazley, D. and B. Jones.
#   Recipe 4.14, Python Cookbook 3rd Ed., O'Reilly Media Inc. Sebastopol, CA: 2013.

from collections import Iterable
import yaml

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

# File looks like
# credentials:
#     username: myusername
#     password: mysupergoodpassword
#     app_id:     c9e43f93cdff4ff59a7de17c4219a0f414929b48c0234c818400c1f67da24564
#     app_secret: 0593518c7a044fa58907f3355082f16290662698e5bc497aa48e038bc3e212ec
#
# Note: hex values generated as follows (random each time):
# import uuid
# print('{}{}'.format(uuid.uuid4().hex, uuid.uuid4().hex))
# print('{}{}'.format(uuid.uuid4().hex, uuid.uuid4().hex))
#
# Alternatively:
# import secrets
# secrets.token_hex(32)


def load_credentials(config_file):
    with open(config_file, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg

