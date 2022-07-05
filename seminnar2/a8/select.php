<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "admin";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT userid, username FROM login_user";
$result = $conn->query($sql);
echo "<table>";
echo "<tr>";
echo "<th> UserId</th>";
echo "<th> User Name </th>";
echo "</tr>";
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
   // echo "userid: " . $row["userid"]. " - Name: " . $row["username"]. "<br>";
    $id=$row["userid"];
    $name=$row["username"];
        echo "<tr> <td>" . $id."</td><td>". $name ."</td></tr>";
  }
  echo "</table>";
} 

else {
  echo "0 results";
}

$conn->close();
?>