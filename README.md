nss-module
==========

Manage NSS crypto modules and respective slots.

Requirements
------------

`modutil` utility must be available on the managed node.

Role Variables
--------------

```yaml
# the nick name for the module
nss_module_name: Root Certs
# the library path for the module
nss_module_lib: libnssckbi.so
# the path to the nssdb to be managed
nss_module_nssdb: /etc/pki/nssdb

# options 'present', 'absent'
nss_module_state: present

# whether to create a missing nssdb
nss_module_create_db: yes

# list of slots to enable if present
nss_module_slot_whitelist: []
#- /etc/pki/ca-trust/source

# list of slots to disable if present
nss_module_slot_blacklist: []
#- /usr/share/pki/ca-trust-source

# whether to disable all non-whitelisted slots
nss_module_slot_exclusive: no
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- name: add only locally-trusted certificates to the nssdb
  hosts: servers
  vars:
    nss_module_name: Root Certs
    nss_module_lib: libnssckbi.so
    nss_module_slot_blacklist:
    - /usr/share/pki/ca-trust-source
  roles:
  - nss-module
```

License
-------

(Apache-2.0 or MIT or BSD-3-Clause) and GPL-3.0-or-later and BSD-3-Clause

Author Information
------------------

[James Cassell](https://github.com/jamescassell)
