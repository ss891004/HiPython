
import hashlib 

msg='hessss'

md5=hashlib.md5(msg.encode('utf-8'))

print(md5.hexdigest())

sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
sha256 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
sha512 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
