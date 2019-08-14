# amazon-connect-callout
## 1.关于这个例子
这个例子使用了python调用amazon connect服务拨打外部电话，向相关人员播放指定信息。

## 2.amazon connect服务是什么?
Amazon Connect是一个云端托管的拨号中心。更多信息可以参考这个页面[Amazon connect](https://aws.amazon.com/connect/).

## 3.amazon connect服务可以在AWS上做什么?
Amazon connect几乎可以拨打任意地区的电话号码。我们只需要配置简单的联系流，就可以按照预定于的流程拨打指定的号码。我们可以结合IT的运维系统，在出现严重告警的情况下拨打相关人员的电话。

## 4.配置步骤
* 在AWS的console中选择amazon connect service,然后选择'add an instance'添加connect的实例。在这个例子中，我们只需要拨打的权限，所以选择'call out'，你也可以按照需求选择你需要的功能。
![设置amazon connect](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-1.png "设置amazon connect")

* 使用login url登陆connect的dashboard, 然后做相关配置
![登陆connect的dashboard](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-2.png "登陆connect的dashboard")

* 设置connect的电话号码 
![设置connect的电话号码](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-3.png "设置connect的电话号码")

* 设置联系流 contact flow。按照如下所示截图配置，并发布.也可以使用'import flow' 导入例子中的文件'call_out_contact_flow'
![设置联系流](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-4.png "设置联系流")

* 如果你是本地运行，请配置AWS的AKSK。如果使用AWS Lambda运行，请配置相关的IAM Role。

# 注意更改在connect.py的配置参数
