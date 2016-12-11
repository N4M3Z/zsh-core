##
#  @file
#     powerline/init.zsh
#
#  @brief
#     Module for PowerLine
#
#  @author
#     Martin Zeman <martin.zeman@protonmail.ch>
#

pmodload 'environment'

# Determine if command exists
if (( $+commands[powerline-daemon] ))
then
    powerline-daemon -q

    ## Source module files.
    source "${0:h}/external/powerline/bindings/zsh/powerline.zsh"
else
    echo "Powerline not found on your system, please install it, e.g.:"
    echo "> pip install powerline-status"
fi

# if [[ -d "/usr/local/lib/zpython" ]]
# then
#     module_path=($module_path /usr/local/lib/zpython)
#     zmodload -u zpython
# fi
