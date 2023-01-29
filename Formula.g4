grammar Formula;
formula: expr EOF;
expr : expr op=('*'|'/') expr    # MulDiv
     | expr op=('+'|'-') expr    # AddSub
     | '[' args ']' '->' expr    # Lambda
     | UINT                      # uint
     | UFLOAT                    # ufloat
     | NAME                      # name
     | '(' expr ')'              # parens
     ;
args : arg (',' arg)*;
arg : NAME ':' UINT              # ArgWithSize
    | ':'                        # ArgWithoutName
    | NAME                       # ArgWithoutSize
    ;
MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';
UINT : [0-9]+;
UFLOAT : [0-9]+ '.' [0-9]+;
NAME : [a-zA-Z_][a-zA-Z0-9_]*;
WS : [ \t\r\n]+ -> skip;
