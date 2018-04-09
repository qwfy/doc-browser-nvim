if exists('g:loaded_docbrowser')
    finish
endif
let g:loaded_docbrowser = 1

" utility functions
" ====================================================================
" credit: Luc Hermitte, https://stackoverflow.com/a/1534347/7208627
function! _GetVisSelection()
  try
    let a_save = @a
    normal! gv"ay
    return @a
  finally
    let @a = a_save
  endtry
endfunction

" key maps
" ====================================================================
if !exists('g:docbrowser_map')
    let g:docbrowser_map = 1
endif
if g:docbrowser_map == 1
    nnoremap <leader>b :call DocbrowserSummon(expand("<cword>"))<CR>
    xnoremap <leader>b :call DocbrowserSummon(_GetVisSelection())<CR>
endif
