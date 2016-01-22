" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! C4bPoints()
python << endOfPython

from c4bvim import c4b_show_points
c4b_show_points()

endOfPython
endfunction

function! C4bShare()
python << endOfPython

import vim
from c4bvim import c4b_share
response = c4b_share("\n".join(vim.current.buffer[:]))

endOfPython
endfunction

function! C4bSetInfo(name,server)
python << endOfPython

import vim
from c4bvim import c4b_set_info

name = vim.eval('a:name')
server = vim.eval('a:server')

c4b_set_info(name, server)

endOfPython
endfunction

function! C4bGetInfo()
python << endOfPython

import json
from c4bvim import c4b_get_info
info = c4b_get_info()
print(json.dumps(info, indent=4))

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! C4bPoints call C4bPoints()
command! C4bShare call C4bShare()
command! -nargs=+ C4bSetInfo call C4bSetInfo(<f-args>)
command! C4bGetInfo call C4bGetInfo()
