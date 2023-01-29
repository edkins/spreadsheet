grammar Formula;
expr : expr op=('*'|'/') expr   # MulDiv
     | expr op=('+'|'-') expr   # AddSub
     | NUMBER                   # number
     | NAME                     # name
     | '(' expr ')'             # parens
     ;
MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';
NUMBER : [0-9]+;
NAME : [a-zA-Z_][a-zA-Z0-9_]+;
WS : [ \t\r\n]+ -> skip;
