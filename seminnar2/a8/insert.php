<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "admin";
$message="";
// Create connection
if(count($_POST)>0)
{
$con = mysqli_connect($servername, $username, $password, $dbname) or die('Unable To connect');
$sql="INSERT INTO login_user (userid,username,password)
VALUES ('$_POST[id]','$_POST[name]','$_POST[pw]')";

if (!mysqli_query($con,$sql))
  {
  die('SQL query error');
  }
else 
$message="one record added";
}
?>
<html>
  <body bgcolor="Pale Blue">
    <h1 align="Center" > User Registration </h1>
    <br>
    <form action="" method="post" align="center" >
      Userid:<input type="text" name="id"> <br><br><br>
      Username:<input type="text" name="name"> <br><br><br>
      Password:<input type="password" name="pw"> <br><br><br>
      <input type="submit" value="SUBMIT">
      <input type="reset" value="RESET">

      <br>
      <br>
      <br>
<div class="message" > <?php if($message!="") { echo $message; } ?></div>
    </form>
  </body>
</html>