document.addEventListener("DOMContentLoaded", function () {
    // Reset password button click event listener
    document.getElementById("resetPasswordBtn").addEventListener("click", function (event) {
        event.preventDefault(); // Prevent form submission

        // Get user input
        var userId = document.getElementById("inputID").value;

        // Check if userId is provided
        if (!userId) {
            alert("Please enter your user ID.");
            return;
        }
        // Send request to server to reset password
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/reset_password"); // Assuming your server endpoint for password reset is "/reset_password"
        xhr.setRequestHeader("Content-Type", "application/json");

        // Data to send to server
        var data = JSON.stringify({ userId: userId });

        // Callback function when request is completed
        xhr.onload = function () {
            if (xhr.status === 200) {
                // Password reset successful
                var response = JSON.parse(xhr.responseText);
                alert("Password has been reset for the user ID: " + userId + ". New temporary password: " + response.tempPassword);
            } else {
                // Password reset failed
                alert("Failed to reset password for the user ID: " + userId);
            }
        };

        // Send request with user ID
        xhr.send(data);
    });
});