#### 安装外库
python -m pip install flask  

#### 修改启动端口
vi run.py  
找到port  

#### 启动
nohup python3 run.py > out.file 2>error.file &  

#### 关闭进程
lsof -i:8080  
端口为修改后的启动端口，然后使用kill命令  