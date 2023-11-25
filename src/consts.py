from binary import *

# instructions
cpu_add =       Binary(65535)
cpu_sub =       Binary(65534)
cpu_mod_reg1 =  Binary(65533)
cpu_mod_reg2 =  Binary(65532)
cpu_jmp =       Binary(65531)
cpu_jg =        Binary(65530)
cpu_jl =        Binary(65529)
cpu_je =        Binary(65528)
cpu_write =     Binary(65527)
cpu_recall =    Binary(65526)
cpu_memwrite =  Binary(65525)
cpu_memread =   Binary(65524)
cpu_halt =      Binary(65523)

# register pointers
rp1 =           Binary(65522)
rp2 =           Binary(65521)
rp3 =           Binary(65520)
rp4 =           Binary(65519)
rp5 =           Binary(65518)

NULL =          Binary(0)
