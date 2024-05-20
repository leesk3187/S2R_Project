document.addEventListener("DOMContentLoaded", function () {
    // Reset password button click event listener
    document.getElementById("resetPasswordBtn").addEventListener("click", function (event) {
        event.preventDefault(); // Prevent form submission

        // Get user input
        var userId = document.getElementById("inputID").value;
        var dbPassword = document.getElementById("DBpw").value; // Assuming inputPassword is the ID for the input field containing the password

        // Check if userId and password are provided
        if (!userId || !dbPassword) {
            alert("Please enter your user ID and password.");
            return;
        }

        // Call the check_userid_dbpw function to verify user ID and password
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/check_userid_dbpw"); // Assuming your server endpoint for checking user ID and password is "/check_userid_dbpw"
        xhr.setRequestHeader("Content-Type", "application/json");

        // Data to send to server
        var data = JSON.stringify({ userId: userId, dbPw: dbPassword }); // Make sure the property names match the server expectations

        // Callback function when request is completed
        xhr.onload = function () {
            if (xhr.status === 200) {
                // Password reset successful
                var response = JSON.parse(xhr.responseText);
                if (response.tempPassword) {
                    // If temporary password is received
                    alert("Password has been reset for the user ID: " + userId + ". New temporary password: " + response.tempPassword);
                } else {
                    // If user ID and password don't match
                    alert("Incorrect user ID or password.");
                }
            } else {
                // Request failed
                alert("Failed to verify user ID and password.");
            }
        };

        // Send request with user ID and password
        xhr.send(data);
    });
});
