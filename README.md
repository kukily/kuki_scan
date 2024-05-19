# kuki_scan
fofa联动nuclei实现批量漏扫（需要fofa会员），目前只有linux版本

项目介绍


这是一个结合fofa和nuclei的批量漏洞扫描脚本，能够根据给出的关键词进行批量化扫描， 适合放在linux服务器上，可以做到24小时自动扫描

本项目是基于大佬的bug_scan的二次开发，里面加入了一些自己的小思路，做到完全自动化。

其中fofa查询部分调用了fofamap的项目,修改了部分代码：https://github.com/asaotomo/FofaMap

使用说明
把kuki_scan.py和keyword.txt文件放到/root下
把scan文件放到/root下，放好之后scan的目录是/root/scan

环境配置
python3 ：
这个自行安装，我用的python3.8和3.11都能运行，其他应该也没啥问题 

nuclei：
去官方下载nuclei，这里我只讲单文件版本配置方式，github的nuclei官方项目：nuclei 进入release，选择适合自己的版本，这里我用的是amd64的，解压出来然后使用chmod u+x nuclei给予执行权限，然后mv nculei 环境变量目录(放入环境变量就可以在任意目录执行该程序），就可以直接使用了 image.png

不想用默认poc的看这里： 这里推荐两个nuclei 的poc项目：https://github.com/projectdiscovery/nuclei-templates、https://github.com/ExpLangcn/NucleiTP 把其中low和info去掉，然后去掉xss等国内不怎么收的洞就可以了，最后修改bug_scan.sh内nuclei语句添加-t /xxx/xxx/template指定template（也就是poc文件夹）

然后是fofamap的环境配置
我会放在requirements.txt内，大家下载好后进入requirements所在目录内执行命令即可安装依赖： pip3 install -r requirements.txt

使用步骤
给予bug_scan.sh执行权限
scan文件下载好放到/root文件下，进入/root/scan文件内，给予执行权限chmod u+x bug_scan.sh

首先用python运行kuki_scan.py,输入构造好的fofa语句运行
![image](https://github.com/kukily/kuki_scan/assets/156706190/65d86a21-adb9-40fb-9b29-69dba7397139)
![image](https://github.com/kukily/kuki_scan/assets/156706190/9dae94b0-971e-47b7-ad11-d35c708ad080)


注：填写fofa配置(需要fofa会员)
我们将fofamap的配置文件fofa.ini中email和key填写（最好是旧高级会员账号的key），以及根据自己的需求填写其他配置内容即可，而logger一定要设置为on，因为我们就是从日志文件fofamap.log中提取扫描目标的。
还有工具的原理是利用fofamap通过keyword.txt文件里的fofa语句来查询，如果想要多语句或者多任务，可直接配置keyword.txt,然后执行bug_scan.sh就可以实现多语句查询和扫描了

最后输出结果放在/root/scan_result内，cat /root/scan_result即可 一开始scan_result是没东西的，要扫描出来才有，还有如果是服务器建议用screen跑，这样断开会话还能继续扫

声明
本工具仅提供给安全测试人员进行合法安全测试使用 用户滥用造成的一切后果与作者无关 使用者请务必遵守当地法律 本程序不得用于商业用途，仅限学习交流
