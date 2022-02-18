<?php

if($_POST) {
	$receive = "vanhoof.rowan@gmail.com"
	$full_name = "";
	$email_addr = "";
	$msg_box = "";
	$msg_body = "<div>";

	if(isset($POST['full_name'])) {
		$full_name = filter_var($_POST['full_name'], FILTER_SANITIZE_STRING);
		$msg_body .="<p>Works1</p>"

	}

	if(isset($POST['email_addr'])) {
		$full_name = filter_var($_POST['email_addr'], FILTER_SANITIZE_STRING);
		$msg_body .="<p>Works2</p>"

	}

	if(isset($POST['msg_box'])) {
		$full_name = filter_var($_POST['msg_box'], FILTER_SANITIZE_STRING);
		$msg_body .="<p>Works1</p>"

	}

	$msg_body .="/div"

	$headers = 'MIME-Version: 1.0' . "\r\n"
	         . 'Content-type: text/html; charset = utf-8'. "\r\n"
	         . 'From: ' . $email_addr . "\r\n";

	$subject = 'New message from: ' . $full_name;

	if(mail($recipient, $subject, $msg_body, $headers)) {
        echo "<p>Thank you for contacting me, $full_name, you can expect a reply within 24 hours</p>";
    } else {
        echo '<p>Sorry but the email did not go through.</p>';
    }
	
} else {
	echo '<p>Error</p>';
}
?>