
@(Python)[CH2]

### 个人教程



## MVP

#### Minimum Viable Product 最小可行产品
CH2是首次完整的按照MVP的节奏进行编写的
1. 首先实现Json的内容返回。
2. 实现单个城市的天气信息显示。
3. 封装函数实现通过输入不同城市获得相关天气信息的功能。
4. 实现其他help, exit，history 功能，同时history发现比较难，随即决定先实现简单显示。
5. 程序整个运转良好，重点放在history的显示上....发现异常困难...滴答滴答...时间流逝。
6. 随即决定放弃，回头来看同学们是如何实现的。
7. ing，虽然history的显示这块还没有开始仔细研究同学们的代码，但这次程序的开发过程相当愉悦和踏实。



## 有感于CH2时的大坑



本周躺了有史以来最大的坑

#### Pip

- 因为Python是用anacoda3安装的，所以在调用pip安装virtualenv时，直接在GitBash中使用 pip install virtualenv 会报 failed, 最后使用“py36 -m pip install virtualenv” 安装成功，这是因为用anacoda3安装的python，所以在安装virtualenv时要先确保在python（py36属个人修改）安装路径下调用pip. 如果不知道系统调用的python在哪里，可以在Bash中使用“which " 语句，比如 "which python" "which pip"....


#### Virtualenv
- Install Virtualenv 时要注意要在哪个路径下创建新的env，GitBash就应该指向这个路径.



- Virtualenv's activate and deactivate
1. 首先要 修改你的 “execution policies”, 这样windows才回去执行相关拷贝下来的脚本， as following:
[How to change your Windows execution policies][1]
***note***: 因为修改execution policies是在Powershell 中，所以一定一定要以 Administrator 的身份进入Powershell 如下：
[Run as Administrator][2]
2. Activate
使用绝对路径进行激活，记住windows中最后的activate.ps1文件是在env/Scripts下面，Mac是在env/bin下面，所以使用绝对路径激活，激活后把路径加入系统的环境变量，这样python等所有模块再下次打开Powershell后只需输入“Activate”命令即可直接进入新env。
使用绝对路径:
> C:\Users\CNNEZHA2\AppData\Local\Continuum\Anaconda3\envs\Py36\Scripts\my_env\Scripts> activate.ps1


3. 如果再创建一个新的env，怎么去激活？
> 比如新环境her_env，也是用绝对路径来激活, **注意** 这里要用到**".\"**让Powershell去读取脚本，如下：
>[How to activate another env][3]



-----


#### 总结
熟悉了Python在windows 7 下的运行环境，pip 的使用，以及使用virtuelenv创建新的与主系统隔离的python环境，通过反复捣腾，也对windows系统认知也有了一定加强，比如环境变量Environment Variables 的作用，execution policies...
内心对之前Python运行环境的陌生感随即消失，接下来会更专注代码本身.

-----

[Excellent Lessons learn for CH2](https://github.com/Leon-Huang/Py101-004/blob/master/Chap2/note/README.md)















-----
[1]: https://github.com/Gouwal/Py101-004/blob/master/Chap2/note/execution%20policies_03.png?raw=true
[2]: https://github.com/Gouwal/Py101-004/blob/master/Chap2/note/Execution%20Policy_01.png?raw=true
[3]: https://github.com/Gouwal/Py101-004/blob/master/Chap2/note/How%20to%20activate%20another%20env_02.png?raw=true
