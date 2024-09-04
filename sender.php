//Sender PHP

<?php 
//In this code we will use shell_exec() and escapeshellarg() to pass variables to Pyton (receiver.py)

$email_subj = "Sample Subject"; // count [1]
$email_add = "sample@gmail.com"; // count [2]
$email_body = "This is a message. Thank you!"; // count [3]
$email_sender = "sender@gmail.com"; // count [4]

$body = escapeshellarg($email_body); // This is to allow us to transfer sentences and multiple lines 

//To transfer file
echo shell_exec("python ./receiver.py $email_subj $email_add $body $email_sender");


?>
