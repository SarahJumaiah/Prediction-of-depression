<?php
$serverName = "localhost";
$userName = "root";
$password = "";
$dbName = "users";

// Create connection
$con = mysqli_connect($serverName, $userName, $password, $dbName);

// Check connection
if (mysqli_connect_errno()) {
 echo "Failed to connect to MySQL: " . mysqli_connect_error();
 exit();
}

echo "Connection success";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
// Retrieve the feedback value from the form
$feedback = $_POST["feedback"];

// Prepare the SQL statement to insert the feedback into the database
$sql = "INSERT INTO Users_X (FeedBack) VALUES ('$feedback')";

 // Execute the SQL statement
 if (mysqli_query($con, $sql)) {
echo "Feedback stored successfully";
 } else {
 echo "Error storing feedback: " . mysqli_error($con);
 }
}

mysqli_close($con);
?>