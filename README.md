[![Actions Status - Master](https://github.com/juju4/ansible-sleuthkit/workflows/AnsibleCI/badge.svg)](https://github.com/juju4/ansible-sleuthkit/actions?query=branch%3Amaster)
[![Actions Status - Devel](https://github.com/juju4/ansible-sleuthkit/workflows/AnsibleCI/badge.svg?branch=devel)](https://github.com/juju4/ansible-sleuthkit/actions?query=branch%3Adevel)

This role will build deb package for Sleuthkit and install it locally.
It use recent version (4.6.5 at Mar 2019) unlike current Ubuntu LTS (Xenial has 4.2.0, Bionic 4.4.2).
Debian rules thanks to [log2timeline team](https://github.com/log2timeline/l2tdevtools)!

https://github.com/sleuthkit/sleuthkit/

# Requirements & Dependencies

### Ansible
It was tested on the following versions:
 * 2.7
 * 2.9

### Operating systems

Tested with molecule on Ubuntu 18.04 and 20.04.
It does not support Fedora, RHEL/Centos, mainly because of gift repository dependency and EPEL has usually a version recent enough.

## Example Playbook

Just include this role in your list.
For example

```
- host: all
  roles:
    - juju4.sleuthkit
```

## Continuous integration

This role has a travis config leveraging molecule for testing

Once you ensured all necessary roles are present, You can test with:
```
$ pip install molecule docker
$ molecule test
$ MOLECULE_DISTRO=ubuntu:18.04 molecule test --destroy=never
```

## Troubleshooting & Known issues

## License

BSD 2-clause
