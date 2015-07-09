#compdef dropbox
#
# Description:
# Zsh completion script for the Dropbox Command Line Interface (CLI).
# http://www.dropbox.com
#
_dropbox() {
  _values \
    'command' \
    'status[get current status of the dropboxd]' \
    'help[provide help]' \
    'puburl[get public url of a file in your dropbox]' \
    'stop[stop dropboxd]' \
    'running[return whether dropbox is running]' \
    'start[start dropboxd]' \
    'filestatus[get current sync status of one or more files]' \
    'ls[list directory contents with current sync status]' \
    'autostart[automatically start dropbox at login]' \
    'exclude[ignores/excludes a directory from syncing]' \
    'lansync[enables or disables LAN sync]' \
}
