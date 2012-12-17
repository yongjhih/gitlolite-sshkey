# Gitolite-admin repository to clone (optional)
ADMIN_REPO   = 'ssh://qrd8x30@10.8.24.7/gitolite-admin.git'

# Location of ADMIN_REPO working copy. If ADMIN_REPO is set, the webapp will
# clone it into WORKDIR. Adding or removing a key will trigger a push to
# ADMIN_REPO.
#
# If ADMIN_REPO is not set (or set to ''), WORKDIR is just a directory for
# storing keys.
WORKDIR      = '/home/sshkey/gitolite-admin' # absolute path

# gitolite-admin branch to which keys should be pushed (optional)
BRANCH       = 'master'

# author/email to use when adding keys to gitolite-admin
AUTHOR_NAME  = 'Gitolite Publickey Form'
AUTHOR_EMAIL = 'sshkey@gitsync.gbc.intra'

# enable/disable the identities functionality (optional
ENABLE_IDENTITIES = False
IDENTITIES_DB = 'sshkey.db'

# show public key addition/removal log on /log
ENABLE_LOG = True
