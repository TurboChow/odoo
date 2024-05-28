#### docker部署说明
1. 自定义模块需要放在addons/17.0下；
2. 增加自定义模块需要修改docker-compose.yml里面的command命令；
3. docker-compose.yml里面的volumes配置的映射目录根据实际情况修改；
4. 修改config里面的数据库连接信息