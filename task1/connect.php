<?php
	$firstname = $_POST['firstname'];
	$lastname = $_POST['lastname'];
	$email = $_POST['email'];
	$password = $_POST['password'];
	$regno = $_POST['regno'];
	$DOB = $_POST['DOB'];
	$Age = $_POST['Age'];
	$Address = $_POST['Address'];
	$comments = $_POST['comments'];
	$conn = new mysqli('localhost','root','','reg');
$sql="INSERT INTO reg(firstname,lastname,email,password,regno,DOB,Age,Address,comments) VALUES('$firstname','$lastname','$email','$password','$regno','$DOB','$Age','$Address','$comments')";
$ss=mysqli_query($conn,$sql);
if($ss){
	echo "Form submited";
}
else{
	echo "Form not submited";
}
mysqli_close($conn);
?>