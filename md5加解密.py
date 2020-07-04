import hashlib
import os
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


class Encrypts:
    """MD5 base64 AES RSA 四种加密方法"""

    def __init__(self):
        self.aes_mode = AES.MODE_ECB  # AES加密模式
        self.aes_key_size = 256  # AES秘钥，随机数值
        self.rsa_count = 2048  # RSA秘钥对，随机数值

    def md5_encrypt(plaintext):
        """ MD5加密
        :param plaintext: 需要加密的内容
        :return: encrypt_str密文
        """
        h1 = hashlib.md5()  # 创建md5对象
        h1.update(plaintext.encode(encoding='utf-8'))  # 必须声明encode
        # 加密
        encrypt_str = h1.hexdigest()
        return encrypt_str

    def base64_encry(plaintext):
        """base64加密"""
        base64_encry = base64.b64encode(plaintext.encode('utf-8'))
        return base64_encry

    def generate_aes_key(self):
        """AES秘钥生成"""
        # length for urandom
        key_size = self.aes_key_size
        u_len = int(key_size / 8 / 4 * 3)
        aes_key = base64.b64encode(os.urandom(u_len))  # os.urandom()生成随机字符串
        return aes_key

    def aes_encrypt(self, message, aes_key):
        """use AES to encrypt message,
        :param message: 需要加密的内容
        :param aes_key: 密钥
        :return: encrypted_message密文
        """
        mode = self.aes_mode  # 加密模式
        if type(message) == str:
            message = bytes(message, 'utf-8')
        if type(aes_key) == str:
            aes_key = bytes(aes_key, 'utf-8')
        # aes_key, message必须为16的倍数
        while len(aes_key) % 16 != 0:
            aes_key += b' '

        while len(message) % 16 != 0:
            message += b' '
        # 加密对象aes
        aes = AES.new(key=aes_key, mode=mode)
        encrypt_message = aes.encrypt(plaintext=message)
        return b2a_hex(encrypt_message)

    def generate_rsa_keys(self):
        """RSA秘钥对生成"""
        rsa_count = self.rsa_count
        # 随机数生成器
        random_generator = Random.new().read
        # rsa算法生成实例
        rsa = RSA.generate(rsa_count, random_generator)
        # master的秘钥对的生成
        rsa_public_key = rsa.publickey().exportKey()
        rsa_private_key = rsa.exportKey()
        return rsa_public_key, rsa_private_key

    def rsa_encrypt(message, rsa_public_key):
        """use RSA to encrypt message,
        :param message: 需要加密的内容
        :param rsa_public_key: 公钥(字节类型）
        :return: encrypt_msg_list密文列表
        """
        pub_key = RSA.importKey(rsa_public_key)
        # 加密对象
        cipher = Cipher_pkcs1_v1_5.new(pub_key)
        msg = message.encode('utf-8')
        # 分段加密
        default_encrypt_length = 245
        length = default_encrypt_length
        msg_list = [msg[i:i + length] for i in list(range(0, len(msg), length))]
        # 加密后信息列表
        encrypt_msg_list = []
        for msg_str in msg_list:
            cipher_text = base64.b64encode(cipher.encrypt(message=msg_str))
            encrypt_msg_list.append(cipher_text)
        return encrypt_msg_list


class Decrypts:
    """base64 AES RSA 三种解密方法"""

    def __init__(self):
        # AES解密模式(须与加密模式一致）
        self.aes_mode = AES.MODE_ECB

    def base64_decry(ciphertext):
        """base64解密"""
        base64_decry = (base64.b64decode(ciphertext)).decode('utf-8')
        return base64_decry

    def aes_decrypt(self, encrypt_message, aes_key):
        """ AES解密
        :param encrypt_message: 密文
        :param aes_key: 秘钥
        :return: decrypt_text解密后内容
        """
        aes_mode = self.aes_mode
        aes = AES.new(key=aes_key, mode=aes_mode)
        decrypted_text = aes.decrypt(a2b_hex(encrypt_message))
        decrypted_text = decrypted_text.rstrip()  # 去空格
        return decrypted_text.decode()

    def rsa_decrypt(encrypt_msg_list, rsa_private_key):
        """ RSA解密
        :param encrypt_msg_list: 密文列表
        :param rsa_private_key: 私钥(字节类型)
        :return  解密后内容
        """
        random_generator = Random.new().read
        pri_key = RSA.importKey(rsa_private_key)
        cipher = Cipher_pkcs1_v1_5.new(pri_key)
        # 解密后信息列表
        msg_list = []
        for msg_str in encrypt_msg_list:
            msg_str = base64.decodebytes(msg_str)
            de_str = cipher.decrypt(msg_str, random_generator)
            msg_list.append(de_str.decode('utf-8'))
        return ''.join(msg_list)


##

import hashlib
import datetime
#import sys
def Findmd5(args):
    md=args.hashvalue
    starttime=datetime.datetime.now()
    for i in open(args.file):
        md5=hashlib.md5()   #获取一个md5加密算法对象
        rs=i.strip()    #去掉行尾的换行符
        md5.update(rs.encode('utf-8'))  #指定需要加密的字符串
        newmd5=md5.hexdigest()  #获取加密后的16进制字符串
        #print newmd5
        if newmd5==md:
            print('明文是：'+rs )   #打印出明文字符串
            break
        else:
            pass

    endtime=datetime.datetime.now()
    print (endtime-starttime)	#计算用时，非必须

if __name__=='__main__':
    import argparse #命令行参数获取模块
    parser=argparse.ArgumentParser(usage='Usage:./findmd5.py -l 密码文件路径 -i 哈希值 ',description='help info.')   #创建一个新的解析对象
    parser.add_argument("-l", default='wordlist.txt', help="密码文件.", dest="file")    #向该对象中添加使用到的命令行选项和参数
    parser.add_argument("-i", dest="hashvalue",help="要解密的哈希值.")

    args = parser.parse_args()  #解析命令行
    Findmd5(args)





