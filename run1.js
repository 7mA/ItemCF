var exec = require('child_process').exec;
var filename = 'ItemCF1.py'
var recommenduser = "dingdanglbh"
var neighbornum = "3"
var recommendnum = "10"
exec('python'+' '+filename+' '+recommenduser+' '+neighbornum+' '+recommendnum,function(err,stdout,stderr){
    if(err)
    {
        console.log('stderr',err);
    }
    if(stdout)
    {
//        console.log(stdout);	
    }
});