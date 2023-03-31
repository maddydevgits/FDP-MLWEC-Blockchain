const sms=artifacts.require('sms');

module.exports=function(deployer){
    deployer.deploy(sms);
}