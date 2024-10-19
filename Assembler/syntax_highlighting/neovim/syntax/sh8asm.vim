" Define syntax highlighting for SH8 assembly
syntax keyword sh8Keyword dw
syntax match sh8Directive /\.org/

syntax keyword sh8Instruction MOV CALL JMP RET AND
syntax match sh8Register /\b@\=R\d\+\b/
syntax match sh8HexNumber /0x[0-9A-Fa-f]\+/
syntax match sh8Immediate /#[0-9A-Fa-fx]\+/
syntax match sh8Label /^[a-zA-Z_][a-zA-Z0-9_]*:/

" Set highlighting colors
highlight link sh8Keyword Keyword
highlight link sh8Directive Keyword
highlight link sh8Instruction Statement
highlight link sh8Register Identifier
highlight link sh8HexNumber Number
highlight link sh8Immediate Constant
highlight link sh8Label Label
