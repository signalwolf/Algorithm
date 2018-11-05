Reference： https://kopu.chat/2017/08/19/遞迴-recursive-介紹與經典題型/

Recursion：递归
Iterative：迭代

1. 任何的recursive都可以用iterative来解决
2. recursive的时候，其实每层都放在了memory里面，准确来说是 stack，不停的向stack 中push data

![image](https://github.com/signalwolf/Algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E6%83%B3/image/STACK.png)

3. 故而当recursion 太多的时候，就会产生stack overflow的问题。
4. 当recursion到底的时候会开始pop，这样知道 stack被清空之后。所以recursion 的 space要求是高的
5. 另外注意的是每次的push 与 pop 其实是消耗时间的，故而iterative的方法会更好。
6. Recursion 与 iterative 的对比：时间复杂度相同，空间复杂度上递归更大
   Recursion:
    1. 优点：代码数量小；暂存的变量小
    2. 缺点：程序执行时间较长；需要额外的stack的支持，故而容易stack overflow
   Iterative:
    1. 优点：执行时间短，无需额外的stack的支持
    2. 缺点：代码冗长或者非常难编写

7. 递归与迭代的思维：
    递归是尝试将问题变小后逐步解决问题，当问题足够小的时候回归上层让上层去解决更复杂的问题
    迭代是
 
    
      
