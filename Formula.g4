grammar Formula;
formula: 'import' NAME           # Import
     | expr EOF                  # BareExpr
     ;
expr : expr '[' indexes ']'      # GetItem
     | expr op=('*'|'/') expr    # MulDiv
     | expr op=('+'|'-') expr    # AddSub
     | '[' args ']' '->' expr    # Lambda
     | UINT                      # Uint
     | UFLOAT                    # Ufloat
     | (NAME '::')+ NAME         # Namespaced
     | NAME                      # Name
     | QUOTED                    # Quoted
     | '(' expr ')'              # Parens
     ;
args : arg (',' arg)*;
arg : NAME ':' UINT              # ArgWithSize
    | ':'                        # ArgWithoutName
    | NAME                       # ArgWithoutSize
    ;
indexes : index (',' index)*;
index : UINT                     # UintIndex
      | NAME                     # NameIndex
      | ':'                      # AllIndex
      ;
MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';
UINT : [0-9]+;
UFLOAT : [0-9]+ '.' [0-9]+;
NAME : [a-zA-Z_][a-zA-Z0-9_]*;
QUOTED : '"' (~["\\])* '"';
WS : [ \t\r\n]+ -> skip;
