import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("name,version", [
    ("sleuthkit", "4.6"),
    ("libtsk-dev", "4.6"),
    ("libtsk-dbg", "4.6"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


@pytest.mark.parametrize("filename,filemode", [
    ("/usr/bin/hfind", "0o755"),
    ("/usr/bin/ils", "0o755"),
    ("/usr/bin/sorter", "0o755"),
    ("/usr/lib/libtsk.so.13.4.6", "0o644"),
])
def test_files(host, filename, filemode):
    f = host.file(filename)
    assert f.exists
    assert f.user == 'root'
#    assert f.mode == filemode


# def test_commands(self):
#     out = Command.check_output("hfind -V")
#     out2 = Command.check_output("ils -V")
#     assert out == "The Sleuth Kit ver 4.6.5"
#     assert out2 == "The Sleuth Kit ver 4.6.5"
