
# This file was generated by 'versioneer.py' (0.15+dev) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json
import sys

version_json = '''
{
 "branch": "HEAD -> master",
 "dirty": false,
 "error": null,
 "full-revisionid": "354042b84d488db38ac1917bb69bd164f4e7f750",
 "version": "1.2.16"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
