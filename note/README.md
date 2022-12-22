# 二次开发的主要功能
## 20220308
- ~~1.直接通过修改Jupyter 源码，实现 编译开发~~
- ~~2.实现用户 用户名和密码登录注册功能~~
- ~~3.实现session ~~
- 4.每次用户登录，默认进入自己的文件夹目录
- 5.实现用户-角色-目录权限设置
- 6.集成单点登录


# Jupyter 二级开发记录

## 启动

```shell

# 卸载notebook
pip uninstall notebook -y
# 拉取源码
git clone https://github.com/jupyter/notebook
cd notebook
# 安装依赖包
pip install -e .  -i  https://pypi.tuna.tsinghua.edu.cn/simple
# 编译js 和 css
npm run build
# 启动
python -m notebook --port 8989
```


## 问题

### 1.用户名或密码错误，render 到 login1.html 中，login1.html 不显示。

```python
# 代码位置 在login.py LoginHandler 的 post方法中。

# 问题原因 没有 return
```






