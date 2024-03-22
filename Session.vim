let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Computer-Networks-and-Data-Communications
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/Computer-Networks-and-Data-Communications
badd +1 ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/server.py
badd +12 ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py
badd +1 term://~/Computer-Networks-and-Data-Communications//105881:/bin/bash
badd +1 term://~/Computer-Networks-and-Data-Communications//105905:/bin/bash
argglobal
%argdel
$argadd ~/Computer-Networks-and-Data-Communications
edit ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/server.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd w
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 1resize ' . ((&columns * 118 + 118) / 237)
exe '2resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 2resize ' . ((&columns * 118 + 118) / 237)
exe '3resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 3resize ' . ((&columns * 118 + 118) / 237)
exe '4resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 4resize ' . ((&columns * 118 + 118) / 237)
argglobal
balt ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 8 - ((7 * winheight(0) + 16) / 33)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 034|
wincmd w
argglobal
if bufexists(fnamemodify("~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py", ":p")) | buffer ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py | else | edit ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py | endif
if &buftype ==# 'terminal'
  silent file ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/client.py
endif
balt ~/Computer-Networks-and-Data-Communications/Projects/Project2/single-server/server.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 12 - ((11 * winheight(0) + 16) / 33)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 12
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("term://~/Computer-Networks-and-Data-Communications//105881:/bin/bash", ":p")) | buffer term://~/Computer-Networks-and-Data-Communications//105881:/bin/bash | else | edit term://~/Computer-Networks-and-Data-Communications//105881:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Computer-Networks-and-Data-Communications//105881:/bin/bash
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 16) / 33)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("term://~/Computer-Networks-and-Data-Communications//105905:/bin/bash", ":p")) | buffer term://~/Computer-Networks-and-Data-Communications//105905:/bin/bash | else | edit term://~/Computer-Networks-and-Data-Communications//105905:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Computer-Networks-and-Data-Communications//105905:/bin/bash
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 11 - ((10 * winheight(0) + 16) / 33)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 0
wincmd w
exe '1resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 1resize ' . ((&columns * 118 + 118) / 237)
exe '2resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 2resize ' . ((&columns * 118 + 118) / 237)
exe '3resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 3resize ' . ((&columns * 118 + 118) / 237)
exe '4resize ' . ((&lines * 33 + 35) / 70)
exe 'vert 4resize ' . ((&columns * 118 + 118) / 237)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
