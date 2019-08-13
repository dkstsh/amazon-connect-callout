# amazon-connect-callout
## about this sample
this is a sample which use python code to make amazon connect to call out with self defined text. 

## what is amazon connect?
Amazon Connect is a self-service, cloud-based contact center service that makes it easy for any business to deliver better customer service at lower cost. You can find more info at this page [Amazon connect](https://aws.amazon.com/connect/).

## what can this service do in aws?
Amazon connect can call out to almost everyone. You only need configure a contact flow, then you can make a call with a robot voice to say what you want to say to the target number. With this feature, you can call integrate with your monitor system, then call developer, ops, even manager. You also can define your call tree with this system. In this sample, I will show you how to define the contact flow, and how to trigger with python code, which can be deployed in lambda.

## steps to setup the amazon connect
1. select amazon connect service in aws console, and choose 'add an instance', in this example we only need call out, so select the 'call out' checkbox, and you can choose what you need in your application.
![setup amazon connect](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-1.png "setup amazon connect")

2. you can login the connect dashboard with the login url, then setup the configuration
![login to amazon connect dashboard](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-2.png "login to amazon connect dashboard")

3. setup the phone number to call out 
![phone number call out](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-3.png "phone number call out")

4. define the contact flow as below. you can use 'import flow' to import the 'call_out_contact_flow' file in this sample
![define contact flow](https://github.com/forhead/amazon-connect-callout/blob/master/images/connect-sample-4.png "define contact flow")

5. If you run your code in local, please configure the AKSK of your aws account. If you run with lambda, please configure IAM role which can access amazon connect service. 
#please reminder, replace the parameter with yours in connect.py#
