
# 允许所有ip访问
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip='*'
# 设置验证参数token
c.NotebookApp.token = 'zrrjdd'
# 解决跨域问题
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors self *",
    }
}
# jupyter工作目录
c.NotebookApp.notebook_dir ='/Users/zrrjdd/software/jupyter/workplace'
# 启动时不在浏览器打开
c.NotebookApp.open_browser = False
# 端口
c.NotebookApp.port = 8001