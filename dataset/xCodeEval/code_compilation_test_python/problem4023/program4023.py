def program4023():
    
         zqz050928
    洛谷 / 题目列表 / 题目详情 
    CF68A Irrational problem
    Luogu
    应用 
    题库
    训练
    比赛
    记录
    讨论
    388
    通过
    607
    提交
    题目来源 CodeForces 68A
    评测方式 RemoteJudge
    标签
    难度 入门难度
    时空限制 2000ms / 256MB
     提交   题解    
    提示：收藏到任务计划后，可在首页查看。
    体验新版界面
    
    最新讨论 显示
    推荐的相关题目 显示
    题意翻译
    输入p1、p2、p3、p4，输入a和b，求在[a,b]这个区间内有多少个数%p1、%p2、%p3、%p4后还是它本身
    
    Translated by @夜刀神十香ღ
    
    题目描述
    Little Petya was given this problem for homework:
    
    You are given function  (here represents the operation of taking the remainder). His task is to count the number of integers x x in range [a;b] [a;b] with property f(x)=x f(x)=x .
    
    It is a pity that Petya forgot the order in which the remainders should be taken and wrote down only 4 numbers. Each of 24 possible orders of taking the remainder has equal probability of being chosen. For example, if Petya has numbers 1, 2, 3, 4 then he can take remainders in that order or first take remainder modulo 4, then modulo 2, 3, 1. There also are 22 other permutations of these numbers that represent orders in which remainder can be taken. In this problem 4 numbers wrote down by Petya will be pairwise distinct.
    
    Now it is impossible for Petya to complete the task given by teacher but just for fun he decided to find the number of integers  with property that probability that f(x)=x f(x)=x is not less than $ 31.4159265352718281828459045% $ . In other words, Petya will pick up the number x x if there exist at least 7 7 permutations of numbers p_{1},p_{2},p_{3},p_{4} p 
    1
    ​	 ,p 
    2
    ​	 ,p 
    3
    ​	 ,p 
    4
    ​	  , for which f(x)=x f(x)=x .
    
    输入输出格式
    输入格式：
    First line of the input will contain 6 integers, separated by spaces: p_{1},p_{2},p_{3},p_{4},a,b p 
    1
    ​	 ,p 
    2
    ​	 ,p 
    3
    ​	 ,p 
    4
    ​	 ,a,b ( 1<=p_{1},p_{2},p_{3},p_{4}<=1000,0<=a<=b<=31415 1<=p 
    1
    ​	 ,p 
    2
    ​	 ,p 
    3
    ​	 ,p 
    4
    ​	 <=1000,0<=a<=b<=31415 ).
    
    It is guaranteed that numbers p_{1},p_{2},p_{3},p_{4} p 
    1
    ​	 ,p 
    2
    ​	 ,p 
    3
    ​	 ,p 
    4
    ​	  will be pairwise distinct.
    
    输出格式：
    Output the number of integers in the given range that have the given property.
    
    输入输出样例
    输入样例#1： 复制
    2 7 1 8 2 8
    输出样例#1： 复制
    0
    输入样例#2： 复制
    20 30 40 50 0 100
    输出样例#2： 复制
    20
    输入样例#3： 复制
    31 41 59 26 17 43
    输出样例#3： 复制
    9
    
    在洛谷，
    享受Coding的欢乐
    
    关于洛谷 | 帮助中心 | 用户协议 | 联系我们 
    小黑屋 | 陶片放逐 | 社区规则 | 招贤纳才 
    2013-2019 , 洛谷 © Developed by the Luogu Dev Team 
    陕ICP备17005722号-1 All rights reserved.