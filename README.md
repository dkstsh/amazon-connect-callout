# amazon-connect-callout
## 1.about this sample
This sample uses python code to call amazon connect, which can call out with aws polly's voice reading defined text. 

## 2.what is amazon connect?
Amazon Connect is a self-service, cloud-based contact center service that makes it easy for any business to deliver better customer service at lower cost. You can find more info at this page [Amazon connect](https://aws.amazon.com/connect/).

## 3.what can this service do in aws?
Amazon connect can call out to almost everyone. You only need configure a contact flow, then you can make a call with a robot voice to say what you want to say to the target number. With this feature, you can call integrate with your monitor system, then call developer, ops, even manager. You also can define your call tree with this system. In this sample, I will show you how to define the contact flow, and how to trigger with python code, which can be deployed in lambda.

## 4.steps to setup the amazon connect
* select amazon connect service in aws console, and choose 'add an instance', in this example we only need call out, so select the 'call out' checkbox, and you can choose what you need in your application.
![setup amazon connect](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-1.png "setup amazon connect")

* you can login the connect dashboard with the login url, then setup the configuration
![login to amazon connect dashboard](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-2.png "login to amazon connect dashboard")

* setup the phone number to call out 
![phone number call out](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-3.png "phone number call out")

* define the contact flow as below. you can use 'import flow' to import the 'call_out_contact_flow' file in this sample
![define contact flow](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-4.png "define contact flow")

* If you run your code in local, please configure the AKSK of your aws account. If you run with lambda, please configure IAM role which can access amazon connect service. 

# please reminder, replace the parameter with yours in connect.py
