[![Build Status - Master](https://travis-ci.org/juju4/ansible-sleuthkit.svg?branch=master)](https://travis-ci.org/juju4/ansible-sleuthkit)
[![Build Status - Devel](https://travis-ci.org/juju4/ansible-sleuthkit.svg?branch=devel)](https://travis-ci.org/juju4/ansible-sleuthkit/branches)

# Sleuthkit install

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

Tested with molecule on Ubuntu 18.04

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
