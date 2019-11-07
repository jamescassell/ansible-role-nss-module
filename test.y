- hosts: localhost
  gather_facts: no
  tasks:
  - command: modutil -dbdir /etc/pki/nssdb -list
    register: r
    changed_when: no
  - debug:
      msg: >-
        {{ '\n'.decode('string_escape') }}
  - debug:
        #{{ r.stdout }}
      msg: >-
        {{ r.stdout.split('\n\n'.decode('string_escape')) | map('regex_search', '(?s)^ ? ?[0-9]+\. (?P<module>.*?)$.*?\slibrary name: (?P<lib>.*?)$', multiline=True, groupdict=True) | select('mapping') |list}}
#        {{ r.stdout | regex_search('(?s)^ ? ?[0-9]+\. (?P<module>.*?)$\n(?P<config>.*?)(?=\n\n)', multiline=True) }}
#        {{ r.stdout | regex_search('(?s)^ ? ?[0-9]+\. (.*?)$..', multiline=True) }}
  - debug:
      msg: "{{ v1 | zip(v2) | map('combine', thing ,attribute='1') | list }}"
    vars:
     thing: {'thing':'test'}
     v1:
      - thing
      - thing2
     v2:
      - thing: val
        thing2: val
      - thing3: v
        thing4: v2
