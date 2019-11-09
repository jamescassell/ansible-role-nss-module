# (c) 2012, Jeroen Hoekx <jeroen@hoekx.be>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re


def regex_search(value, regex, *args, **kwargs):
    ''' Perform re.search and return the list of matches or a backref '''

    groups = list()
    for arg in args:
        if arg.startswith('\\g'):
            match = re.match(r'\\g<(\S+)>', arg).group(1)
            groups.append(match)
        elif arg.startswith('\\'):
            match = int(re.match(r'\\(\d+)', arg).group(1))
            groups.append(match)
        else:
            raise AnsibleFilterError('Unknown argument')

    flags = 0
    if kwargs.get('ignorecase'):
        flags |= re.I
    if kwargs.get('multiline'):
        flags |= re.M

    match = re.search(regex, value, flags)
    if match:
        if not groups:
            if kwargs.get('groupdict'):
                return match.groupdict()
            else:
                return match.group()
        else:
            items = list()
            for item in groups:
                items.append(match.group(item))
            return items


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'regex_search_with_groupdict': regex_search,
        }
