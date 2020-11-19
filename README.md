# RSA 密码体制

独立选取两个大素数$p$和$q$(各 100~200 位十进制数字),计算
$$n=p\times q$$
其欧拉函数值为
$$\varphi(n)=(p-1)(q-1)$$
随机选一整数$e$,$1\le e<\varphi(n)$,$(\varphi(n),e)=1$.因而在模$\varphi(n)$下,$e$有逆元
$$d=e^{-1}\ mod\varphi(n)$$
取公钥为$n$,$e$.密钥为$d$($p$,$q$不再需要,可以销毁).
加密:将明文分组,各组在$mod\ n$下,可唯一地表示出来(以二元数字表示,选$2$的最大幂小于$n$).可用明文集为
$$A_z=\{m:1\le m< n,(m,n)=1\}$$
注意,$(m,n)\ne1$是很危险的.$m\in A_z$的概率
$$\frac{\varphi(n)}{n}=\frac{(p-1)(q-1)}{pq}=1-\frac{1}{p}-\frac{1}{q}+\frac{1}{pq}\rightarrow 1$$
密文
$$c=m^e\ mod\ n$$
解密:
$$m=c^d\ mod\ n$$
证明:$c^d=(m^e)^d=m^(de)$,因为$de\equiv 1\ mod\varphi(n)$而有$de\equiv q\varphi(n)+1$.由欧拉定理,$(x,n)=1$意味$x^{\varphi(n)}\equiv 1\ mod\ n$,故有
$$c^d=m^{de}=x^{q\varphi(n)+1}=x\cdot x^{q\varphi(n)}=x\cdot 1=x\ mod\ n$$
陷门函数:$Z=(p,q,d)$
