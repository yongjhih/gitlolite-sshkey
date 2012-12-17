# vim: ft=python

from os import environ

# path to config file
environ['WEBSSHKEY_HELPER_CONFIG'] = '/home/sshkey/sshkey/etc/config.py'


activate_py = '/home/sshkey/venv/bin/activate_this.py'
execfile(activate_py, dict(__file__=activate_py))

# or

#import site
#site.addsitedir("/var/lib/web-sshkey-helper/env/lib/pythonX.X/site-packages")


from gitolite_sshkey_form.app import app as application
