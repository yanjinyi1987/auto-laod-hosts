# auto-laod-hosts
自动的更新laod.cn提供的hosts


1 需要安装的软件

  python 2.7 [from official site]
  
    sudo -H pip install bs4 requests
  
  git, wget, Pillow module installation:
  
  MAC OSX
  
  homebrew for mac
  
    brew install wget libjpeg git
    
    sudo -H pip install pillow
  
  Ubuntu
  
  sudo apt-get install python-PIL python-pil python-imaging python-pil.imagetk wget git
  
  2 下载&&运行
  
  git clone https://github.com/yanjinyi1987/auto-laod-hosts.git
  
  ./run.sh #可能会有窗口弹出要求输入验证码
