'''
`url` `uni`

`a2` `a8` `a16` `b16` `b32` `a36` `b36` 

`a58` `b58` `a62` `b62` `b64` `a85` `b85` `b91`

`md5` `sha1` `sha224` `sha256` `sha384 ``sha512`

`blake2b` `blake2s`

`sha3_224` `sha3_256` `sha3_384` `sha3_512`

`shake_128` `shake_256`

	>>> bencode(s:all,salt='')->byte_type
	>>> bdecode(s:all,p=('',False,))->byte_type
	>>> basecode(s:all,api:int,en=True,normal=True,ab:str=None)->str
	>>> hashcode(s:all,api:str)->str
'''

from tols._other import othercode,_other_set1
from tols._hash import hashcode,_hash_set1,_hash_set2
from tols._base import basecode,_base_set1

# apiset={
# 	'other':list(_other_set1),
# 	'hash':list(_hash_set1|_hash_set2),
# 	'base':list(_base_set1),
# }

print('import',__name__,'succ')
