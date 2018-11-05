reference： https://kopu.chat/2017/08/19/遞迴-recursive-介紹與經典題型/

1. 任何的recursive都可以用iterative来解决
2. recursive的时候，其实每层都放在了memory里面，准确来说是 stack，不停的向stack 中push data

![image](https://github.com/signalwolf/Algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E6%83%B3/image/STACK.png)

3. 故而当recursion 太多的时候，就会产生stack overflow的问题。
4. 当recursion到底的时候会开始pop，这样就
